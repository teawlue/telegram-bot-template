# utils/__init__.py

import logging
from .helpers import load_config

# Configure logging for the entire bot
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO  # You can change to DEBUG for more details
)

logger = logging.getLogger(__name__)
