# Git Message Generator

Generate meaningful commit messages automatically from git diffs using OpenAI's language models.

## Overview

Git Message Generator is a command-line tool that analyzes your git diffs and generates descriptive commit messages using OpenAI's language models. It helps developers create more meaningful and consistent commit messages with minimal effort.

## Features

- Generate commit messages automatically from git diffs
- Support for multiple OpenAI models (GPT-4, GPT-3.5, etc.)
- Easy integration with git workflow
- Command-line interface with helpful options
- List available OpenAI models

## Installation

### Prerequisites

- Python 3.7 or higher
- OpenAI API key

### Install using pip

```bash
pip install git-message
```

## Configuration

1. Set your OpenAI API key as an environment variable:

```bash
# Linux/macOS
export OPENAI_API_KEY='your-api-key'

# Windows (CMD)
set OPENAI_API_KEY=your-api-key

# Windows (PowerShell)
$env:OPENAI_API_KEY='your-api-key'
```

2. (Optional) Add it to your shell profile for persistence:

```bash
# Add to ~/.bashrc, ~/.zshrc, etc.
export OPENAI_API_KEY='your-api-key'
```

## Usage

### Basic Usage

Generate a commit message for your current changes:

```bash
git diff | git-message
```

### Using with Staged Changes

Generate a message for staged changes:

```bash
git diff --staged | git-message
```

### Specify a Different Model

```bash
git diff | git-message --model gpt-4
# or
git diff | git-message -m gpt-4
```

### List Available Models

```bash
git-message --list-models
# or
git-message -l
```

### Git Alias Setup (Optional)

Add this to your git config to create a shortcut:

```bash
git config --global alias.generate-msg '!git diff --staged | git-message'
```

Then use:

```bash
git generate-msg
```

## Command-Line Options

```
--model, -m     Specify the OpenAI model to use (default: gpt-4o-mini)
--list-models, -l   List all available OpenAI models
--help, -h      Show help message
```

## Examples

### Example 1: Basic Commit Message Generation

```bash
$ git diff | git-message
feat: Add user authentication middleware with JWT support
```

### Example 2: Using a Different Model

```bash
$ git diff | git-message --model gpt-4
fix: Resolve race condition in database connection pool
```

### Example 3: Complete Git Workflow

```bash
# Stage your changes
git add .

# Generate commit message
git diff --staged | git-message > commit-msg.txt

# Review and edit if needed
vim commit-msg.txt

# Commit with the generated message
git commit -F commit-msg.txt
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Development Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/git-message.git
cd git-message

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install in editable mode
pip install -e .
```

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- OpenAI for providing the API
- The Python community for the excellent tools and libraries

## Support

If you encounter any problems or have suggestions, please file an issue on the [GitHub issue tracker](https://github.com/yourusername/git-message/issues).