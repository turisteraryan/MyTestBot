import os
import time
import subprocess

# Define bot paths
telegram_bot_path = './telegram-bot/telegram_bot.py'
discord_bot_path = './discord-bot/discord_bot.py'

def run_bot(bot_path):
    while True:
        print(f"Starting bot: {bot_path}")
        process = subprocess.Popen(['python', bot_path])
        process.wait()  # Wait for the bot to finish
        print(f"Bot {bot_path} crashed or stopped. Restarting...")
        time.sleep(5)  # Small delay before restarting

if __name__ == "__main__":
    # Start both bots in separate threads
    import threading
    telegram_thread = threading.Thread(target=run_bot, args=(telegram_bot_path,))
    discord_thread = threading.Thread(target=run_bot, args=(discord_bot_path,))
    
    telegram_thread.start()
    discord_thread.start()

    # Restart every 6 hours
    while True:
        time.sleep(21600)  # 6 hours in seconds
        print("Restarting all bots...")
        os.system('pkill -f telegram_bot.py')  # Kill Telegram bot
        os.system('pkill -f discord_bot.py')   # Kill Discord bot
      
