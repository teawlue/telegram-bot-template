# bot.py

from telegram.ext import ApplicationBuilder
from handlers import register_handlers
from utils import load_config, logger

def main():
    # Load configuration from .env
    config = load_config()

    # Create the bot application
    application = ApplicationBuilder().token(config['TELEGRAM_API_TOKEN']).build()

    # Register handlers (currently empty)
    register_handlers(application)

    # Run the bot
    logger.info("Bot is running...")
    application.run_polling()

if __name__ == '__main__':
    main()
