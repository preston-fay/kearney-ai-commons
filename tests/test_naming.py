"""
Test that all references to 'commons' have been renamed to 'skills'.
"""
import os
import re
from pathlib import Path


def get_project_root():
    return Path(__file__).parent.parent


def test_no_commons_references():
    """Ensure no files contain 'commons' in project name context."""
    project_root = get_project_root()

    # Files to check (excluding .git and tests)
    files_with_commons = []

    for root, dirs, files in os.walk(project_root):
        # Skip .git and tests directories
        dirs[:] = [d for d in dirs if d not in ['.git', '__pycache__', 'tests']]

        for filename in files:
            filepath = Path(root) / filename

            # Skip binary files
            if filepath.suffix in ['.pyc', '.png', '.jpg', '.ico', '.woff', '.woff2']:
                continue

            try:
                content = filepath.read_text()
                # Look for "commons" in naming context (case insensitive)
                if re.search(r'ai\s*commons|commons\s*team', content, re.IGNORECASE):
                    files_with_commons.append(str(filepath.relative_to(project_root)))
            except (UnicodeDecodeError, PermissionError):
                continue

    assert files_with_commons == [], f"Files still containing 'commons' references: {files_with_commons}"
