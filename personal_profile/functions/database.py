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

def getProfileData():
    try:
        cnx = connectToDatabase()
        mycursor = cnx.cursor()

        mycursor.execute("SELECT * FROM personal_profile;")

        allprofiles = mycursor.fetchall()

        return allprofiles
    except Exception:
        raise
        
def getProfileDataFromDbById(from_dbid):
    try:

        cnx = connectToDatabase()
        mycursor = cnx.cursor()
        sql = ("SELECT * FROM personal_profile WHERE ID = {};".format(from_dbid))


        mycursor.execute(sql)

        profilebyid = mycursor.fetchall()

        return profilebyid
    except Exception:
        raise
        
def updateProfileDataFromDbById(id,data):
    try:

        cnx = connectToDatabase()
        mycursor = cnx.cursor()

        sql = ("UPDATE personal_profile SET registeredmobile = '"+data['registeredMobile']+"',firstname = '"+data['firstName']+"',lastname = '"+data['lastName']+"',email = '"+data['email']+"',marriedstatus = '"+data['marriedStatus']+"',age = '"+data['age']+"',addr1 = '"+data['addrLine1']+"',addr2 = '"+data['addrLine2']+"',addr3 = '"+data['addrLine3']+"',addr4 = '"+data['addrLine4']+"',occupation = '"+data['occupation']+"' WHERE id = {};".format(id))



        mycursor.execute(sql)
        cnx.commit()
    except Exception:
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
