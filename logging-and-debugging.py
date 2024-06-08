import logging

def main():
    # starting logging with creating file in system
    logging.basicConfig(filename="test.log", level=logging.INFO)

    # information to put into log file
    logging.info("this is my line execution")


    # error to put into log file
    logging.error("this is my error")


    # critical error to put into log file
    logging.critical("this is my critical file")

    # warning to put into log file
    logging.warning("this is my warning")

    # debug to put in log file
    logging.debug("this is my infro related to debug")


if __name__ == "__main__":
    main()
