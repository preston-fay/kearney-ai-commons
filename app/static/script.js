/**
 * Kearney AI Skills Library - Client-Side JavaScript
 * Handles clipboard operations, filtering, tabs, and UI interactions.
 */

// Current filter state
let currentFilter = 'all';

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
 * Set the current filter and update the display.
 * @param {string} filter - The filter type ('all', 'prompt', or 'skill').
 * @param {HTMLElement} button - The button that was clicked.
 */
function setFilter(filter, button) {
    currentFilter = filter;

    // Update button states
    document.querySelectorAll('.filter-btn').forEach(btn => {
        btn.classList.remove('active');
    });
    button.classList.add('active');

    // Apply filter
    filterItems();
}

/**
 * Filter items based on search input and current filter.
 */
function filterItems() {
    const searchInput = document.getElementById('search-input');
    const searchTerm = searchInput ? searchInput.value.toLowerCase() : '';
    const items = document.querySelectorAll('.prompt-card');
    const noResults = document.getElementById('no-results');
    let visibleCount = 0;

    items.forEach(item => {
        const type = item.dataset.type || 'prompt';
        const title = item.dataset.title || '';
        const usecase = item.dataset.usecase || '';

        // Check filter
        const matchesFilter = currentFilter === 'all' || type === currentFilter;

        // Check search
        const matchesSearch = searchTerm === '' ||
            title.includes(searchTerm) ||
            usecase.includes(searchTerm);

        // Show or hide
        if (matchesFilter && matchesSearch) {
            item.style.display = 'block';
            visibleCount++;
        } else {
            item.style.display = 'none';
        }
    });

    // Show/hide no results message
    if (noResults) {
        noResults.style.display = visibleCount === 0 ? 'block' : 'none';
    }
}

/**
 * Switch between platform tabs on skill detail pages.
 * @param {string} platform - The platform to switch to.
 * @param {HTMLElement} button - The tab button that was clicked.
 */
function switchTab(platform, button) {
    // Update button states
    document.querySelectorAll('.tab-btn').forEach(btn => {
        btn.classList.remove('active');
    });
    button.classList.add('active');

    // Show the correct content
    document.querySelectorAll('.tab-content').forEach(content => {
        content.classList.remove('active');
    });
    const targetTab = document.getElementById('tab-' + platform);
    if (targetTab) {
        targetTab.classList.add('active');
    }
}

/**
 * Toggle FAQ accordion items.
 * @param {HTMLElement} button - The FAQ question button that was clicked.
 */
function toggleFaq(button) {
    const answer = button.nextElementSibling;
    const isOpen = button.classList.contains('open');

    // Close all other FAQs
    document.querySelectorAll('.faq-question').forEach(q => {
        q.classList.remove('open');
        q.nextElementSibling.classList.remove('open');
    });

    // Toggle this one
    if (!isOpen) {
        button.classList.add('open');
        answer.classList.add('open');
    }
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

    // Add enter key support for search
    const searchInput = document.getElementById('search-input');
    if (searchInput) {
        searchInput.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                e.preventDefault();
                filterItems();
            }
        });
    }
});
