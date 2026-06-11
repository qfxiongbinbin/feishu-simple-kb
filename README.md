# Feishu Simple KB

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
![Codex Skill](https://img.shields.io/badge/Codex-Skill-111827)
![Feishu/Lark](https://img.shields.io/badge/Feishu%20%2F%20Lark-Knowledge%20Base-2563eb)
![LLM Wiki](https://img.shields.io/badge/LLM-Wiki-7c3aed)
![Bilingual](https://img.shields.io/badge/README-中文%20%7C%20English-f97316)
![Version](https://img.shields.io/badge/version-0.2.0-blue)

中文 | [English](#english)

一个给本地 AI Agent 使用的飞书三层个人知识库 skill，适用于 Codex、OpenClaw、Hermes 等支持本地 skill / 工具目录的 Agent。

它把个人知识库简化成三个用户可见入口：

- `收件箱`：保存原始记录、临时想法、任务和未整理材料
- `笔记`：沉淀长期可复用的主题页、方法、观点和清单
- `归档`：保留不再活跃但仍可能有用的历史内容

底层采用 LLM Wiki 思路：用户负责提供材料、提问和判断重点；Agent 负责把材料持续编译成可复用的知识库，而不是每次问答都从零检索和拼接。

## 它能做什么

- 在飞书个人知识库或指定 Wiki space 下创建三层结构
- 把用户口述或文本写入 `收件箱`
- 用户只说“记录到飞书知识库”时，先检索可访问知识库并请用户确认目标
- 提取微信公众号文章链接，并把标题、来源、摘要和正文保存到 `收件箱`
- 从 `收件箱` 编译高价值内容到 `笔记`
- 把过期或已整理的原始记录移动到 `归档`
- 用 `00-控制台` 维护 Schema、Index、Log 和待办视图

## 依赖

- 支持本地 skill / tools / plugins 的 AI Agent，例如 Codex、OpenClaw、Hermes
- `lark-cli`
- 已完成飞书 / Lark 用户身份授权

如果本地 `lark-cli` 已经登录并且具备目标知识库权限，Agent 会直接使用，不需要用户重复登录或重新授权。只有命令失败时才进入授权排查。

## 让你的 Agent 一句话安装

把下面这句话发给你的本地 Agent：

```text
请把 https://github.com/qfxiongbinbin/feishu-simple-kb 安装成你可发现的本地 skill。根据你的运行环境选择正确的 skills/tools/plugins 目录；安装后告诉我如何重启或重新加载，以及我应该用什么名字调用它。
```

如果你的 Agent 已经支持 skill 安装器，也可以说：

```text
用你的 skill 安装器从 GitHub 安装 qfxiongbinbin/feishu-simple-kb 这个 skill。
```

Codex 手动安装示例：

```bash
git clone https://github.com/qfxiongbinbin/feishu-simple-kb.git ~/.codex/skills/feishu-simple-kb
```

其他 Agent 请把仓库克隆到它自己的 skills / tools / plugins 目录。安装后重启或重新加载 Agent，让 skill 被重新发现。

## 常用口令

创建新的个人知识库：

```text
用 $feishu-simple-kb 帮我搭建一个个人用的管理工作和生活的知识库
```

创建到已有飞书知识库里：

```text
用 $feishu-simple-kb 在“QA大全”这个飞书知识库里创建我的三层知识库
```

存一条记录：

```text
用 $feishu-simple-kb 存一下：今天想到一个知识库搭建思路……
```

只说记录到飞书知识库：

```text
用 $feishu-simple-kb 记录到飞书知识库：今天读到一个关于 AI Agent 的观点……
```

如果目标不明确，Agent 会先列出你可访问的知识库，并问你是否写入某一个知识库。

保存微信公众号文章：

```text
用 $feishu-simple-kb 保存这篇微信文章到飞书知识库：https://mp.weixin.qq.com/s/...
```

## 把收件箱编译成笔记

推荐口令：

```text
用 $feishu-simple-kb 整理一下收件箱，把有长期价值的内容编译成笔记。不要只是移动文件，要提炼结论、保留来源链接、更新控制台 Index 和 Log。合并或覆盖旧笔记前先问我。
```

更具体一点：

```text
用 $feishu-simple-kb 处理收件箱。请逐条判断：
1. 哪些只是流水账，保留或归档；
2. 哪些是任务，留在收件箱并进入待办视图；
3. 哪些有长期价值，编译成笔记；
4. 哪些应该更新已有笔记；
5. 哪些和旧结论冲突，需要标记待核对。

先给我整理计划，不要直接合并或覆盖。
```

如果你想让它直接动手：

```text
用 $feishu-simple-kb 自动整理收件箱：把明确有长期价值的内容编译成笔记，把低价值过期内容归档，把任务保留在收件箱并进入待办视图。合并、覆盖、删除前必须先确认。
```

最短口令：

```text
用 $feishu-simple-kb 清理收件箱，编译成笔记。
```

建议常用第一句。它最能触发正确行为：编译成笔记，而不是分类移动。

## 目录结构

```text
feishu-simple-kb/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── command-patterns.md
│   ├── llm-wiki-patterns.md
│   ├── local-kb-patterns.md
│   └── setup-and-auth.md
└── tools/
    └── extract_wechat_article.py
```

## License

MIT

---

## English

A local AI Agent skill for building a simple three-layer personal knowledge base in Feishu / Lark. It can be used by agents such as Codex, OpenClaw, Hermes, or any agent that supports local skills / tool directories.

It exposes only three user-facing areas:

- `Inbox`: raw captures, temporary ideas, tasks, and unprocessed material
- `Notes`: compiled long-term knowledge, topic pages, methods, viewpoints, and lists
- `Archive`: historical context that is no longer active but should be preserved

Under the hood, it follows the LLM Wiki pattern: the user provides sources, questions, and judgment; the agent continuously compiles the material into reusable knowledge instead of re-deriving everything from scratch at query time.

## What It Does

- Creates the three-layer structure in a Feishu personal library or a specified Wiki space
- Captures user text or spoken notes into `Inbox`
- Lists available knowledge bases and asks for confirmation when the target is ambiguous
- Extracts WeChat public article links and saves the title, source, digest, and body into `Inbox`
- Compiles valuable inbox items into `Notes`
- Moves stale or already-processed raw records into `Archive`
- Maintains Schema, Index, Log, and task views in `00-控制台`

## Requirements

- An AI Agent that supports local skills / tools / plugins, such as Codex, OpenClaw, or Hermes
- `lark-cli`
- Feishu / Lark user authentication for the target knowledge base

If local `lark-cli` is already logged in and authorized for the target knowledge base, the agent should use it directly. It should only enter login or permission troubleshooting when a command fails.

## One-Sentence Agent Install

Send this to your local agent:

```text
Please install https://github.com/qfxiongbinbin/feishu-simple-kb as a local skill that you can discover. Choose the correct skills/tools/plugins directory for your runtime. After installation, tell me how to restart or reload you and what name I should use to invoke it.
```

If your agent has a skill installer, you can say:

```text
Use your skill installer to install qfxiongbinbin/feishu-simple-kb from GitHub.
```

Codex manual install example:

```bash
git clone https://github.com/qfxiongbinbin/feishu-simple-kb.git ~/.codex/skills/feishu-simple-kb
```

For other agents, clone this repository into that agent's own skills / tools / plugins directory. Restart or reload the agent after installation so the skill can be discovered.

## Common Prompts

Create a personal knowledge base:

```text
Use $feishu-simple-kb to create a personal knowledge base for managing my work and life.
```

Create it inside an existing Feishu knowledge base:

```text
Use $feishu-simple-kb to create my three-layer knowledge base inside the Feishu knowledge base named "QA大全".
```

Capture a note:

```text
Use $feishu-simple-kb to save this: today I thought of a new knowledge-base setup idea...
```

Capture to Feishu when the target is not specified:

```text
Use $feishu-simple-kb to record this to my Feishu knowledge base: today I read an idea about AI agents...
```

If the target is ambiguous, the agent will list accessible knowledge bases and ask you to confirm where to write.

Save a WeChat article:

```text
Use $feishu-simple-kb to save this WeChat article to my Feishu knowledge base: https://mp.weixin.qq.com/s/...
```

## Compile Inbox Into Notes

Recommended prompt:

```text
Use $feishu-simple-kb to organize my inbox and compile long-term valuable content into notes. Do not just move files. Extract conclusions, preserve source links, and update the control panel Index and Log. Ask me before merging into or overwriting existing notes.
```

More explicit:

```text
Use $feishu-simple-kb to process my inbox. Judge each item:
1. Which items are just logs, to keep or archive;
2. Which items are tasks, to keep in the inbox and add to the task view;
3. Which items have long-term value and should be compiled into notes;
4. Which items should update existing notes;
5. Which items conflict with older conclusions and should be marked for review.

Give me the organization plan first. Do not merge or overwrite directly.
```

Let it act directly:

```text
Use $feishu-simple-kb to automatically organize my inbox: compile clearly long-term valuable content into notes, archive low-value stale content, and keep tasks in the inbox and task view. Ask before merging, overwriting, or deleting.
```

Shortest prompt:

```text
Use $feishu-simple-kb to clean my inbox and compile it into notes.
```

The recommended prompt is usually best because it triggers the right behavior: compiling knowledge, not merely moving files.
