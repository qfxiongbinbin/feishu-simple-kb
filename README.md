# Feishu Simple KB

[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
![Codex Skill](https://img.shields.io/badge/Codex-Skill-111827)
![Feishu/Lark](https://img.shields.io/badge/Feishu%20%2F%20Lark-Knowledge%20Base-2563eb)
![LLM Wiki](https://img.shields.io/badge/LLM-Wiki-7c3aed)
![Bilingual](https://img.shields.io/badge/README-中文%20%7C%20English-f97316)
![Version](https://img.shields.io/badge/version-0.1.0-blue)

中文 | [English](#english)

一个给 Codex / AI Agent 使用的飞书三层个人知识库 skill。

它把个人知识库简化成三个用户可见入口：

- `收件箱`：保存原始记录、临时想法、任务和未整理材料
- `笔记`：沉淀长期可复用的主题页、方法、观点和清单
- `归档`：保留不再活跃但仍可能有用的历史内容

底层采用 LLM Wiki 思路：用户负责提供材料、提问和判断重点；Agent 负责把材料持续编译成可复用的知识库，而不是每次问答都从零检索和拼接。

## 它能做什么

- 在飞书个人知识库或指定 Wiki space 下创建三层结构
- 把用户口述或文本写入 `收件箱`
- 从 `收件箱` 编译高价值内容到 `笔记`
- 把过期或已整理的原始记录移动到 `归档`
- 用 `00-控制台` 维护 Schema、Index、Log 和待办视图

## 依赖

- Codex 或兼容本地 skill 的 AI Agent
- `lark-cli`
- 已完成飞书 / Lark 用户身份授权

## 一句话安装

把下面这句话发给你的本地 Agent：

```text
请帮我从 GitHub 安装这个 Codex skill：https://github.com/qfxiongbinbin/feishu-simple-kb 。安装到 ~/.codex/skills/feishu-simple-kb，并提醒我重启 Codex。
```

如果你的 Agent 已经支持 `$skill-installer`，也可以说：

```text
用 $skill-installer 从 GitHub 安装 qfxiongbinbin/feishu-simple-kb 这个 skill。
```

手动安装：

```bash
git clone https://github.com/qfxiongbinbin/feishu-simple-kb.git ~/.codex/skills/feishu-simple-kb
```

安装后重启 Codex，让 skill 被重新发现。

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
└── references/
    ├── command-patterns.md
    ├── llm-wiki-patterns.md
    ├── local-kb-patterns.md
    └── setup-and-auth.md
```

## License

MIT

---

## English

A Codex / AI Agent skill for building a simple three-layer personal knowledge base in Feishu / Lark.

It exposes only three user-facing areas:

- `Inbox`: raw captures, temporary ideas, tasks, and unprocessed material
- `Notes`: compiled long-term knowledge, topic pages, methods, viewpoints, and lists
- `Archive`: historical context that is no longer active but should be preserved

Under the hood, it follows the LLM Wiki pattern: the user provides sources, questions, and judgment; the agent continuously compiles the material into reusable knowledge instead of re-deriving everything from scratch at query time.

## What It Does

- Creates the three-layer structure in a Feishu personal library or a specified Wiki space
- Captures user text or spoken notes into `Inbox`
- Compiles valuable inbox items into `Notes`
- Moves stale or already-processed raw records into `Archive`
- Maintains Schema, Index, Log, and task views in `00-控制台`

## Requirements

- Codex or another local-skill-compatible AI Agent
- `lark-cli`
- Feishu / Lark user authentication for the target knowledge base

## One-Sentence Install

Send this to your local agent:

```text
Please install this Codex skill from GitHub: https://github.com/qfxiongbinbin/feishu-simple-kb . Install it to ~/.codex/skills/feishu-simple-kb and remind me to restart Codex.
```

If your agent supports `$skill-installer`, you can say:

```text
Use $skill-installer to install qfxiongbinbin/feishu-simple-kb from GitHub.
```

Manual install:

```bash
git clone https://github.com/qfxiongbinbin/feishu-simple-kb.git ~/.codex/skills/feishu-simple-kb
```

Restart Codex after installation so the skill can be discovered.

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
