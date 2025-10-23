# GEMINI on TELEGRAM

A Telegram bot powered by Google's Gemini AI that provides intelligent conversational responses.

## Overview

This project integrates Google's Gemini 2.5 Flash model with Telegram to create an interactive chatbot. The bot uses Gemini AI to respond to user queries and echoes all text messages with their details.

## Features

- **Gemini AI Chat**: Use `/gemini <your message>` to get intelligent responses from Google's Gemini AI
- **Text Echo**: Automatically responds to all text messages with the message ID and content

## Prerequisites

- Python 3.7+
- Telegram Bot Token (from [@BotFather](https://t.me/botfather))
- Google Gemini API Key (from [Google AI Studio](https://makersuite.google.com/app/apikey))

## Installation

### Option 1: Docker (Recommended)

1. Clone the repository:
```bash
git clone https://github.com/tarsislimadev/gemini_on_telegram.git
cd gemini_on_telegram
```

2. Create a `.env` file from the example:
```bash
cp .env.example .env
```

3. Edit `.env` and add your API keys:
```
GOOGLE_API_KEY=your_google_api_key_here
TELEGRAM_API_KEY=your_telegram_bot_token_here
```

4. Run with Docker Compose:
```bash
docker-compose up -d
```

5. View logs:
```bash
docker-compose logs -f
```

6. Stop the bot:
```bash
docker-compose down
```

### Option 2: Local Python

1. Clone the repository:
```bash
git clone https://github.com/tarsislimadev/gemini_on_telegram.git
cd gemini_on_telegram
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file or set environment variables:
```bash
export GOOGLE_API_KEY=your_google_api_key_here
export TELEGRAM_API_KEY=your_telegram_bot_token_here
```

4. Run the bot:
```bash
python app.py
```

## Usage

### Available Commands

- `/gemini <your question or message>` - Chat with Google's Gemini AI model

### Examples

```
/gemini What is the capital of France?
/gemini Explain quantum computing in simple terms
/gemini Write a haiku about coding
```

All text messages (including commands) will receive an automatic echo response showing the message ID and content.

## Technology Stack

- **[python-telegram-bot](https://docs.python-telegram-bot.org/en/stable/index.html)**: Telegram Bot API wrapper
- **Google Generative AI**: Gemini 2.5 Flash model for AI responses
- **requests**: HTTP library for making HTTP requests

## How It Works

The bot uses Google's Gemini 2.5 Flash model to generate intelligent responses to your questions. When you send a message with the `/gemini` command, it creates a chat session with the AI model and returns the generated response. All messages are also echoed back with their metadata for transparency.

## Development

### Project Structure

```
gemini-telegram/
├── app.py              # Main bot application
├── requirements.txt    # Python dependencies
├── pyproject.toml      # Project metadata and build configuration
├── Dockerfile          # Docker image definition
├── docker-compose.yml  # Docker Compose configuration
└── README.md          # This file
```

### Setting Up Development Environment

1. Clone the repository:
```bash
git clone https://github.com/tarsislimadev/gemini-telegram.git
cd gemini-telegram
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
```bash
export GOOGLE_API_KEY=your_google_api_key_here
export TELEGRAM_API_KEY=your_telegram_bot_token_here
```

5. Run the bot:
```bash
python app.py
```

### Code Structure

The bot consists of:

- **`gemini()` handler**: Processes `/gemini` commands and interacts with Google's Gemini AI
- **`text()` handler**: Echoes all text messages with their metadata
- **Application setup**: Configures the Telegram bot with handlers and starts polling

### Dependencies

- `python-telegram-bot`: Framework for building Telegram bots
- `google-generativeai`: Official Google Gemini API client
- `requests`: HTTP library for API calls

### Environment Variables

| Variable | Description | Required |
|----------|-------------|----------|
| `GOOGLE_API_KEY` | API key from Google AI Studio | Yes |
| `TELEGRAM_API_KEY` | Bot token from @BotFather | Yes |

### Building with Docker

Build the Docker image:
```bash
docker build -t gemini-telegram .
```

Run the container:
```bash
docker run -d \
  -e GOOGLE_API_KEY=your_key \
  -e TELEGRAM_API_KEY=your_token \
  gemini-telegram
```

### Testing

To test the bot locally:

1. Start the bot using one of the installation methods above
2. Open Telegram and find your bot
3. Send `/gemini Hello!` to test the Gemini integration
4. Send any text message to test the echo functionality

## Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Make your changes
4. Commit your changes (`git commit -m 'Add amazing feature'`)
5. Push to the branch (`git push origin feature/amazing-feature`)
6. Open a Pull Request

## License

This project is open source and available for educational purposes.
