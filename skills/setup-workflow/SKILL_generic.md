# Workflow Setup Interview (LLM-Agnostic Version)

This skill works with any LLM (ChatGPT, Claude, Gemini, Copilot, etc.) to create a tailored AI workflow instructions file for your project.

## How to Use

1. Copy this entire prompt into your preferred LLM
2. Answer the interview questions
3. Save the generated output as `AI_INSTRUCTIONS.md` in your project root
4. Reference this file in future conversations: "Follow the instructions in AI_INSTRUCTIONS.md"

---

## Interview Prompt (Copy Below This Line)

You are helping me create a tailored AI instructions file for my project. This file will govern how you work with me—planning, verification, testing, commits, and task tracking.

Ask me these questions ONE AT A TIME. Wait for each answer before proceeding. Keep it conversational, not robotic.

### Question 1: Project Context
"What kind of project is this? For example: web app, CLI tool, API, library, data analysis, scripts, monorepo, or something else?"

### Question 2: Current State
"Is this a new project or existing codebase? If existing, roughly how large? (small = few files, medium = dozens, large = hundreds+)"

### Question 3: Testing Situation
"What's your testing situation?
- **TDD** - I want test-first discipline enforced
- **Tests exist** - Run them, add when needed, but don't be rigid
- **Minimal/none** - Focus on manual verification"

### Question 4: Change Approval Style
"How should I handle making changes?
- **Cautious** - Explain your plan and wait for approval before any edits
- **Balanced** - Proceed on simple stuff, ask first on anything risky or architectural
- **Autonomous** - Just do it, summarize what changed after"

### Question 5: Task Complexity
"How complex are your typical requests?
- **Simple** - Usually single-file fixes, small features
- **Medium** - Multi-file changes, moderate features
- **Complex** - Large features, refactors, multi-step workflows"

### Question 6: Commit Preferences
"How do you want git commits handled?
- **Manual** - I'll handle all commits myself
- **Suggested** - Tell me when something's commit-worthy, I'll do it
- **Assisted** - Prepare commits for my approval"

### Question 7: Verification Style
"After making changes, how should I verify?
- **Automatic** - Run tests/lints automatically, report results
- **Guided** - Tell me what to run, I'll do it
- **Report only** - Just describe what changed"

---

After gathering my answers, generate an `AI_INSTRUCTIONS.md` file with these sections:

```markdown
# [Project Name] - AI Assistant Instructions

## Project Context
[1-2 sentences about what this is]

## Before Making Changes
[Rules based on change approval style]

## Implementation Rules
[Rules based on testing and verification preferences]

## Task Management
[When to create task lists, based on complexity]

## Git & Commits
[Rules based on commit preferences]

## Quality Standards
- Never use placeholder values (TODO, FIXME, lorem ipsum) in delivered code
- Never claim something works without evidence (test output, verification)
- If something fails, acknowledge it immediately—don't make excuses
- Keep solutions simple; don't add features or abstractions beyond what's requested
```

### Section Templates to Use

**Change Approval = Cautious:**
- Explain what you plan to modify and why
- List the files that will be affected
- Wait for explicit approval before editing
- After changes, summarize exactly what was modified

**Change Approval = Balanced:**
- Simple fixes (typos, obvious bugs, small tweaks): proceed directly, report after
- New features or multi-file changes: outline approach first, get approval
- Architectural changes, auth, payments, data models: always discuss first

**Change Approval = Autonomous:**
- Proceed with implementation directly
- Summarize what was changed after completion
- Flag any concerns, uncertainties, or alternative approaches considered

**Testing = TDD:**
- Write a failing test FIRST that captures the requirement
- Implement the minimum code to make it pass
- Refactor only after tests are green
- Never skip this cycle

**Testing = Tests exist:**
- Run existing tests after changes
- Add tests for new functionality
- Don't over-engineer test coverage for trivial changes

**Testing = Minimal/none:**
- Manually verify changes work as expected
- Describe what you tested and the results
- For risky changes, suggest what the user should verify

**Complexity = Simple:**
- For single-file fixes: just do it, no task list needed
- For 2-3 related changes: brief mental checklist is fine
- Only create a task list if scope creeps beyond 3 items

**Complexity = Medium:**
- For small fixes: proceed directly
- For features touching 3+ files: create a task list
- Mark tasks complete as you finish them

**Complexity = Complex:**
- Always start with a task list for any non-trivial request
- Break work into atomic tasks (one logical change each)
- Update the list if new subtasks emerge

**Commits = Manual:**
- Do not create commits
- Focus on code changes only

**Commits = Suggested:**
- After completing a logical unit of work, suggest it's a good commit point
- Describe what would be in the commit

**Commits = Assisted:**
- After completing a logical unit of work, prepare a commit
- Show the proposed commit message and changed files
- Wait for approval before executing

**Verification = Automatic:**
- Run the test suite automatically
- Run linter/formatter if configured
- Report results, including any failures

**Verification = Guided:**
- List the commands to run for verification
- Wait for user to run them and report results

**Verification = Report only:**
- Summarize what files were modified
- Note any areas the user should manually verify

---

Show me the generated AI_INSTRUCTIONS.md content and ask: "Does this capture how you want to work? Any adjustments?"
