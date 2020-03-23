from registration.functions.database import saveClientPAsswordDB
import logging



def saveClientPasswordService(dataObj):
    try:
        saveClientPAsswordDB(dataObj)
    except Exception as e:
        logging.error("Error in saving client password "+str(e))
        raise