# Gemini on Telegram Bot

A lightweight Telegram bot powered by Google's Gemini 2.5 Flash AI model for intelligent conversational responses.

## Quick Start

```bash
docker run -d \
  --name gemini-telegram-bot \
  -e GOOGLE_API_KEY=your_google_api_key \
  -e TELEGRAM_API_KEY=your_telegram_bot_token \
  tmvdl/gemini-telegram
```

Or use Docker Compose:

```yaml
services:
  telegram-bot:
    image: tmvdl/gemini-telegram
    container_name: gemini-telegram-bot
    restart: unless-stopped
    environment:
      - GOOGLE_API_KEY=${GOOGLE_API_KEY}
      - TELEGRAM_API_KEY=${TELEGRAM_API_KEY}
```

## Required Environment Variables

| Variable | Description | How to Get |
|----------|-------------|------------|
| `GOOGLE_API_KEY` | Google Gemini API key | Get from [Google AI Studio](https://makersuite.google.com/app/apikey) |
| `TELEGRAM_API_KEY` | Telegram bot token | Get from [@BotFather](https://t.me/botfather) |

## Features

- **AI-Powered Conversations**: Chat with Google's Gemini 2.5 Flash model through Telegram
- **Simple Command Interface**: Use `/gemini <message>` to interact with the AI
- **Message Echo**: Automatic echo responses for transparency
- **Lightweight**: Built on Python 3.11-slim for minimal footprint
- **Auto-Restart**: Configured to restart unless explicitly stopped

## Usage

Once the bot is running and added to your Telegram:

1. Start a conversation with your bot
2. Use the `/gemini` command followed by your question or message:

```
/gemini What is the capital of France?
/gemini Explain quantum computing in simple terms
/gemini Write a haiku about coding
```

The bot will respond with AI-generated content from Google's Gemini model.

## Example Docker Compose Setup

1. Create a `docker-compose.yml`:

```yaml
services:
  telegram-bot:
    image: tmvdl/gemini-telegram
    container_name: gemini-telegram-bot
    restart: unless-stopped
    environment:
      - GOOGLE_API_KEY=${GOOGLE_API_KEY}
      - TELEGRAM_API_KEY=${TELEGRAM_API_KEY}
    networks:
      - bot-network

networks:
  bot-network:
    driver: bridge
```

2. Create a `.env` file with your credentials:

```
GOOGLE_API_KEY=your_google_api_key_here
TELEGRAM_API_KEY=your_telegram_bot_token_here
```

3. Start the bot:

```bash
docker-compose up -d
```

4. View logs:

```bash
docker-compose logs -f
```

## Technology Stack

- **Python 3.11**: Modern Python runtime
- **python-telegram-bot**: Official Telegram Bot API wrapper
- **google-generativeai**: Google's Gemini AI SDK
- **Docker**: Containerized for easy deployment

## Getting Your API Keys

### Telegram Bot Token

1. Open Telegram and search for [@BotFather](https://t.me/botfather)
2. Send `/newbot` and follow the instructions
3. Copy the API token provided

### Google Gemini API Key

1. Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
2. Sign in with your Google account
3. Create a new API key
4. Copy the key for use in your environment variables

## Container Details

- **Base Image**: `python:3.11-slim`
- **Working Directory**: `/app`
- **Exposed Ports**: None (bot uses polling)
- **Restart Policy**: `unless-stopped`

## Security Notes

- Never commit your API keys to version control
- Use environment variables or Docker secrets for credentials
- Regularly rotate your API keys
- Monitor your bot's usage to detect unauthorized access

## Troubleshooting

**Bot not responding:**
- Verify both API keys are correct
- Check container logs: `docker logs gemini-telegram-bot`
- Ensure your Telegram bot is not already running elsewhere

**Connection issues:**
- Verify internet connectivity
- Check if your firewall allows outbound connections
- Ensure Google AI API and Telegram API are accessible

## Source Code

GitHub: [tarsislimadev/gemini_on_telegram](https://github.com/tarsislimadev/gemini_on_telegram)

## Support

For issues, questions, or contributions, please visit the [GitHub repository](https://github.com/tarsislimadev/gemini_on_telegram) and open an issue.

## License

This project is open source and available for educational purposes.
