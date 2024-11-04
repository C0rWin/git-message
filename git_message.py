import os
import openai
import sys
import argparse


def list_models(client):
    try:
        models = client.models.list()
        print("Available models:")
        for model in models:
            print(f"- {model.id}")
    except Exception as e:
        print(f"Error fetching models: {e}", file=sys.stderr)
        sys.exit(1)

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
    parser.add_argument(
        '--list-models', '-l',
        action='store_true',
        help='List all available OpenAI models'
    )
    args = parser.parse_args()

    try:
        client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
        if client.api_key is None:
            raise ValueError("OPENAI_API_KEY environmental variable is not set")

        if args.list_models:
            list_models(client)
            sys.exit(0)

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
