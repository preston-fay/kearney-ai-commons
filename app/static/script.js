/**
 * Kearney AI Commons - Client-Side JavaScript
 * Handles clipboard operations and UI interactions.
 */

/**
 * Copy the text content of an element to the clipboard.
 * @param {string} elementId - The ID of the element containing text to copy.
 * @param {HTMLElement} button - The button element that was clicked.
 */
function copyToClipboard(elementId, button) {
    const element = document.getElementById(elementId);
    if (!element) {
        console.error('Element not found:', elementId);
        return;
    }

    const text = element.textContent;

    // Use the modern Clipboard API if available
    if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text)
            .then(() => {
                showCopySuccess(button);
            })
            .catch(err => {
                console.error('Clipboard API failed:', err);
                fallbackCopyToClipboard(text, button);
            });
    } else {
        // Fallback for older browsers
        fallbackCopyToClipboard(text, button);
    }
}

/**
 * Fallback copy method using a temporary textarea element.
 * @param {string} text - The text to copy.
 * @param {HTMLElement} button - The button element for feedback.
 */
function fallbackCopyToClipboard(text, button) {
    const textarea = document.createElement('textarea');
    textarea.value = text;
    textarea.style.position = 'fixed';
    textarea.style.left = '-9999px';
    textarea.style.top = '-9999px';
    document.body.appendChild(textarea);
    textarea.focus();
    textarea.select();

    try {
        const successful = document.execCommand('copy');
        if (successful) {
            showCopySuccess(button);
        } else {
            showCopyError(button);
        }
    } catch (err) {
        console.error('Fallback copy failed:', err);
        showCopyError(button);
    }

    document.body.removeChild(textarea);
}

/**
 * Show success feedback on the copy button.
 * @param {HTMLElement} button - The button element.
 */
function showCopySuccess(button) {
    const originalText = button.innerHTML;
    button.innerHTML = '<span class="copy-icon">&#10003;</span> Copied!';
    button.classList.add('copy-success');

    setTimeout(() => {
        button.innerHTML = originalText;
        button.classList.remove('copy-success');
    }, 2000);
}

/**
 * Show error feedback on the copy button.
 * @param {HTMLElement} button - The button element.
 */
function showCopyError(button) {
    const originalText = button.innerHTML;
    button.innerHTML = '<span class="copy-icon">&#10007;</span> Failed';
    button.classList.add('copy-error');

    setTimeout(() => {
        button.innerHTML = originalText;
        button.classList.remove('copy-error');
    }, 2000);
}

/**
 * Initialize any page-level event listeners.
 */
document.addEventListener('DOMContentLoaded', function() {
    // Add keyboard shortcut (Ctrl/Cmd + C on focused code blocks)
    document.querySelectorAll('.prompt-content-wrapper').forEach(wrapper => {
        wrapper.addEventListener('keydown', function(e) {
            if ((e.ctrlKey || e.metaKey) && e.key === 'c' && window.getSelection().toString() === '') {
                // If Ctrl+C pressed with no text selected, copy the whole block
                const codeBlock = wrapper.querySelector('code');
                const button = wrapper.querySelector('.copy-btn');
                if (codeBlock && button) {
                    copyToClipboard(codeBlock.id, button);
                }
            }
        });
    });
});
