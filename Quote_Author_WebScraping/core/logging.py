import logging
#import os

LOG_FILE = "logs.log"


def setup_logging():

    # Ensure the log directory exists:
    # os.makedirs(os.path.dirname(LOG_FILE),exist_ok=True)

    logging.basicConfig(
        filename=LOG_FILE,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        filemode='a',
    )

    # Writing to console
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(logging.Formatter("%(asctime)s - %(levelname)s - %(message)s"))

    logger = logging.getLogger(__name__)
    logger.addHandler(console_handler)

    return logger


# Create logger when module is imported
logger = setup_logging()