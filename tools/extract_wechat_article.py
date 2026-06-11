#!/usr/bin/env python3
"""Extract readable text from a WeChat public article page."""

from __future__ import annotations

import argparse
import html
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from html.parser import HTMLParser


class TextExtractor(HTMLParser):
    block_tags = {
        "address",
        "article",
        "blockquote",
        "br",
        "div",
        "h1",
        "h2",
        "h3",
        "h4",
        "h5",
        "h6",
        "li",
        "p",
        "section",
        "table",
        "tr",
    }

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.parts: list[str] = []
        self.skip_depth = 0

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag in {"script", "style", "noscript"}:
            self.skip_depth += 1
            return
        if tag in self.block_tags:
            self._newline()

    def handle_endtag(self, tag: str) -> None:
        if tag in {"script", "style", "noscript"} and self.skip_depth:
            self.skip_depth -= 1
            return
        if tag in self.block_tags:
            self._newline()

    def handle_data(self, data: str) -> None:
        if self.skip_depth:
            return
        text = re.sub(r"\s+", " ", data).strip()
        if text:
            self.parts.append(text)

    def _newline(self) -> None:
        if self.parts and self.parts[-1] != "\n":
            self.parts.append("\n")

    def get_text(self) -> str:
        raw = "".join(self.parts)
        lines = [line.strip() for line in raw.splitlines()]
        text = "\n".join(line for line in lines if line)
        return re.sub(r"\n{3,}", "\n\n", text).strip()


def fetch(url: str, timeout: int) -> str:
    req = urllib.request.Request(
        url,
        headers={
            "User-Agent": (
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
                "AppleWebKit/537.36 (KHTML, like Gecko) "
                "Chrome/125.0 Safari/537.36"
            ),
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
            "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8",
        },
    )
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        charset = resp.headers.get_content_charset() or "utf-8"
        return resp.read().decode(charset, errors="replace")


def js_string_var(page: str, name: str) -> str:
    patterns = [
        rf"var\s+{re.escape(name)}\s*=\s*'((?:\\'|[^'])*)'",
        rf'var\s+{re.escape(name)}\s*=\s*"((?:\\"|[^"])*)"',
    ]
    for pattern in patterns:
        match = re.search(pattern, page)
        if match:
            return decode_js_string(match.group(1))
    return ""


def decode_js_string(value: str) -> str:
    value = value.replace(r"\/", "/")
    if "\\" in value:
        try:
            value = bytes(value, "utf-8").decode("unicode_escape")
        except UnicodeDecodeError:
            pass
    return html.unescape(value).strip()


def meta_content(page: str, key: str) -> str:
    pattern = (
        rf'<meta[^>]+(?:property|name)=["\']{re.escape(key)}["\'][^>]+'
        rf'content=["\']([^"\']*)["\']'
    )
    match = re.search(pattern, page, re.IGNORECASE)
    return html.unescape(match.group(1)).strip() if match else ""


def extract_content_html(page: str) -> str:
    patterns = [
        r'<div[^>]+id=["\']js_content["\'][^>]*>(.*?)</div>\s*<script',
        r'<div[^>]+id=["\']js_content["\'][^>]*>(.*?)</div>\s*</div>\s*</div>',
    ]
    for pattern in patterns:
        match = re.search(pattern, page, flags=re.IGNORECASE | re.DOTALL)
        if match:
            return match.group(1)
    return ""


def extract_article(url: str, timeout: int = 20) -> dict[str, str]:
    parsed = urllib.parse.urlparse(url)
    if parsed.netloc and "mp.weixin.qq.com" not in parsed.netloc:
        raise ValueError("currently only mp.weixin.qq.com article URLs are supported")

    page = fetch(url, timeout)
    content_html = extract_content_html(page)
    if not content_html:
        raise ValueError("could not locate WeChat article content block")

    parser = TextExtractor()
    parser.feed(content_html)
    body = parser.get_text()
    if not body:
        raise ValueError("article content block was found but no readable text was extracted")

    title = js_string_var(page, "msg_title") or meta_content(page, "og:title")
    author = js_string_var(page, "nickname") or meta_content(page, "og:article:author")
    digest = js_string_var(page, "msg_desc") or meta_content(page, "og:description")
    publish_time = ""
    ct = js_string_var(page, "ct")
    if ct.isdigit():
        publish_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(int(ct)))

    return {
        "url": url,
        "title": title or "未命名微信文章",
        "author": author,
        "publish_time": publish_time,
        "digest": digest,
        "content": body,
    }


def to_markdown(article: dict[str, str]) -> str:
    lines = [
        f"# {article['title']}",
        "",
        f"来源链接：{article['url']}",
    ]
    if article.get("author"):
        lines.append(f"作者/公众号：{article['author']}")
    if article.get("publish_time"):
        lines.append(f"发布时间：{article['publish_time']}")
    if article.get("digest"):
        lines.extend(["", "## 摘要", article["digest"]])
    lines.extend(["", "## 正文", article["content"]])
    return "\n".join(lines).strip() + "\n"


def main() -> int:
    parser = argparse.ArgumentParser(description="Extract text from a WeChat article URL.")
    parser.add_argument("url", help="WeChat public article URL, usually https://mp.weixin.qq.com/s/...")
    parser.add_argument("--format", choices=["markdown", "json"], default="markdown")
    parser.add_argument("--timeout", type=int, default=20)
    args = parser.parse_args()

    try:
        article = extract_article(args.url, args.timeout)
    except (ValueError, urllib.error.URLError, TimeoutError) as exc:
        print(f"extract_wechat_article: {exc}", file=sys.stderr)
        return 1

    if args.format == "json":
        print(json.dumps(article, ensure_ascii=False, indent=2))
    else:
        print(to_markdown(article), end="")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
