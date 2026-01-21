# Issue Tree Decomposer

The essential companion to Hypothesis Tree Builder. Decomposes complex, fuzzy problems into clean MECE structures that guide analysis.

## What It Does

Takes a problem like "Why is our profitability declining?" and produces:

1. **Sharpened Root Problem** - Clear, bounded, actionable framing
2. **MECE Branch Structure** - 3-4 levels of logical decomposition
3. **MECE Validation** - Explicit check for overlap and gaps
4. **Analysis Mapping** - What analysis addresses each branch
5. **Prioritization Guide** - Where to start

## Why It Matters

- **Eliminates confusion** - Everyone works from the same structure
- **Prevents scope creep** - Clear boundaries on what's in/out
- **Guides workplan** - Each branch maps to specific analysis
- **Ensures completeness** - MECE check catches gaps early

## When to Use

| Situation | Use Issue Tree |
|-----------|----------------|
| Starting a new case | ✓ First step |
| Problem is fuzzy | ✓ To sharpen it |
| Team misaligned | ✓ To create shared structure |
| Analysis feels random | ✓ To organize it |
| Before hypothesis building | ✓ Structure first, then hypothesize |

## Versions

| Version | File | Platform |
|---------|------|----------|
| Claude Code | `SKILL_claude-code.md` | Claude Code CLI |
| Generic | `SKILL_generic.md` | Any LLM (ChatGPT, Claude.ai, Gemini, etc.) |

## Usage

### Any LLM (Copy-Paste)
1. Copy contents of `SKILL_generic.md`
2. Paste into ChatGPT, Claude.ai, or any AI
3. Answer the 5 interview questions
4. Get your MECE issue tree

### Claude Code (Slash Command)
1. Save `SKILL_claude-code.md` as `~/.claude/skills/issue-tree-decomposer/SKILL.md`
2. Run `/issue-tree-decomposer` in any project
3. Optionally pass the problem directly: `/issue-tree-decomposer "Why is margin declining?"`

## Interview Questions

1. **The Problem** - What are you trying to solve?
2. **Scope Boundaries** - What's in/out of scope?
3. **Stakeholder Lens** - CEO, CFO, COO, or functional?
4. **Known Factors** - What do you already know?
5. **Depth** - Quick (2 levels), Standard (3), or Deep (4)?

## Common Patterns

### Profitability
```
Why is profitability declining?
├── Revenue issues
│   ├── Volume decline
│   └── Price/mix erosion
├── Cost issues
│   ├── Variable (COGS)
│   └── Fixed (SG&A)
└── Asset efficiency
```

### Growth
```
How do we grow revenue?
├── Existing customers
├── New customers
├── New products
└── New geographies
```

### Operations
```
Why is performance declining?
├── People
├── Process
├── Technology
└── External factors
```

## MECE Quality Check

**Mutually Exclusive:**
- Can any issue fit in multiple branches? If yes → fix it
- Test: "Where does [specific issue] go?" Should have ONE answer

**Collectively Exhaustive:**
- Is there a scenario not covered? If yes → add a branch
- Test: "What if the answer isn't in any branch?" Should be impossible

## Pairs Well With

- **Hypothesis Tree Builder** - After structuring, build hypotheses for each branch
- **Workplan Generator** - Convert branches to project tasks
- **Data Request Builder** - Formalize data needs per branch

## Author

Kearney AI Skills Library

## License

Internal Kearney Use Only
