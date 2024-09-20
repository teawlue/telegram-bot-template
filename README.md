# Telegram Bot Template

This is a clean template for creating a Telegram bot using Python and the `python-telegram-bot` library. The bot includes logging and is structured for scalability and maintainability.

## Features

- **Environment Variables**: Uses a `.env` file to securely manage API tokens.
- **Logging**: Configured logging for easier debugging and monitoring.
- **Modular Structure**: Clean project structure separating handlers, utilities, and main application logic.
- **Ready for Expansion**: Set up to easily add new features and handlers.

## Getting Started

### Prerequisites

- Python 3.7 or higher
- A Telegram bot token from [BotFather](https://t.me/BotFather)

### Installation

1. **Clone the repository**

   ```
   git clone https://github.com/teawlue/telegram-bot-template.git
   cd telegram-bot-template
   ```

2. **Create a virtual environment (optional but recommended)**

   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use: venv\Scripts\activate
   ```

3. **Install the dependencies**

   ```
   pip install -r requirements.txt
   ```

4. **Set up the `.env` file**

   Create a `.env` file in the root directory:

   ```
   TELEGRAM_API_TOKEN=your_telegram_bot_token_here
   ```

   Replace `your_telegram_bot_token_here` with your actual Telegram bot token.

### Running the Bot

Run the bot using the following command:

```
python bot.py
```

You should see:

```
INFO:__main__:Bot is running...
```

## Project Structure

```
telegram-bot-template/
├── bot.py
├── .env
├── .gitignore
├── handlers/
│   ├── __init__.py
├── utils/
│   ├── __init__.py
│   ├── helpers.py
├── requirements.txt
└── README.md
```

- `bot.py`: The main application file that runs the bot.
- `.env`: Contains environment variables (not committed to version control).
- `.gitignore`: Specifies files and directories to be ignored by Git.
- `handlers/`: Contains command and message handlers.
- `utils/`: Contains utility functions and configurations.
- `requirements.txt`: Lists the project's dependencies.
- `README.md`: Project documentation.

## Extending the Bot

1. **Add a new command handler**

   - Create a new file in `handlers/`, e.g., `start.py`.
   - Define the command handler and a `register_handlers` function.
   - Import and call the new `register_handlers` function in `handlers/__init__.py`.

   ```
   # handlers/start.py

   from telegram import Update
   from telegram.ext import ContextTypes, CommandHandler

   async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
       await update.message.reply_text("Hello! This is a template bot.")

   def register_handlers(application):
       application.add_handler(CommandHandler('start', start))
   ```

   Update `handlers/__init__.py`:

   ```
   # handlers/__init__.py

   from .start import register_handlers as register_start_handlers

   def register_handlers(application):
       register_start_handlers(application)
   ```

2. **Use helper functions**

   - Add utility functions in `utils/helpers.py`.
   - Import them where needed.

3. **Manage configurations**

   - Add new environment variables in the `.env` file.
   - Load them using the `load_config()` function in `utils/helpers.py`.

## Logging

- The logging configuration is set to `INFO` level by default.
- To see more detailed logs, change the level to `DEBUG` in `utils/__init__.py`.

  ```
  # utils/__init__.py

  import logging

  logging.basicConfig(
      format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
      level=logging.DEBUG
  )

  logger = logging.getLogger(__name__)
  ```

## Contributing

Feel free to submit issues and pull requests for new features, improvements, and bug fixes.

## License

This project is open-source and available under the [MIT License](LICENSE).

