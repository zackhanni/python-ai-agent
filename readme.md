# Python AI Agent

This project implements an AI-powered research assistant using OpenAI's GPT-4 model and various tools.

## Features

- Uses OpenAI's GPT-4 model for natural language processing
- Integrates with external tools like Wikipedia and DuckDuckGo for information retrieval
- Saves research outputs to a text file
- Provides a structured response format using Pydantic models

## Usage

To run the agent:

1. Install required dependencies:

2. Set up environment variables (e.g., API keys) using a `.env` file

3. Run the main script: python ./main.py

4. Interact with the agent by typing queries when prompted

## Tools

The agent utilizes several tools:

- **Save Tool**: Saves structured research data to a text file
- **Search Tool**: Performs web searches using DuckDuckGo
- **Wiki Tool**: Retrieves information from Wikipedia API

These tools are implemented in the `tools.py` file.

## Configuration

The agent uses a configuration file (`main.py`) that sets up:

- The language model (currently GPT-4 mini)
- Prompt templates for guiding the AI's responses
- Tool integration

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

[Insert license information here]

## Acknowledgments

- OpenAI for providing the GPT-4 model
- LangChain library for AI agent framework
- Wikipedia API and DuckDuckGo for data retrieval tools
