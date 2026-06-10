# Command Patterns

Use these patterns as starting points. Always check local `lark-cli ... --help` when flags differ.

## Create Root And Children

Create under the user's personal library:

```bash
lark-cli wiki +node-create --as user --space-id my_library --title "个人知识库" --format json
lark-cli wiki +node-create --as user --parent-node-token "<ROOT_NODE_TOKEN>" --title "00-控制台" --format json
lark-cli wiki +node-create --as user --parent-node-token "<ROOT_NODE_TOKEN>" --title "收件箱" --format json
lark-cli wiki +node-create --as user --parent-node-token "<ROOT_NODE_TOKEN>" --title "笔记" --format json
lark-cli wiki +node-create --as user --parent-node-token "<ROOT_NODE_TOKEN>" --title "归档" --format json
```

Each result usually includes `node_token`, `obj_token`, `obj_type`, `title`, and `resolved_space_id`.

## Create Inside An Existing Feishu Knowledge Base

If the user names an existing knowledge base from the Feishu UI, resolve the Wiki space first:

```bash
lark-cli wiki +space-list --as user --format json
```

Find the exact `name` match and read its `space_id`. Then create the three-node KB root inside that space:

```bash
lark-cli wiki +node-create --as user --space-id "<SPACE_ID>" --title "个人知识库" --format json
lark-cli wiki +node-create --as user --parent-node-token "<ROOT_NODE_TOKEN>" --title "00-控制台" --format json
lark-cli wiki +node-create --as user --parent-node-token "<ROOT_NODE_TOKEN>" --title "收件箱" --format json
lark-cli wiki +node-create --as user --parent-node-token "<ROOT_NODE_TOKEN>" --title "笔记" --format json
lark-cli wiki +node-create --as user --parent-node-token "<ROOT_NODE_TOKEN>" --title "归档" --format json
```

If the user provides a knowledge base or Wiki node URL instead of a name, inspect it first:

```bash
lark-cli wiki +node-get --as user --url "<WIKI_URL>" --format json
```

Use the returned `space_id` and, when relevant, `node_token` as the target. If multiple spaces have similar names, show candidates and ask the user to choose; do not guess.

## Write Or Update Docx Content

Use docs v2 for document content:

```bash
lark-cli docs +update --api-version v2 --doc "<OBJ_TOKEN_OR_URL>" --command overwrite --content "<title>标题</title><p>内容</p>"
lark-cli docs +update --api-version v2 --doc "<OBJ_TOKEN_OR_URL>" --command append --content "<p>追加内容</p>"
lark-cli docs +fetch --api-version v2 --doc "<OBJ_TOKEN_OR_URL>"
```

Prefer XML for structured writes unless the user explicitly asks for Markdown import.

## List Nodes

List children under a root/inbox/notes/archive node:

```bash
lark-cli wiki +node-list --as user --parent-node-token "<NODE_TOKEN>" --page-all --format json
```

If `--page-all` is unavailable in the user's CLI version, paginate manually according to `lark-cli wiki +node-list --help`.

## Move Existing Wiki Nodes

Move an existing note between the three nodes:

```bash
lark-cli wiki +move --as user --node-token "<NODE_TOKEN>" --target-parent-token "<TARGET_NODE_TOKEN>" --format json
```

Only move existing nodes. Do not use docs-to-wiki move mode for this skill unless the user explicitly imports external documents.

## Search

When a scoped node search is unavailable, combine broad Drive search with local filtering:

```bash
lark-cli drive +search --query "<关键词>" --format json
```

Then filter results to documents whose URL/title/path belongs to the configured `个人知识库` root or the three child nodes. Fetch likely candidates before answering.

## Control Console Template

Write this to `00-控制台` after creation and keep it updated:

```markdown
# 00-控制台

这是个人知识库的系统页，用来保存入口、规则、索引和操作日志。日常只需要使用“收件箱、笔记、归档”三个入口。

## 入口

| 区域 | 用途 | 链接 |
|---|---|---|
| 个人知识库 | 根节点 | [打开](<ROOT_URL>) |
| 收件箱 | 保存原始记录、临时想法、任务和未整理材料 | [打开](<INBOX_URL>) |
| 笔记 | 沉淀长期可复用的主题页、方法、观点和清单 | [打开](<NOTES_URL>) |
| 归档 | 保留不再活跃但仍可能有用的历史内容 | [打开](<ARCHIVE_URL>) |

## Schema

| 区域 | 角色 | 说明 |
|---|---|---|
| 收件箱 | raw sources | 保留原始记录，优先保真，不急着整理。 |
| 笔记 | compiled wiki | 把高价值内容编译成稳定知识。 |
| 00-控制台 | schema / index / log | 保存规则、索引、日志和待办视图。 |
| 归档 | historical context | 保留历史上下文，不删除。 |

状态：`inbox` / `draft` / `active` / `stale` / `contradicted` / `archived`

## 规则
- 新内容先进入收件箱。
- 长期有价值的内容移动到笔记。
- 过期但仍需保留的内容移动到归档。
- 不删除；合并、覆盖、批量移动前先确认。

## Index

当前还没有已沉淀的稳定笔记。整理收件箱后，这里记录主题页。

| 笔记 | 摘要 | 类型 | 状态 | 最近更新 |
|---|---|---|---|---|
| 暂无 | - | - | - | - |

## 待办视图

| 分类 | 待办 |
|---|---|
| 工作 | 暂无 |
| 学习 | 暂无 |
| 生活 | 暂无 |

最近整理时间：YYYY-MM-DD HH:mm
最近整理统计：收件箱 0 条，移动到笔记 0 条，移动到归档 0 条

## Log

| 时间 | 动作 | 标题 | 链接 | 备注 |
|---|---|---|---|---|
| YYYY-MM-DD HH:mm | create | 初始化个人知识库 | [打开](<ROOT_URL>) | 创建控制台、收件箱、笔记、归档 |
```
