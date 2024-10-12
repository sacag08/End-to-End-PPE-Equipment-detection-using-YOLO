from WorkerSafety.logger import logging
from WorkerSafety.exception import CustomException
import sys

logging.info("welcome")
def test():
    try:
        a = 1/0
    except Exception as e:
        logging.info("Divide by Zero")
        raise CustomException(e,sys)
test()