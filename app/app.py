"""
Kearney AI Skills Library - Flask Application
A web interface for browsing and copying AI prompts and skills.
"""

import json
import os
from flask import Flask, render_template

app = Flask(__name__)

# Get the base directory (parent of app folder)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_items():
    """
    Load prompts and skills from the JSON data store and enrich with file content.

    Returns:
        list: List of item dictionaries with full content loaded.
    """
    items_json_path = os.path.join(os.path.dirname(__file__), 'prompts.json')

    with open(items_json_path, 'r', encoding='utf-8') as f:
        items = json.load(f)

    # Load the actual content for each item
    for item in items:
        item_type = item.get('Type', 'prompt')

        if item_type == 'skill':
            # Load skill content from folder
            skill_folder = os.path.join(BASE_DIR, item.get('SkillFolder', ''))
            platforms = item.get('Platforms', [])
            item['SkillVersions'] = {}

            for platform in platforms:
                skill_file = os.path.join(skill_folder, f'SKILL_{platform}.md')
                try:
                    with open(skill_file, 'r', encoding='utf-8') as f:
                        item['SkillVersions'][platform] = f.read()
                except FileNotFoundError:
                    item['SkillVersions'][platform] = f"[Error: Skill file not found at {skill_file}]"
                except Exception as e:
                    item['SkillVersions'][platform] = f"[Error loading skill: {str(e)}]"

            # Set primary content to first available platform
            if platforms and item['SkillVersions']:
                item['PromptContent'] = item['SkillVersions'].get(platforms[0], '')
        else:
            # Load prompt content from file
            content_file_path = os.path.join(BASE_DIR, item.get('PromptContentFile', ''))
            try:
                with open(content_file_path, 'r', encoding='utf-8') as f:
                    item['PromptContent'] = f.read()
            except FileNotFoundError:
                item['PromptContent'] = f"[Error: Content file not found at {item.get('PromptContentFile', '')}]"
            except Exception as e:
                item['PromptContent'] = f"[Error loading content: {str(e)}]"

    return items


# Keep backwards compatibility
def load_prompts():
    """Alias for load_items() for backwards compatibility."""
    return load_items()


@app.route('/')
def index():
    """Render the main page with all prompts and skills."""
    items = load_items()
    return render_template('index.html', prompts=items)


@app.route('/prompt/<int:prompt_id>')
def prompt_detail(prompt_id):
    """Render a detail page for a single prompt or skill."""
    items = load_items()
    item = next((p for p in items if p['id'] == prompt_id), None)
    if item is None:
        return "Item not found", 404
    return render_template('detail.html', prompt=item)


@app.route('/guide')
def guide():
    """Render the how-to-use guide page."""
    return render_template('guide.html')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
