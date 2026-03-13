# CC Best Practices

## [Getting the most out of Claude Code][1]

### 0. Think

- The first thing is to think about the problem. Come up with exactly what you want to build by chatting back and forth. Explore various options available while designing the system.

> The more information that you have in plan mode, the better your output is actually going to be because the better the input is going to be.

> You click shift + tab twice, and you’re in plan mode. Trust me when I say this, this is going to take 5 minutes of your time, but will save you hours upon hours of debugging later on.

### 1. Claude.md

- This is a markdown file. Keep it short as Claude Code can only follow ~200 instructions at a time, Claude code system prompt already uses 50 of those.
- Make the content specific to the project that Claude doesn't know.
- Tell it why, not just what. For example, "Use TypeScript strict mode because we've had production bugs from implicit any types".
- If you are correcting Claude multiple times on something, add it to the `Claude.md`. Update it constantly. **Press the # key while you're working and Claude will add instructions to your `Claude.md` automatically**

### 2. Context Window Limitations

- Opus 4.5 has 200K context window, but quality starts to deteriorate starting halfway through.
- `/compact` slash command to get the summary of the context.
- Scope your conversations - One conversation per feature, per task, per bug fix etc
- Make Claude write plans to say `plan.md` and then progress to the code. This way we store the context externally and Claude can resume back by reading the plan.
- When context gets bloated, copy everything important from the terminal, run `/compact` to get a summary, then `/clear` the context entirely, and paste back in only what matters. Fresh context with the critical information preserved.
- If the conversation is not going anywhere, `/clear` and start fresh.

>The mental model that works: Claude is stateless. Every conversation starts from nothing except what you explicitly give it. Plan accordingly.

### 3. Prompting

- Get better at prompting(conveying clearly what needs to be done)
- Be specific about what should be done or what's needed.
- Explicitly state what to do and what NOT to do.
- Add context on why something needs to be done certain way.

> Something that you have to remember is that AI is designed to speed us up and not completely replace us, especially in the era of very professional software engineering. Claude still makes mistakes.

- Use Opus for thinking, complex reasoning, its slower, but also its more expensive. Use Sonnet for straight forward tasks, its faster and cheaper.

> A workflow that works: use Opus to plan and make architectural decisions, then switch to Sonnet (Shift+Tab in Claude Code) for implementation.

### 4. Claude Code Features

- MCP servers - Access Browser, File system, databases, Github etc. Create your own MCP server, if there isn''t one for your use case.
- Hooks - run some code automatically before and after Claude makes/made the changes
- Custom Slash commands - Custom slash commands are just prompts you use repeatedly, packaged as commands. Create a `.claude/commands` folder, add markdown files with your prompts, and now you can run them with `/command`. If you're running the same kind of task often - debugging, reviewing, deploying - make it a command.
- Settings.json configurations
- Skills
- Plugins

### 5. Getting Stuck

- Complex problems can make Claude to get stuck. When this happens, start off simple by `/clear`
- Simplify the task further.
- If we can write a minimal example, do it to make it understand better.
- Reframing - Try different ways to convey what you want

> The meta-skill here is recognizing when you're in a loop early. If you've explained the same thing three times and Claude still isn't getting it, more explaining won't help. Change something.

### 6. Build Systems

- Claude code has `-p` for headless mode. No interactive interface. This means you can script it. Pipe output to other tools. Chain it with bash commands. Integrate it into automated workflows.

- The flywheel: Claude makes a mistake, you review the logs, you improve the `CLAUDE.md` or tooling, Claude gets better next time. This compounds.

- Think how you can formulate the problems that can make Claude work without our intervention

## [Claude Code mastery][2]

- Add common gatekeeper rules(do and don'ts) to the user level CLAUDE.md
- Maintain the CLAUDE.md global configuration in a remote Git repository to share across multiple machines.
- Prefer CLI tools than MCP servers if available.

## Useful Git Repos

Useful Github repositories with Claude code configuration.

- [Claude Code showcase](https://github.com/ChrisWiles/claude-code-showcase)
- [Claude Bootstrap Repo](https://github.com/ntanner-ctrl/claude-bootstrap)
- [Claude personal configuration](https://github.com/ZacheryGlass/.claude)
- [Claude code tips](https://github.com/ykdojo/claude-code-tips)
- [Claude code mastery](https://github.com/TheDecipherist/claude-code-mastery/tree/main)
- [Spec driven development](https://github.com/papaoloba/spec-based-claude-code/)

---

## References

- [Claude code mastery article][2]
- [Learn Claude Code][1]

[1]: https://ccforeveryone.com/
[2]:https://thedecipherist.com/articles/claude-code-guide-v4
