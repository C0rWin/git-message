import os
import openai
import sys
import argparse


def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(
        description='Generate commit messages from git diffs using OpenAI models.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        '--model', '-m',
        default='gpt-4o-mini',
        help='OpenAI model to use for generating commit messages'
    )
    args = parser.parse_args()

    try:
        client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        if client.api_key is None:
            raise ValueError("OPENAI_API_KEY environmental variable is not set")

        response = client.chat.completions.create(
                model=args.model,
                messages=[
                    {"role": "system", "content": "You are a helpful assistant that analyzes git diffs and generates commit messages."},
                    {"role": "user", "content": "Here is the git diff:\n" + sys.stdin.read()},
                ]
                )
        print(response.choices[0].message.content)
    
    except ValueError as ve:
        print(f"Error: {ve}", file=sys.stderr)
        sys.exit(1)
    except openai.APIError as e:
        print(f"OpenAI API Error: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Unexpected error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
