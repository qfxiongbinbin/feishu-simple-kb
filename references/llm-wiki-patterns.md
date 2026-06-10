# LLM Wiki Patterns

This skill adapts the LLM Wiki pattern to Feishu. The user sees a simple three-node knowledge base; the agent operates it as a persistent, compounding wiki.

## Layer Mapping

| LLM Wiki concept | Feishu Simple KB |
|---|---|
| Raw sources | `收件箱` |
| Compiled wiki | `笔记` |
| Schema | `00-控制台 / Schema` |
| Index | `00-控制台 / Index` |
| Log | `00-控制台 / Log` |
| Archive | `归档` |

## Ingest

When processing a new source:

1. Preserve the source in `收件箱`.
2. Identify entities, themes, claims, tasks, and reusable ideas.
3. Search `笔记` for related pages before creating a new one.
4. Update existing pages when the new source strengthens, revises, or contradicts them.
5. Create a new topic page only when no existing page can naturally own the idea.
6. Update Index and append Log.

Do not silently overwrite older conclusions. If the new source conflicts with an existing note, mark the page `contradicted` or add a `待核对` section with both claims.

## Query

When answering:

1. Read Index first.
2. Search likely pages in `笔记`.
3. Include `收件箱` only for recent or unresolved material.
4. Include `归档` only when the user asks for old/history/closed context or when active notes are insufficient.
5. Cite note links in the response.
6. If the answer itself is reusable, ask whether to save it as a new or updated note.

## Lint

Periodic health checks should look for:

- stale pages
- contradicted claims
- orphan notes with no related links
- missing source links
- duplicate or overlapping topic pages
- frequent concepts without a topic page
- inbox items older than the user's threshold

Lint produces a report first. Writes require confirmation unless the user explicitly asked to run an automatic cleanup.

## Page Shape

Stable pages in `笔记` should prefer this shape:

```markdown
# 标题

一句话摘要：
状态：draft / active / stale / contradicted / archived
类型：工作 / 生活 / 学习 / 表达 / 系统 / 待办 / 流水账 / 素材
来源：
最近更新：
相关笔记：

## 结论

## 关键事实

## 关联与冲突

## 更新记录
```

Keep pages concise. The goal is accumulated clarity, not long summaries.
