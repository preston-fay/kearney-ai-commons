#!/usr/bin/env python3
"""
Kearney AI Commons - Prompt Validation Suite

This script validates prompts by running standardized test queries against
both Anthropic and OpenAI APIs, generating a comprehensive validation report.
"""

import os
import sys
import csv
import json
import glob
from datetime import datetime
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv(Path(__file__).parent.parent / '.env')


# Configuration
ANTHROPIC_API_KEY = os.getenv('ANTHROPIC_API_KEY')
OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
PROMPTS_DIR = Path(__file__).parent.parent / 'prompts'
OUTPUT_DIR = Path(__file__).parent.parent / 'scripts'

# Standard Test Queries for Validation
TEST_QUERIES = [
    {
        'id': 'T1',
        'name': 'Basic Understanding',
        'query': 'Summarize the main purpose and key capabilities described in this prompt.',
        'evaluation_criteria': 'Response should accurately capture the core intent'
    },
    {
        'id': 'T2',
        'name': 'Instruction Clarity',
        'query': 'Are the instructions in this prompt clear and unambiguous? Identify any areas of confusion.',
        'evaluation_criteria': 'Response should identify clarity issues if present'
    },
    {
        'id': 'T3',
        'name': 'Completeness Check',
        'query': 'What essential information or context might be missing from this prompt?',
        'evaluation_criteria': 'Response should note gaps or confirm completeness'
    },
    {
        'id': 'T4',
        'name': 'Use Case Alignment',
        'query': 'Generate a sample output following these prompt instructions for a typical use case.',
        'evaluation_criteria': 'Response should demonstrate practical application'
    },
    {
        'id': 'T5',
        'name': 'Edge Case Handling',
        'query': 'What edge cases or unusual inputs might cause issues with this prompt?',
        'evaluation_criteria': 'Response should identify potential failure modes'
    }
]


def check_api_keys():
    """Verify that API keys are configured."""
    missing_keys = []
    if not ANTHROPIC_API_KEY or ANTHROPIC_API_KEY == 'your-key-here':
        missing_keys.append('ANTHROPIC_API_KEY')
    if not OPENAI_API_KEY or OPENAI_API_KEY == 'your-key-here':
        missing_keys.append('OPENAI_API_KEY')

    return missing_keys


def load_prompt_files():
    """Load all .txt files from the prompts directory."""
    prompt_files = []
    for filepath in PROMPTS_DIR.glob('*.txt'):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        prompt_files.append({
            'filename': filepath.name,
            'filepath': str(filepath),
            'content': content,
            'size_bytes': len(content.encode('utf-8')),
            'line_count': len(content.splitlines())
        })
    return prompt_files


def call_anthropic_api(system_prompt: str, user_query: str) -> dict:
    """
    Call Anthropic's Claude API with the given prompt and query.

    Returns a dict with 'response', 'tokens_used', 'latency_ms', and 'error' fields.
    """
    try:
        import anthropic

        client = anthropic.Anthropic(api_key=ANTHROPIC_API_KEY)

        start_time = datetime.now()
        message = client.messages.create(
            model="claude-sonnet-4-20250514",
            max_tokens=1024,
            system=system_prompt,
            messages=[
                {"role": "user", "content": user_query}
            ]
        )
        latency_ms = (datetime.now() - start_time).total_seconds() * 1000

        return {
            'response': message.content[0].text,
            'tokens_used': message.usage.input_tokens + message.usage.output_tokens,
            'latency_ms': round(latency_ms, 2),
            'error': None
        }
    except ImportError:
        return {
            'response': None,
            'tokens_used': 0,
            'latency_ms': 0,
            'error': 'anthropic package not installed'
        }
    except Exception as e:
        return {
            'response': None,
            'tokens_used': 0,
            'latency_ms': 0,
            'error': str(e)
        }


def call_openai_api(system_prompt: str, user_query: str) -> dict:
    """
    Call OpenAI's GPT API with the given prompt and query.

    Returns a dict with 'response', 'tokens_used', 'latency_ms', and 'error' fields.
    """
    try:
        from openai import OpenAI

        client = OpenAI(api_key=OPENAI_API_KEY)

        start_time = datetime.now()
        response = client.chat.completions.create(
            model="gpt-4o",
            max_tokens=1024,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_query}
            ]
        )
        latency_ms = (datetime.now() - start_time).total_seconds() * 1000

        return {
            'response': response.choices[0].message.content,
            'tokens_used': response.usage.total_tokens if response.usage else 0,
            'latency_ms': round(latency_ms, 2),
            'error': None
        }
    except ImportError:
        return {
            'response': None,
            'tokens_used': 0,
            'latency_ms': 0,
            'error': 'openai package not installed'
        }
    except Exception as e:
        return {
            'response': None,
            'tokens_used': 0,
            'latency_ms': 0,
            'error': str(e)
        }


def run_validation(prompt_files: list, dry_run: bool = False) -> list:
    """
    Run validation tests on all prompt files.

    Args:
        prompt_files: List of prompt file dictionaries
        dry_run: If True, skip actual API calls

    Returns:
        List of validation results
    """
    results = []

    for prompt in prompt_files:
        print(f"\n{'='*60}")
        print(f"Validating: {prompt['filename']}")
        print(f"  Lines: {prompt['line_count']}, Size: {prompt['size_bytes']} bytes")
        print(f"{'='*60}")

        for test in TEST_QUERIES:
            print(f"\n  Running Test {test['id']}: {test['name']}...")

            result = {
                'timestamp': datetime.now().isoformat(),
                'prompt_file': prompt['filename'],
                'test_id': test['id'],
                'test_name': test['name'],
                'test_query': test['query'],
                'evaluation_criteria': test['evaluation_criteria']
            }

            if dry_run:
                # Simulate results for dry run
                result.update({
                    'anthropic_response': '[DRY RUN - No API call made]',
                    'anthropic_tokens': 0,
                    'anthropic_latency_ms': 0,
                    'anthropic_error': None,
                    'openai_response': '[DRY RUN - No API call made]',
                    'openai_tokens': 0,
                    'openai_latency_ms': 0,
                    'openai_error': None,
                    'status': 'DRY_RUN'
                })
            else:
                # Call Anthropic API
                anthropic_result = call_anthropic_api(prompt['content'], test['query'])
                result.update({
                    'anthropic_response': anthropic_result['response'][:500] if anthropic_result['response'] else None,
                    'anthropic_tokens': anthropic_result['tokens_used'],
                    'anthropic_latency_ms': anthropic_result['latency_ms'],
                    'anthropic_error': anthropic_result['error']
                })

                # Call OpenAI API
                openai_result = call_openai_api(prompt['content'], test['query'])
                result.update({
                    'openai_response': openai_result['response'][:500] if openai_result['response'] else None,
                    'openai_tokens': openai_result['tokens_used'],
                    'openai_latency_ms': openai_result['latency_ms'],
                    'openai_error': openai_result['error']
                })

                # Determine overall status
                if anthropic_result['error'] and openai_result['error']:
                    result['status'] = 'BOTH_FAILED'
                elif anthropic_result['error']:
                    result['status'] = 'ANTHROPIC_FAILED'
                elif openai_result['error']:
                    result['status'] = 'OPENAI_FAILED'
                else:
                    result['status'] = 'SUCCESS'

            results.append(result)
            print(f"    Status: {result['status']}")

    return results


def generate_report(results: list, output_path: Path):
    """Generate a CSV validation report."""
    if not results:
        print("No results to report.")
        return

    fieldnames = [
        'timestamp', 'prompt_file', 'test_id', 'test_name', 'test_query',
        'evaluation_criteria', 'status',
        'anthropic_response', 'anthropic_tokens', 'anthropic_latency_ms', 'anthropic_error',
        'openai_response', 'openai_tokens', 'openai_latency_ms', 'openai_error'
    ]

    with open(output_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)

    print(f"\n{'='*60}")
    print(f"Validation report generated: {output_path}")
    print(f"Total tests run: {len(results)}")

    # Summary statistics
    statuses = [r['status'] for r in results]
    print(f"\nSummary:")
    print(f"  SUCCESS: {statuses.count('SUCCESS')}")
    print(f"  DRY_RUN: {statuses.count('DRY_RUN')}")
    print(f"  ANTHROPIC_FAILED: {statuses.count('ANTHROPIC_FAILED')}")
    print(f"  OPENAI_FAILED: {statuses.count('OPENAI_FAILED')}")
    print(f"  BOTH_FAILED: {statuses.count('BOTH_FAILED')}")
    print(f"{'='*60}")


def main():
    """Main entry point for the validation script."""
    import argparse

    parser = argparse.ArgumentParser(
        description='Validate AI prompts against Anthropic and OpenAI APIs'
    )
    parser.add_argument(
        '--dry-run',
        action='store_true',
        help='Run without making actual API calls'
    )
    parser.add_argument(
        '--output',
        type=str,
        default='validation_report.csv',
        help='Output filename for the validation report'
    )

    args = parser.parse_args()

    print("=" * 60)
    print("Kearney AI Commons - Prompt Validation Suite")
    print("=" * 60)
    print(f"Timestamp: {datetime.now().isoformat()}")
    print(f"Prompts Directory: {PROMPTS_DIR}")
    print(f"Dry Run Mode: {args.dry_run}")

    # Check API keys
    if not args.dry_run:
        missing_keys = check_api_keys()
        if missing_keys:
            print(f"\n⚠️  Warning: Missing API keys: {', '.join(missing_keys)}")
            print("   Set these in your .env file or run with --dry-run")
            print("   Continuing with available APIs...\n")

    # Load prompts
    prompt_files = load_prompt_files()
    if not prompt_files:
        print(f"\n❌ No .txt files found in {PROMPTS_DIR}")
        sys.exit(1)

    print(f"\nFound {len(prompt_files)} prompt file(s):")
    for p in prompt_files:
        print(f"  - {p['filename']} ({p['line_count']} lines)")

    # Run validation
    results = run_validation(prompt_files, dry_run=args.dry_run)

    # Generate report
    output_path = OUTPUT_DIR / args.output
    generate_report(results, output_path)

    print("\n✅ Validation complete!")


if __name__ == '__main__':
    main()
