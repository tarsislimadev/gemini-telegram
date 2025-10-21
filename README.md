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
- **requests**: HTTP library for fetching AWS status

## How It Works

The bot uses Google's Gemini 2.5 Flash model to generate intelligent responses to your questions. When you send a message with the `/gemini` command, it creates a chat session with the AI model and returns the generated response. All messages are also echoed back with their metadata for transparency.

## Contributing

Feel free to open issues or submit pull requests for improvements.

## License

This project is open source and available for educational purposes.
