# Kearney AI Commons - Local Development Environment

A self-contained, local-first implementation of the Kearney AI Commons prompt library. This project enables rapid iteration, validation, and testing of enterprise AI prompts without external dependencies.

## Overview

The AI Commons is a curated library of validated AI prompts designed for Kearney enterprise workflows. This local implementation provides:

- **Web Interface**: Browse and copy prompts via a clean Flask-based UI
- **Validation Suite**: Test prompts against Anthropic and OpenAI APIs
- **Rapid Iteration**: Develop and refine prompts locally before deployment

## Project Structure

```
kearney-ai-commons-local/
├── app/
│   ├── static/
│   │   ├── script.js      # Clipboard functionality
│   │   └── style.css      # Kearney-branded styling
│   ├── templates/
│   │   ├── index.html     # Main library view
│   │   └── detail.html    # Individual prompt view
│   ├── app.py             # Flask application
│   └── prompts.json       # Local prompt database
├── prompts/
│   └── *.txt              # Prompt content files
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
# Navigate to project directory
cd kearney-ai-commons-local

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

### 4. Run the Validation Suite

```bash
# Full validation (requires API keys)
python scripts/validate_prompts.py

# Dry run (no API calls, for testing)
python scripts/validate_prompts.py --dry-run

# Custom output file
python scripts/validate_prompts.py --output my_report.csv
```

## Adding New Prompts

1. **Create the prompt file**: Add a `.txt` file to the `/prompts` directory
   ```
   prompts/MyNewPrompt_v1.txt
   ```

2. **Register in the database**: Add an entry to `app/prompts.json`
   ```json
   {
     "id": 2,
     "Title": "My New Prompt",
     "PromptContentFile": "prompts/MyNewPrompt_v1.txt",
     "UseCase": "Analysis",
     "TargetAudience": "Consultant",
     "Version": 1.0,
     "Status": "Draft"
   }
   ```

3. **Validate**: Run the validation suite to test against AI providers

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

### Data Store

The `prompts.json` file serves as a lightweight local database. For production, this would migrate to SharePoint Lists or a proper database.

### Separation of Concerns

- **Content files** (`/prompts/*.txt`): The actual prompt text
- **Metadata** (`prompts.json`): Cataloging and organization
- **Presentation** (`/app`): User interface layer
- **Validation** (`/scripts`): Testing and quality assurance

## API Requirements

| Provider | Model | Purpose |
|----------|-------|---------|
| Anthropic | claude-sonnet-4-20250514 | Primary validation |
| OpenAI | gpt-4o | Cross-provider validation |

## Contributing

1. Create prompts in the `/prompts` directory
2. Register them in `prompts.json`
3. Run validation to ensure quality
4. Submit for review

## Next Steps

- [ ] Add user authentication
- [ ] Implement prompt versioning
- [ ] Add search/filter functionality
- [ ] Build governance workflow
- [ ] Migrate to SharePoint for production

## License

Internal Kearney Use Only

---

*Built for the Kearney AI Commons Initiative*
