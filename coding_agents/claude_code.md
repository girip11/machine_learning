
# Claude Code Tutorial

```bash
cd <project_dir>
# Start claude code on the terminal
claude
```

## Useful CLI commands

- [CLI Reference](https://code.claude.com/docs/en/cli-reference)

```bash
# opens claude code in interactive mode
claude

# Update claude
claude update

# Run a one time task. Best for standalone tasks that doesnt
# need to build upon previous work. After the task completion
# it exits
claude "write a python script to convert JSON to csv."

# Run one off query and exit
claude -p "query"

# continue most recent conversation in the current directory
claude -c

# resume a previous conversation
claude -r <session_name>

# git commit
claude commit

# Start with the model opus/sonnet/haiku
claude --model opus

# configure mcp servers
claude mcp

# start in plan mode
claude --permission-mode plan
```

## Useful slash commands

- `/login` - First time usage. Then the credentials are stored.
- `/help` - Help
- `/exit` - Exit Claude code
- `/resume <session_name>` - Continues previous conversation. `/resume` acts as a session picker if no session is provided.
- `/clear` - Clear the context aka conversation history
- `/init` - Setup CLAUDE.md
- `/model` - Helps switching between the models
- `/stats` - Usage stats
- `/status` - which also displays your account information
- `/agents` - To create subagents
- `/rename <session_name>`  - Name a session. Use the session name with `claude -r` or `/resume`
- - `/memory` - to check the files loaded into memory and to edit

## Configure the [Status line](https://code.claude.com/docs/en/statusline)

- Configure the status line to have the model name, context remaining, git branch to be displayed on the claude code.
- We can write custom python or bash scripts, because Claude passes a [JSON](https://code.claude.com/docs/en/statusline#json-input-structure) to these scripts, which can then extract information and its stdout is what's displayed in the status line.

This goes into the settings.json.

```JSON
{
  "statusLine": {
    "type": "command",
    "command": "bash ~/.claude/statusline-command.sh"
  },
}
```

## Model Selection

- Plan mode - Opus
- Execution mode - Sonnet
- Simple tasks - Haiku

`opusplan` model setting uses Opus for planning and automatically switches to Sonnet for execution.

Use `Shift + Tab` to switch between Plan mode and accept edits model

### System prompt

Claude code's Default system prompt is untouched except using output styles we can turn off some parts of the system prompt.

NOTE: All output styles have their own custom instructions added to the end of the system prompt.

Below are ways to add to the default system prompt.

- `claude --append-system-prompt <prompt>` - Appends to the default system prompt
- Contents of `CLAUDE.md` gets added to the default system prompt.

### Scope

Settings and plugins go into `settings.json`

- Managed(system) - Cannot be overridden
- User - `~/.claude/settings.json`, `~/.claude/agents`, `~/.claude.json`
- Project - Overrides User settings. `<project_dir>/.claude/settings.json`, `CLAUDE.md`, `.mcp.json`
- Local - Overrides project settings. These are very individual specific styles/settings. `<project_dir>/.claude/settings.local.json`, `CLAUDE.local.md`

## [All about Claude.md file](https://claude.com/blog/using-claude-md-files)

BOTTOM LINE: Always start to think of communicating with Claude using file (markdown, JSON) based workflows

- `CLAUDE.md` helps implement the DRY pattern, so we don't have to repeat things in each conversation. This goes from conventions followed in the project, to module relationships etc.
- This file is incorporated in to every conversation as part of the system prompt. So its size matters.
- Provides Claude with the project specific context. Start simple and expand gradually.
- We can split this file into multiple files and reference them in this file. `CLAUDE.md` files can import additional files using `@path/to/import` syntax (relative and absolute paths work). **Paths should not be inside markdown code spans**. Recursive import of depth 5 is supported.
- `/memory` - to check the files loaded into memory.
- No sensitive information should be included.
- `CLAUDE.local.md` for local settings(team member individual preferences for example)
- Search goes from CWD all the way to Root. This way, we can have multiple CLAUDE.md in projects that follow monorepo

Example

```
````markdown
# Project Context

When working with this codebase, prioritize readability over cleverness. Ask clarifying questions before making architectural changes.

## About This Project

FastAPI REST API for user authentication and profiles. Uses SQLAlchemy for database operations and Pydantic for validation.

## Key Directories

- `app/models/` - database models
- `app/api/` - route handlers
- `app/core/` - configuration and utilities

## Standards

- Type hints required on all functions
- pytest for testing (fixtures in `tests/conftest.py`)
- PEP 8 with 100 character lines

## Common Commands
```bash
uvicorn app.main:app --reload  # dev server
pytest tests/ -v               # run tests

## Notes

All routes use `/api/v1` prefix. JWT tokens expire after 24 hours.
```

- `/init` creates this file. It can also be used on projects with existing `CLAUDE.md` to capture missing points.

Some topics to cover in this file

- Important commands
- Test instructions
- Key directories, module structures, major dependencies
- Code conventions and style guidelines
- Project specific details
- MCP Tools that it should be aware of and instructions to use it.

## Rules

Modular rules with `.claude/rules`. [Rules support YAML frontmatter](https://code.claude.com/docs/en/memory#path-specific-rules). Rules support symlinks. User level rules go into `~/.claude/rules`

```
.claude/rules/
├── frontend/
│   ├── react.md
│   └── styles.md
├── backend/
│   ├── api.md
│   └── database.md
└── general.md
```

Define a standard workflow for different usecases like features, UI change, testing requirements

Techniques to improve how claude code works

- Keep the context fresh. Context bloating impacts the performance.
- Long conversations accumulate context. Implementation and code review are two tasks that can use distinct subagents. Subagents maintain their own context. Subagents work best for multistep workflows where each phase requires different perspectives.
- Create custom slash commands. Saves time from prompting the same thing.

---

## Output styles

- Output styles are like stored system prompts
- Output styles directly affect the main agent loop and only affect the system prompt.

Output styles allow you to use Claude Code as any type of agent while keeping its core capabilities, such as running local scripts, reading/writing files, and tracking TODOs.

Builtin ones are as follows mainly targeting software engineering tasks

- Default - To complete software engineering tasks efficiently.
- Explanatory - Helps you understand implementation choices and codebase patterns
- Learning - Collaborative. Useful when we are learning some framework or language.

- `/output-style <style>` applied to local settings. We can also change this, at user or project level `settings.json`

We can write our own custom output style and store it under `.claude/output-styles`

```---
name: My Custom Style
description:
  A brief description of what this style does, to be displayed to the user
keep-coding-instructions: false
---

# Custom Style Instructions

You are an interactive CLI tool that helps users with software engineering
tasks. [Your custom instructions here...]

## Specific Behaviors

[Define how the assistant should behave in this style...]
```

## Custom Slash Commands

These go into `.claude/commands`. These are markdown files. The file names become the command name.

- Commands can have subdirectories `.claude/commands/frontend/component.md`. This is invoked as `/frontend:component`
- Passing arguments to commands using `$ARGUMENTS` placeholder or we can also use `$1`, `$2` placeholders

```
echo 'Find and fix issue #$ARGUMENTS. Follow these steps: 1.
Understand the issue described in the ticket 2. Locate the relevant code in
our codebase 3. Implement a solution that addresses the root cause 4. Add
appropriate tests 5. Prepare a concise PR description' >
.claude/commands/fix-issue.md
```

- Instead of tool calling for bash command, we can prefix the command with `!`, so that claude code executes the command in the same shell(speed up). The output of the command is added to the prompt and sent to the model.

Example

```markdown
## Context

Current spec: !`cat spec/.current-spec 2>/dev/null || echo "No active spec"` Spec directory contents: !`ls -la spec/$(cat spec/.current-spec 2>/dev/null)/ 2>/dev/null || echo "Spec not found"`
```

## Built in Subagents

Subagents cannot spawn other subagents

- Explore - Haiku. Code exploration. Read only tools
- Plan - Inherits the model from the main conversation. Read only tools
- General purpose - All tools, model inherited. Code modifications, complex reasoning

We can build [custom subagents](https://code.claude.com/docs/en/sub-agents#quickstart:-create-your-first-subagent) with our own prompts, tool restrictions, permissions, modes, hooks and skills.

Custom Subagents are defined in Markdown files with YAML frontmatter under `.claude/agents`

Subagents markdown example

```
---
name: code-reviewer
description: Reviews code for quality and best practices
tools: Read, Glob, Grep, Bash
disallowedTools: Write, Edit
model: sonnet
permissionMode: default/acceptEdits/dontAsk/bypassPermissions/Plan
skills: 
hooks: 
 PreToolUse:
     - matcher: "Bash"
       hooks:
         - type: command
           command: "./scripts/validate-readonly-query.sh"

 PostToolUse:
  - matcher: "Edit|Write"
    hooks:
   - type: command
     command: "./scripts/run-linter.sh"
---

You are a code reviewer. When invoked, analyze the code and provide
specific, actionable feedback on quality, security, and best practices.
```

NOTE: **Subagents receive only this system prompt (plus basic environment details like working directory), not the full Claude Code system prompt.**

NOTE: Subagents don't inherit skills from the parent conversation.

NOTE: Claude Code [passes hook input as JSON](https://code.claude.com/docs/en/hooks#pretooluse-input) via stdin to hook commands

Subagents via CLI as JSON

```
claude --agents '{
  "code-reviewer": {
    "description": "Expert code reviewer. Use proactively after code changes.",
    "prompt": "You are a senior code reviewer. Focus on code quality, security, and best practices.",
    "tools": ["Read", "Grep", "Glob", "Bash"],
    "model": "sonnet"
  }
}'
```

## [Skills](https://agentskills.io/specification)

- Skills helps agent accomplish complex task.
- [Skill best practices](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices)
- [Skill-ref](https://github.com/agentskills/agentskills/tree/main/skills-ref) is a python package for validating skill markdown files.
- [Injecting into context using skillref](https://agentskills.io/integrate-skills#injecting-into-context)For filesystem-based agents, include the `location` field with the absolute path to the SKILL.md file. For tool-based agents, the location can be omitted.
- Supports [YAML frontmatter](https://code.claude.com/docs/en/skills#frontmatter-reference)

| Field                      | Required    | Description                                                                                                                                                          |
| -------------------------- | ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `name`                     | No          | Display name for the skill. If omitted, uses the directory name. Lowercase letters, numbers, and hyphens only (max 64 characters).                                   |
| `description`              | Recommended | What the skill does and when to use it. Claude uses this to decide when to apply the skill. If omitted, uses the first paragraph of markdown content.                |
| `argument-hint`            | No          | Hint shown during autocomplete to indicate expected arguments. Example: `[issue-number]` or `[filename] [format]`.                                                   |
| `disable-model-invocation` | No          | Set to `true` to prevent Claude from automatically loading this skill. Use for workflows you want to trigger manually with `/name`. Default: `false`.                |
| `user-invocable`           | No          | Set to `false` to hide from the `/` menu. Use for background knowledge users shouldn’t invoke directly. Default: `true`.                                             |
| `allowed-tools`            | No          | Tools Claude can use without asking permission when this skill is active.                                                                                            |
| `model`                    | No          | Model to use when this skill is active.                                                                                                                              |
| `context`                  | No          | Set to `fork` to run in a forked subagent context.                                                                                                                   |
| `agent`                    | No          | Which subagent type to use when `context: fork` is set.                                                                                                              |
| `hooks`                    | No          | Hooks scoped to this skill’s lifecycle. See [Hooks in skills and agents](https://code.claude.com/docs/en/hooks#hooks-in-skills-and-agents) for configuration format. |

- Supports arguments substitution using `$N`, `$ARGUMENTS`, `$ARGUMENTS[N]` - zero indexed

---

## Tools

Knowing the tools, we can add these to settings.json or to skills as `allowed-skills` as well as building subagents.

Built-in tools (first-class)

- **Read** – Read file contents
- **Write** – Create/overwrite files
- **Edit** – Single-replacement edits on files
- **MultiEdit** – Batch edits on files
- **Grep** – Content search (ripgrep under the hood)
- **Glob** – File pattern matching
- **LS** – List directory contents
- **WebFetch** – Fetch a URL
- **WebSearch** – Web search
- **TodoRead / TodoWrite** – Task list management
- **NotebookRead / NotebookEdit** – Jupyter notebook ops
- **Skill** – Invoke other skills

`Bash` supports glob-style scoping so you can whitelist specific commands only. The syntax is `Bash(<command>:*)` or more granularly `Bash(<command> <subcommand>:*)`.

---

## Hooks

- We can write scripts as hooks and can be used in subagents for example

---

### MCP

TODO

---

## [Plugins](https://code.claude.com/docs/en/discover-plugins)

We have a variety of plugins

- LSP plugins for code intelligence.
- External integrations like Azure, Github
- Output styles from others
- Development workflows containing commands and agents

Plugins can be installed at project, user and local scope.

Incase of custom slash commands from the plugins, after installing, the plugin’s commands are immediately available. Plugin commands are namespaced by the plugin name, so **commit-commands** provides commands like `/commit-commands:commit`

NOTE: Marketplace can be a github repo. Add a GitHub repository that contains a `.claude-plugin/marketplace.json` file using the `owner/repo` format—where `owner` is the GitHub username or organization and `repo` is the repository name.

Local path is also possible. We just have to have `.claude-plugin/marketplace.json`

```bash
# To add a custom plugin market place
/plugin marketplace add anthropics/claude-code
/plugin marketplace list
/plugin marketplace remove marketplace-name
/plugin marketplace remove marketplace-name


# To install from the official marketplace.
/plugin install plugin-name@marketplace-name
# Example
/plugin install plugin-name@claude-plugins-official

/plugin disable plugin-name@marketplace-name

/plugin enable plugin-name@marketplace-name

/plugin uninstall plugin-name@marketplace-name
```

To specify scope, we can use these commands

```bash
claude plugin install formatter@your-org --scope project
claude plugin uninstall formatter@your-org --scope project
```

---

## [Claude Code Features and Workflows](https://code.claude.com/docs/en/common-workflows)

- TODO

---

## References

- [Claude Code docs](https://code.claude.com/docs/)
- [Claude Code 101](https://x.com/eyad_khrais/status/2010076957938188661?s=20)
