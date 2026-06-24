# NOVA AI Assistant

NOVA is a command-line AI assistant built using Python, LangChain, and Groq. It provides a simple conversational interface that allows users to interact with a large language model directly from the terminal.

## Features

* Interactive terminal-based chatbot
* Powered by Groq language models
* Configurable system prompt
* Environment variable support using `.env`
* Clean and extensible codebase

## Requirements

* Python 3.12+
* Groq API Key

## Installation

### Clone the Repository

```bash
git clone https://github.com/adityaraj-devx/Python-Practice-Projects.git
cd Python-Practice-Projects
cd "NOVA AI-assistant"
```

### Install Dependencies

```bash
uv sync
```

### Configure Environment Variables

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_api_key_here
```

## Usage

Run the application:

```bash
python main.py
```

Example:

```text
Welcome! I'm NOVA, your AI assistant. Type 'quit' to exit

You: What is Python?

Assistant: Python is a high-level, general-purpose programming language...
```

To exit:

```text
quit
```

## Project Structure

```text
.
├── main.py
├── pyproject.toml
├── uv.lock
├── .env.example
├── .gitignore
└── README.md
```

## Technologies Used

* Python
* LangChain
* Groq
* python-dotenv



## License

This project is licensed under the MIT License.
