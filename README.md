# Feishu Simple KB

一个给 Codex / AI Agent 使用的飞书三层个人知识库 skill。

它把个人知识库简化成三个用户可见入口：

- `收件箱`：保存原始记录、临时想法、任务和未整理材料
- `笔记`：沉淀长期可复用的主题页、方法、观点和清单
- `归档`：保留不再活跃但仍可能有用的历史内容

底层采用 LLM Wiki 思路：用户负责提供材料、提问和判断重点；Agent 负责把材料持续编译成可复用的知识库，而不是每次问答都从零检索和拼接。

## What It Does

- 在飞书个人知识库或指定 Wiki space 下创建三层结构
- 把用户口述或文本写入 `收件箱`
- 从 `收件箱` 编译高价值内容到 `笔记`
- 把过期或已整理的原始记录移动到 `归档`
- 用 `00-控制台` 维护 Schema、Index、Log 和待办视图

## Requirements

- Codex or compatible AI Agent with local skill support
- `lark-cli`
- Feishu/Lark user authentication for the target knowledge base

## Install

Clone this repository into your Codex skills directory:

```bash
git clone https://github.com/qfxiongbinbin/feishu-simple-kb.git ~/.codex/skills/feishu-simple-kb
```

Restart Codex so the skill can be discovered.

## Usage

Create a new personal knowledge base:

```text
用 $feishu-simple-kb 帮我搭建一个个人用的管理工作和生活的知识库
```

Create inside an existing Feishu knowledge base:

```text
用 $feishu-simple-kb 在“QA大全”这个飞书知识库里创建我的三层知识库
```

Capture a note:

```text
用 $feishu-simple-kb 存一下：今天想到一个知识库搭建思路……
```

Compile inbox content into notes:

```text
用 $feishu-simple-kb 清理收件箱，编译成笔记。
```

## Structure

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
