__author__ = 'cromox'

import inspect
import logging
import datetime

def customLogger(logLevel=logging.DEBUG):
    # Gets the name of the class / method from where this method is called
    loggerName = inspect.stack()[1][3]
    logger = logging.getLogger(loggerName)
    # By default, log all messages
    logger.setLevel(logging.DEBUG)

    masani = datetime.datetime.now().strftime("%Y%m%d_%H")
    minitni = int(datetime.datetime.now().strftime("%M"))
    minit = int(minitni/5) * 5
    if minit < 10:
        minitstr = '0' + str(minit)
    else:
        minitstr = str(minit)
    fileHandler = logging.FileHandler("automation_" + masani + minitstr + "00.log", mode='a')
    fileHandler.setLevel(logLevel)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s', datefmt='%d/%m/%Y %I:%M:%S %p')
    fileHandler.setFormatter(formatter)
    logger.addHandler(fileHandler)

    return logger
