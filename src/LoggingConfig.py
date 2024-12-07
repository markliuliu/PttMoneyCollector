import logging
import os.path

FOLDER = "./log"


def configure_logging():
    if not os.path.exists(FOLDER):
        os.makedirs(FOLDER)
    logging.basicConfig(filename=f'{FOLDER}/scheduler.log', level=logging.INFO, encoding="UTF-8",
                        format='[%(asctime)s]-[%(levelname)s]-[%(name)s]: %(message)s')
