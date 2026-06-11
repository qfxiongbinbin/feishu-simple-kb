# Setup And Auth

Use this reference when the user is installing the skill, using it for the first time, or when a Feishu/Lark command fails because `lark-cli` is missing, unauthenticated, or unauthorized.

## Preflight

1. Check whether `lark-cli` exists:

```bash
lark-cli --version
```

2. If unavailable, tell the user this skill needs a local Feishu/Lark CLI or equivalent Lark API tool. Do not invent credentials or ask for secrets in chat.
3. If available, inspect auth/profile help before login operations:

```bash
lark-cli auth --help
lark-cli wiki --help
lark-cli docs --api-version v2 --help
```

4. If the user is already logged in and the command works, continue directly. Do not ask the user to log in or authorize again just because this is the first time this skill is used in a new agent.
5. Prefer user identity for personal knowledge bases:

```bash
lark-cli auth login
```

## Permission Principles

- Use `--as user` by default for Wiki spaces and personal libraries.
- Treat successful `lark-cli wiki +space-list --as user --format json` or a successful Wiki/Docs command as proof that the local login is usable.
- Ask the user to finish browser/device login if the CLI opens an auth flow.
- If an API reports missing scopes, report the missing scope and ask the user to authorize the app/tool.
- Never paste access tokens, refresh tokens, app secrets, cookies, or private keys into notes or final responses.

## Minimal User-Facing Message

When setup is blocked, say only:

```text
本地还不能操作飞书知识库：缺少 lark-cli 登录/权限。请先完成 lark-cli auth login，完成后我继续创建知识库。
```

Adjust the sentence only when the exact blocker is known.
