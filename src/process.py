# src/main.py
import logging
import logging.config
import os
from datetime import datetime
from decouple import config
from config import logging

# download the latest log file
LOGGER = logging.create_log('proccess')

if __name__ == "__main__":
    logger = logging.getLogger(__name__)
    logger.info("Program started")
    logger.info("Program finished")