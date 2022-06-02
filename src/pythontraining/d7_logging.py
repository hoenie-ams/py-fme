"""
Demo of the logging module
"""


import logging
logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)-8s %(message)s",
    filename="logging_demo.log",
    filemode="w"
)

logging.warning("This program is for demo purposes only.")


def main():
    logging.info("Starting the program")
    retrieve_data()
    logging.info("Ending the program")


def retrieve_data():
    logging.info("Downloading data")
    data = [1, 2, 3]
    logging.debug(data)


if __name__ == "__main__":
    main()
