# Git Commit Message Generator

This project contains a script, `git_message.py`, that utilizes OpenAI's API to generate commit messages from git diffs. The script is designed to assist developers in writing meaningful commit messages, using AI to analyze the changes in code.

## Requirements

- Python 3
- An OpenAI API key

## Setup

1. Install the OpenAI Python client library:

   ```shell
   pip install openai
   ```

2. Set the `OPENAI_API_KEY` environment variable with your OpenAI API key:

   ```shell
   export OPENAI_API_KEY='your-api-key-here'
   ```

## Usage

The script reads a git diff from standard input and outputs a suggested commit message. You can use it in combination with git commands.

Example usage:

```shell
git diff HEAD~1 | python git_message.py
```

This command will take the diff of the last commit and pass it to the script, which will then print a suggested commit message.

## Note

Ensure that the `OPENAI_API_KEY` is set in your environment to authenticate requests to the OpenAI API.

## License

[MIT License](LICENSE)
