import os
import logging
from datetime import datetime

from config import LOG_DIR


if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)


log_file = os.path.join(
    LOG_DIR,
    datetime.now().strftime("%Y-%m-%d") + ".log"
)


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    handlers=[
        logging.FileHandler(
            log_file,
            encoding="utf-8"
        ),
        logging.StreamHandler()
    ]
)


logger = logging.getLogger()