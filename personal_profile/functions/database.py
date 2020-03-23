import mysql.connector
import logging
from mysql.connector import errorcode
from metadata.functions.metadata import connectToDatabase


def savePersonalProfileDB(dataObj):
    try:
        cnx = connectToDatabase()
        mycursor = cnx.cursor()
       
        sql = "INSERT INTO personal_profile (registeredmobile, firstname, lastname, email, marriedstatus, age, addr1, addr2, addr3,addr4,occupation) VALUES (%s, %s,%s, %s,%s, %s,%s, %s, %s, %s, %s)"
        #dataObj['registeredmobile']
        val = (dataObj['registeredMobile'],dataObj['firstName'],dataObj['lastName'],dataObj['email'],dataObj['marriedStatus'],dataObj['age'],dataObj['addrLine1'],dataObj['addrLine2'],dataObj['addrLine3'],dataObj['addrLine4'],dataObj['occupation'])
        
        mycursor.execute(sql, val)

        cnx.commit()
        
        cnx.close()
    except Exception as e:
        logging.error("Error in saving Personal Profile "+str(e))
        raise

def getPersonalProfileQuestionsDB():
    try:
        cnx = connectToDatabase()
        mycursor = cnx.cursor()
       
        mycursor.execute("select profqname,profqtype,profqorder,profqkey,profqselection from profquestion where profqstatus='A'")
        
        result = mycursor.fetchall()
        
        cnx.close()
        
        return result
    except Exception as e:
        logging.error("Error in retrieving Personal Profile questions "+str(e))
        raise

def getLookUpID(lookupname):
    try:
        cnx = connectToDatabase()
        mycursor = cnx.cursor()
       
        mycursor.execute("select lookupid from lookupmaster where lookupname='{}'".format(lookupname))
        
        result = mycursor.fetchall()
        
        cnx.close()
        
        return result
        
    except Exception as e:
        logging.error("Error in retrieving lookUpId "+str(e))
        raise

def getLookUpValues(lookupid):
    try:
        cnx = connectToDatabase()
        mycursor = cnx.cursor()
       
        mycursor.execute("select lookupname from lookupmaster where lookupid={} and lookupmasterid != 0".format(lookupid))
        
        result = mycursor.fetchall()
        
        cnx.close()
        
        return result
        
    except Exception as e:
        logging.error("Error in retrieving lookUpValues "+str(e))
        raise
