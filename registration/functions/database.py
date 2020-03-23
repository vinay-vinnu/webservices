import mysql.connector
import logging
from mysql.connector import errorcode
from metadata.functions.metadata import connectToDatabase
 
 
def saveClientPAsswordDB(dataObj):
    try:
        cnx = connectToDatabase()
        mycursor = cnx.cursor()
        sql = "UPDATE registration SET password = '"+dataObj['password']+"' WHERE phonenumber ={}".format(dataObj['phonenumber'])

        mycursor.execute(sql)

        cnx.commit()
        cnx.close()
    except Exception as e:
        logging.error("Error in saving client password "+str(e))
        raise