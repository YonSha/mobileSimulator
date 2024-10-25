# custom_logger.py

import logging

# ANSI escape sequences for colors
RESET = "\033[0m"
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"

# Custom log level colors
COLORS = {
    'DEBUG': BLUE,
    'INFO': GREEN,
    'WARNING': YELLOW,
    'ERROR': RED,
    'CRITICAL': MAGENTA,
}

# Custom logging format
class ColoredFormatter(logging.Formatter):
    def format(self, record):
        color = COLORS.get(record.levelname, RESET)
        record.msg = f"{color}{record.msg}{RESET}"
        return super().format(record)

def setup_logger():
    # Configure logging
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)  # Set to DEBUG to include all levels

    # Create console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)  # Set to DEBUG to include all levels
    console_handler.setFormatter(ColoredFormatter('%(asctime)s - %(levelname)s - %(message)s'))

    # Add the handler to the logger
    logger.addHandler(console_handler)

    return logger
