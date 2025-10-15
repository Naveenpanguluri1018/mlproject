import datetime
import logging
import os

log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)
log_file = f"{datetime.datetime.now().strftime('%m%d%Y__%H%M%S')}.log"
log_file_path = os.path.join(log_dir, log_file)

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file_path),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)
logger.info(f"Logging is set up. Log file at: {log_file_path}")
