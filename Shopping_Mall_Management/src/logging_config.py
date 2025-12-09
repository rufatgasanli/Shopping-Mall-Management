import logging
import os

# Create logs folder
LOG_DIR = "logs"
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

# Logger configuration
logging.basicConfig(
    filename=os.path.join(LOG_DIR, "system.log"),
    level=logging.INFO,
    format="[%(asctime)s] [%(levelname)s] %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S",
    encoding="utf-8"
)

def get_logger(name):
    return logging.getLogger(name)
