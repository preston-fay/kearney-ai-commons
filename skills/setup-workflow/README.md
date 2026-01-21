# Setup Workflow Skill

An interactive interview skill that generates customized AI workflow instructions for any project.

## What It Does

This skill conducts a brief interview (7 questions) about your project and working preferences, then generates a tailored instructions file that governs how AI assistants work with you on:

- **Change approval** - When to ask permission vs. proceed autonomously
- **Testing** - TDD enforcement, test requirements, verification
- **Task management** - When to use task lists for tracking
- **Git commits** - Manual, suggested, or AI-assisted
- **Quality standards** - Universal rules for reliable output

## Versions

| Version | File | Platform | Description |
|---------|------|----------|-------------|
| Claude Code | `SKILL_claude-code.md` | Claude Code CLI | Uses Claude Code-specific features (TodoWrite, CLAUDE.md convention) |
| Generic | `SKILL_generic.md` | Any LLM | Works with ChatGPT, Claude, Gemini, Copilot, etc. |

## Usage

### Claude Code

1. Install as a slash command in `~/.claude/skills/setup-workflow/SKILL.md`
2. Run `/setup-workflow` in any project directory
3. Answer the interview questions
4. A `CLAUDE.md` file is created in your project

### Other LLMs

1. Copy the contents of `SKILL_generic.md`
2. Paste into your preferred LLM (ChatGPT, Claude.ai, Gemini, etc.)
3. Answer the interview questions
4. Save the output as `AI_INSTRUCTIONS.md` in your project
5. Reference it in future conversations

## Interview Questions

1. **Project type** - Web app, CLI, API, library, etc.
2. **Current state** - New or existing? Size?
3. **Testing situation** - TDD, tests exist, or minimal
4. **Change approval** - Cautious, balanced, or autonomous
5. **Task complexity** - Simple, medium, or complex
6. **Commit preferences** - Manual, suggested, or assisted
7. **Verification style** - Automatic, guided, or report only

## Sample Output

```markdown
# MyProject - AI Instructions

## Project Context
A medium-sized React web application with an existing test suite.

## Before Making Changes
- Simple fixes: proceed directly, report after
- New features or multi-file changes: outline approach first, get approval
- Architectural changes: always discuss first

## Testing
- Run existing tests after changes
- Add tests for new functionality
- Don't over-engineer test coverage for trivial changes

## Task Management
- For small fixes: proceed directly
- For features touching 3+ files: create a task list
- Mark tasks complete as you finish them

## Git & Commits
- After completing a logical unit of work, prepare a commit
- Show the proposed commit message and changed files
- Wait for approval before executing

## Quality Standards
- Never use placeholder values in delivered code
- Never claim something works without evidence
- If something fails, acknowledge immediately
- Keep solutions simple
```

## Author

Preston Fay, Kearney

## License

Internal Kearney Use Only
