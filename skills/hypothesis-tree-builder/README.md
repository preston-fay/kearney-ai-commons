# Hypothesis Tree Builder

The #1 most valuable consulting skill. Transforms fuzzy business questions into structured, testable hypothesis trees.

## What It Does

Takes a business question like "Should we enter the European market?" and produces:

1. **Primary Hypothesis** - A clear, testable claim
2. **MECE Sub-Hypotheses** - 2-4 branches covering all angles
3. **Test Criteria** - Specific ways to validate each branch
4. **Data Requirements** - What evidence you need
5. **Kill Criteria** - What would disprove each hypothesis
6. **Validation Roadmap** - Prioritized testing sequence

## Why It Matters

- **Raises thinking quality** - Forces rigor before analysis
- **Reduces wasted work** - Tests critical assumptions early
- **Creates alignment** - Shared structure for team and client
- **Enables iteration** - Easy to update as evidence emerges

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
4. Get your hypothesis tree

### Claude Code (Slash Command)
1. Save `SKILL_claude-code.md` as `~/.claude/skills/hypothesis-tree-builder/SKILL.md`
2. Run `/hypothesis-tree-builder` in any project
3. Optionally pass the question directly: `/hypothesis-tree-builder "Should we acquire CompanyX?"`

## Interview Questions

1. **Business Question** - What are you trying to answer?
2. **Context** - Client, industry, constraints
3. **Initial Belief** - Your current hypothesis or intuition
4. **Decision Impact** - What decision does this inform?
5. **Depth** - Quick (10 min), Standard (20 min), or Deep (30+ min)

## Sample Output

```
PRIMARY HYPOTHESIS (H0)
───────────────────────
We believe that acquiring CompanyX will generate $50M+ NPV because
it provides market access we can't build organically.

H0: Acquisition creates $50M+ NPV
│
├── H1: Revenue synergies exceed $30M annually
│   ├── H1.1: Cross-sell to CompanyX customers viable
│   │   • Test: Customer overlap analysis, purchase intent survey
│   │   • Data: Customer lists, wallet share data
│   │   • Kill: <10% overlap, low intent scores
│   └── H1.2: Combined sales force increases win rate
│       • Test: Historical win rate comparison
│       • Data: CRM data, competitive intelligence
│       • Kill: No coverage gaps identified
│
├── H2: Cost synergies exceed $15M annually
│   └── ...
│
└── H3: Integration risks are manageable
    └── ...
```

## Best Practices

1. **Start with the decision** - "What would make you say yes vs. no?"
2. **Be specific** - Vague hypotheses can't be tested
3. **Define kill criteria** - Know what disproves you
4. **Prioritize quick wins** - Test cheapest/fastest hypotheses first
5. **Iterate** - Update the tree as evidence emerges

## Pairs Well With

- **Issue Tree Decomposer** - For problem structuring before hypothesis building
- **Workplan Generator** - To operationalize the validation roadmap
- **Data Request Builder** - To formalize data gathering needs

## Author

Kearney AI Skills Library

## License

Internal Kearney Use Only
