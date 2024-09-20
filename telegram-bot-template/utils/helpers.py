# utils/helpers.py

import os
from dotenv import load_dotenv

def load_config():
    """Load configuration variables from .env file."""
    load_dotenv()
    config = {
        'TELEGRAM_API_TOKEN': os.getenv('TELEGRAM_API_TOKEN')
    }
    return config
