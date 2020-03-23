import logging
import configparser
import mysql.connector
from mysql.connector import errorcode
def getConfig():
    try:
        config = configparser.ConfigParser()
        config.read('D:\Production_files\config\webservicesconfig.ini')
        return config
    except Exception as e:
        raise 

def configureLogging(logConfig):
    try:
        logging.basicConfig(filename=logConfig['dir_path']+'webservice.log',
                        level=logConfig.getint('level'), format=logConfig['format'], datefmt=logConfig['date_format'])
        
    except Exception as e:
        raise   

def connectToDatabase():
    try:
        config=getConfig()
        sqldb_config = config['sqldb_config']
        cnx = mysql.connector.connect(user=sqldb_config['user'], password=sqldb_config['password'],
                              host=sqldb_config['host'],
                              database=sqldb_config['database'])
        return cnx
    except Exception as err:
        logging.error("Error in connecting to database "+str(err))
        raise 