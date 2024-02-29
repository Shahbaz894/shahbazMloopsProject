import logging
import os
from datetime import datetime

# Corrected the method name from setftime to strftime
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_path = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_path, exist_ok=True)
LOG_FILE_Path = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_Path,  # Corrected the variable name to LOG_FILE_Path
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

if __name__ == "__main__":
    logging.info('Logging information message')
