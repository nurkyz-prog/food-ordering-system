import logging

def start_logging(log_file="app.log"):
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        force=True
    )
    logging.info("Application started successfully")