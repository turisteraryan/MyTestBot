#!/bin/bash

# Check if the bot is running, and if not, restart it
if ! pgrep -f telegram_bot.py > /dev/null; then
    echo "Bot is not running. Restarting..."
    python ./telegram-bot/telegram_bot.py &  # Start the bot in the background
else
    echo "Bot is running."
fi

