"""
Test that UI templates and assets follow the Kearney design specs.
"""
import os
from pathlib import Path


def get_project_root():
    return Path(__file__).parent.parent


def test_kearney_logo_exists():
    """Ensure the official Kearney logo SVG file exists."""
    project_root = get_project_root()
    logo_path = project_root / "app" / "static" / "kearney-logo.svg"

    assert logo_path.exists(), f"Kearney logo not found at {logo_path}"

    # Verify it's an actual SVG, not just text
    content = logo_path.read_text()
    assert "<svg" in content, "Logo file is not a valid SVG"
    assert "viewBox" in content, "Logo SVG missing viewBox attribute"


def test_templates_use_logo():
    """Ensure all templates reference the logo image, not font-based logos."""
    project_root = get_project_root()
    templates_dir = project_root / "app" / "templates"

    for template in templates_dir.glob("*.html"):
        content = template.read_text()

        # Check that the template includes the logo image
        assert "kearney-logo.svg" in content, f"{template.name} does not reference kearney-logo.svg"


def test_css_uses_kearney_colors():
    """Ensure CSS uses the official Kearney color palette."""
    project_root = get_project_root()
    css_path = project_root / "app" / "static" / "style.css"

    content = css_path.read_text()

    # Check for Kearney primary colors
    assert "#7823DC" in content or "#7823dc" in content.lower(), "Missing Kearney purple (#7823DC)"
    assert "#1E1E1E" in content or "#1e1e1e" in content.lower(), "Missing Kearney black (#1E1E1E)"
    assert "#E0D2FA" in content or "#e0d2fa" in content.lower(), "Missing Kearney accent (#E0D2FA)"


def test_css_uses_inter_font():
    """Ensure CSS uses the Inter font as specified in design."""
    project_root = get_project_root()
    css_path = project_root / "app" / "static" / "style.css"

    content = css_path.read_text()

    # Check for Inter font import
    assert "Inter" in content, "CSS does not reference Inter font"


def test_templates_have_consistent_header():
    """Ensure all templates have the new header structure."""
    project_root = get_project_root()
    templates_dir = project_root / "app" / "templates"

    for template in templates_dir.glob("*.html"):
        content = template.read_text()

        # Check for new header class
        assert "site-header" in content, f"{template.name} missing site-header class"

        # Check for header navigation
        assert "header-nav" in content, f"{template.name} missing header-nav"


def test_templates_have_consistent_footer():
    """Ensure all templates have the new footer structure."""
    project_root = get_project_root()
    templates_dir = project_root / "app" / "templates"

    for template in templates_dir.glob("*.html"):
        content = template.read_text()

        # Check for new footer class
        assert "site-footer" in content, f"{template.name} missing site-footer class"

        # Check for copyright text
        assert "Kearney" in content and "All rights reserved" in content, \
            f"{template.name} missing copyright text"


def test_no_text_based_logos():
    """Ensure templates don't use font-styled text as logos."""
    project_root = get_project_root()
    templates_dir = project_root / "app" / "templates"

    for template in templates_dir.glob("*.html"):
        content = template.read_text()

        # Check that we're not just using <h1>Kearney</h1> or similar as the logo
        # The header h1 should be for the site title, not the logo itself
        # Look for patterns that would indicate a text-based logo
        if "class=\"logo\"" in content or "class='logo'" in content:
            # If there's a logo class, make sure it's on an img tag
            assert '<img' in content and 'logo' in content, \
                f"{template.name} appears to have a text-based logo instead of an image"
