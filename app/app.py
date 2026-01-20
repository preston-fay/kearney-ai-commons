"""
Kearney AI Commons - Local Flask Application
A web interface for browsing and copying AI prompts from the commons library.
"""

import json
import os
from flask import Flask, render_template

app = Flask(__name__)

# Get the base directory (parent of app folder)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_prompts():
    """
    Load prompts from the JSON data store and enrich with file content.

    Returns:
        list: List of prompt dictionaries with full content loaded.
    """
    prompts_json_path = os.path.join(os.path.dirname(__file__), 'prompts.json')

    with open(prompts_json_path, 'r', encoding='utf-8') as f:
        prompts = json.load(f)

    # Load the actual content for each prompt
    for prompt in prompts:
        content_file_path = os.path.join(BASE_DIR, prompt['PromptContentFile'])
        try:
            with open(content_file_path, 'r', encoding='utf-8') as f:
                prompt['PromptContent'] = f.read()
        except FileNotFoundError:
            prompt['PromptContent'] = f"[Error: Content file not found at {prompt['PromptContentFile']}]"
        except Exception as e:
            prompt['PromptContent'] = f"[Error loading content: {str(e)}]"

    return prompts


@app.route('/')
def index():
    """Render the main page with all prompts."""
    prompts = load_prompts()
    return render_template('index.html', prompts=prompts)


@app.route('/prompt/<int:prompt_id>')
def prompt_detail(prompt_id):
    """Render a detail page for a single prompt."""
    prompts = load_prompts()
    prompt = next((p for p in prompts if p['id'] == prompt_id), None)
    if prompt is None:
        return "Prompt not found", 404
    return render_template('detail.html', prompt=prompt)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
