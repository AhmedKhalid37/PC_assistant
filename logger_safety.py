import logging
from datetime import datetime

# logging
# save logs to app.log
logging.basicConfig(
    filename='app.log',
    filemode='a',  # Append to the file
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# log a normal/safe info message
def log_info(message):
    logging.info(message)
    print(f"[INFO] {datetime.now()} - {message}")

# log a warning message
def log_warning(message):
    logging.warning(message)
    print(f"[WARNING] {datetime.now()} - {message}")

# log an error message
def log_error(message):
    logging.error(message)
    print(f"[ERROR] {datetime.now()} - {message}")

# safety
# list of commands to be blocked
DANGEROUS_COMMANDS = ["shutdown", "reboot", "format", "delete", "rm", "kill", "erase", "exit()"]

# a function which will return false if text contains any dangerous command
def is_safe_input(text):
    text = text.lower()
    for cmd in DANGEROUS_COMMANDS:
        if cmd in text:
            return False
    return True

