import logging
import os
import allure

log_path = os.path.join(os.path.abspath(__file__ + '/../'), "current_log_file.log")


class AllureLoggingHandler(logging.Handler):
    def log(self, level_name, message):
        with allure.step(f"Log ({level_name}) {message}"):
            if level_name.lower() == "error":
                # attach_screenshot_in_report()
                assert False, "ERROR LOGGED"

    def emit(self, record):
        self.log(record.levelname, record.getMessage())


def get_logs():
    logger = logging.getLogger()
    if logger.hasHandlers():
        logger.handlers.clear()
    logging.basicConfig(format="%(asctime)s [%(levelname)s] %(message)s (%(filename)s:%(lineno)s)",
                        datefmt='%d/%m/%Y %I:%M:%S %p')
    allure_handler = AllureLoggingHandler()
    filehandler = logging.FileHandler(log_path, mode="w")
    formatter = logging.Formatter('%(asctime)s: %(levelname)s: %(module)s: %(funcName)s: %(message)s',
                                  datefmt='%d/%m/%Y %I:%M:%S %p')
    filehandler.setFormatter(formatter)
    logger.addHandler(filehandler)
    logger.setLevel(logging.INFO)
    logger.addHandler(allure_handler)
    return logger
