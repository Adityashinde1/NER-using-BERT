import logging
import os
from from_root import from_root
from ner.constant import ARTIFACTS_DIR, LOGS_DIR, LOGS_FILE_NAME

logs_path = os.path.join(from_root(), ARTIFACTS_DIR, LOGS_DIR)

os.makedirs(logs_path, exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path, LOGS_FILE_NAME)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,
)