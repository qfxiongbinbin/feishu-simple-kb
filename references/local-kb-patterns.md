# Local KB Patterns

This reference abstracts proven patterns from a mature personal knowledge base into a generic three-node Feishu version. Do not copy private paths, project names, credentials, or personal content into a user's knowledge base.

## Pattern 1: One Visible Entrance

Keep a single control/overview document that works like a total index:

- Link to `收件箱`, `笔记`, and `归档`.
- Record write rules in plain language.
- Record common user actions.
- Record last organization time and recent changes.

In the three-node version, this is `00-控制台`. It replaces many manual navigation files.

## Pattern 2: Inbox First

New information should land in `收件箱` unless the user explicitly names a target. This reduces capture friction.

Use these statuses:

| Status | Meaning |
|---|---|
| `inbox` | newly captured, not yet processed |
| `active_task` | actionable item still pending |
| `draft` | compiled note exists but has not been reviewed |
| `active` | stable note used for default answers |
| `stale` | likely outdated because newer material exists |
| `contradicted` | conflicts with newer or competing material |
| `notes` | stable knowledge moved into notes |
| `archived` | retained but no longer active |

## Pattern 3: Semantic Routing, Not Folder Routing

Use lightweight metadata instead of creating many folders. Common semantic types:

- `工作`: projects, decisions, operations, customer/client matters
- `生活`: diary, daily records, personal management
- `学习`: books, courses, articles, inputs
- `表达`: writing ideas, public posts, viewpoints, drafts
- `系统`: agent workflows, automation, tool rules
- `待办`: explicit tasks
- `流水账`: time-ordered facts or process records
- `素材`: fragments not yet formed into a note

These are tags/fields. Do not create matching folders unless the user explicitly wants an advanced structure.

## Pattern 4: Query Priority

Default search order:

1. `笔记`: stable conclusions and reusable knowledge
2. `收件箱`: recent captures, active tasks, incomplete material
3. `归档`: old context, closed projects, historical records

Adjust only when the user's wording implies recency, active tasks, or old material.

## Pattern 5: Task Board Without A Separate System

When captured content is a task, keep it in `收件箱` and add metadata:

```markdown
任务状态：未完成
截止时间：未知
责任人：我
```

The control document can keep a simple task view: a list of links grouped by `工作`, `学习`, `生活`, or custom labels. Do not build a separate task database unless the user asks.

## Pattern 6: Archive Means Retain, Not Delete

Archive content that is no longer active but may be useful later:

- completed tasks
- old process notes
- outdated drafts
- material superseded by a better note

Never delete during routine organization.
