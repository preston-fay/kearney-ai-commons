# Kearney AI Skills Library

A curated library of validated AI prompts and interactive skills for Kearney enterprise workflows.

## Overview

The AI Skills Library provides:

- **Prompts**: Static, copy-paste prompt templates for common tasks
- **Skills**: Interactive AI workflows (interviews, generators, analyzers)
- **Web Interface**: Browse and copy content via a clean Flask-based UI
- **Validation Suite**: Test prompts against Anthropic and OpenAI APIs

## Project Structure

```
kearney-ai-skills-library/
├── app/
│   ├── static/
│   │   ├── script.js      # Clipboard functionality
│   │   └── style.css      # Kearney-branded styling
│   ├── templates/
│   │   ├── index.html     # Main library view
│   │   └── detail.html    # Individual item view
│   ├── app.py             # Flask application
│   └── prompts.json       # Local prompt/skill database
├── prompts/
│   └── *.txt              # Static prompt content files
├── skills/
│   └── */                 # Interactive skill folders
│       ├── README.md      # Skill documentation
│       ├── SKILL_*.md     # Platform-specific versions
│       └── ...
├── scripts/
│   └── validate_prompts.py # Validation suite
├── .env.example           # Environment template
├── .gitignore
├── requirements.txt
└── README.md
```

## Quick Start

### 1. Set Up Environment

```bash
# Clone the repository
git clone https://github.com/preston-fay/kearney-ai-skills-library.git
cd kearney-ai-skills-library

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Configure API Keys (Optional - for validation)

```bash
# Copy the example environment file
cp .env.example .env

# Edit .env and add your API keys
# ANTHROPIC_API_KEY="sk-ant-..."
# OPENAI_API_KEY="sk-..."
```

### 3. Run the Web Server

```bash
# From the app directory
cd app
flask run

# Or run directly
python app.py
```

The application will be available at **http://localhost:5000**

Production deployment: **http://3.142.207.252** (pending DNS: aiskills.kearney.com)

### 4. Run the Validation Suite

```bash
# Full validation (requires API keys)
python scripts/validate_prompts.py

# Dry run (no API calls, for testing)
python scripts/validate_prompts.py --dry-run

# Custom output file
python scripts/validate_prompts.py --output my_report.csv
```

## Content Types

### Prompts

Static prompt templates users copy into their LLM of choice.

**Adding a new prompt:**
1. Create a `.txt` file in `/prompts`
2. Add metadata to `app/prompts.json`

```json
{
  "id": 2,
  "Title": "My New Prompt",
  "Type": "prompt",
  "PromptContentFile": "prompts/MyNewPrompt_v1.txt",
  "UseCase": "Analysis",
  "TargetAudience": "Consultant",
  "Version": 1.0,
  "Status": "Draft"
}
```

### Skills

Interactive AI workflows with multiple platform versions.

**Adding a new skill:**
1. Create a folder in `/skills/your-skill-name/`
2. Add `README.md` documenting the skill
3. Add platform-specific versions:
   - `SKILL_claude-code.md` - For Claude Code CLI
   - `SKILL_generic.md` - For any LLM
4. Register in `app/prompts.json`

```json
{
  "id": 3,
  "Title": "My New Skill",
  "Type": "skill",
  "SkillFolder": "skills/my-new-skill",
  "Platforms": ["claude-code", "generic"],
  "UseCase": "Workflow Automation",
  "TargetAudience": "Developer",
  "Version": 1.0,
  "Status": "Draft"
}
```

## Validation Tests

The validation suite runs 5 standardized tests against each prompt:

| Test | Description |
|------|-------------|
| T1 - Basic Understanding | Verifies AI comprehends the prompt's purpose |
| T2 - Instruction Clarity | Identifies ambiguous or confusing instructions |
| T3 - Completeness Check | Finds missing information or context |
| T4 - Use Case Alignment | Generates sample output for typical use |
| T5 - Edge Case Handling | Identifies potential failure modes |

## Architecture Decisions

### Local-First Approach

This implementation prioritizes rapid iteration over enterprise deployment. By removing SharePoint dependencies, we can:

- Develop and test prompts faster
- Iterate without deployment friction
- Validate prompts against multiple AI providers
- Build confidence before production rollout

### Content Categories

- **Prompts** (`/prompts/*.txt`): Static, copy-paste content
- **Skills** (`/skills/*/`): Interactive, multi-step workflows
- **Metadata** (`prompts.json`): Cataloging and organization
- **Presentation** (`/app`): User interface layer
- **Validation** (`/scripts`): Testing and quality assurance

### Platform Support

Skills can target specific platforms or be generic:

| Platform | File Pattern | Description |
|----------|--------------|-------------|
| Claude Code | `SKILL_claude-code.md` | Uses Claude Code CLI features |
| Generic | `SKILL_generic.md` | Works with any LLM |
| ChatGPT | `SKILL_chatgpt.md` | ChatGPT-specific optimizations |
| Copilot | `SKILL_copilot.md` | GitHub Copilot optimizations |

## API Requirements

| Provider | Model | Purpose |
|----------|-------|---------|
| Anthropic | claude-sonnet-4-20250514 | Primary validation |
| OpenAI | gpt-4o | Cross-provider validation |

## Contributing

1. Create prompts in `/prompts` or skills in `/skills`
2. Register them in `prompts.json`
3. Run validation to ensure quality
4. Submit for review

## Current Library

### Prompts
- **Kearney Design System v2** - Visual generation with KDS compliance

### Skills
- **Setup Workflow** - Interactive interview to generate AI workflow instructions

## Next Steps

- [ ] Add user authentication
- [ ] Implement versioning for prompts and skills
- [ ] Add search/filter functionality
- [ ] Build governance workflow
- [ ] Add more skills (code review, documentation, analysis)

## License

Internal Kearney Use Only

---

*Kearney AI Skills Library*
