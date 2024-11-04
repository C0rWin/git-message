import os
import openai
import sys


def main():
    client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    if client.api_key is None:
        raise ValueError("OPENAI_API_KEY environmental variable is not set")

    response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that analyzes git diffs and generates commit messages."},
                {"role": "user", "content": "Here is the git diff:\n" + sys.stdin.read()},
            ]
            )
    print(response.choices[0].message.content)


if __name__ == "__main__":
    main()
