from personal_profile.functions.database import getLookUpValues,getLookUpID,savePersonalProfileDB,getPersonalProfileQuestionsDB,getProfileData, getProfileDataFromDbById, updateProfileDataFromDbById
import logging

def savePersonalProfileService(personal_profile):
    try:
        savePersonalProfileDB(personal_profile)
    except Exception as e:
        logging.error("Error in saving personal profile "+str(e))
        raise    
    
def getPersonalProfileQuestionsService():
    try:
        profileQuestions=getPersonalProfileQuestionsDB()
        
        temp = []
        
        for profileQuestion in profileQuestions:
           
            profileQuestionsObj = {
                'profqname':profileQuestion[0],
                'profqtype':profileQuestion[1],
                'profqorder':profileQuestion[2],
                'profqkey': profileQuestion[3],
                'profqselection': profileQuestion[4],
                'values':None
            }
            
            lookUpId = getLookUpID(profileQuestionsObj['profqkey'])
            
            if len(lookUpId) != 0:
                
                lookUpValues = getLookUpValues(lookUpId[0][0])
                lookUpValues = [ lookUpValue[0] for lookUpValue in lookUpValues]
                profileQuestionsObj['values']=lookUpValues      
            temp.append(profileQuestionsObj)
        profileQuestions = temp
        #print(profileQuestions)
        return profileQuestions
    except Exception as e:
        logging.error("Error in retrieving personal profile questions "+str(e))
        
def personalProfileDataByIdService(id):
    try:
        from_dbid = getProfileDataFromDbById(id)
        temp = []
        for i in from_dbid:
            id_index = {
                'ID': i[0],
                "registeredMobile": i[1],
                "firstName": i[2],
                "lastName": i[3],
                "email": i[4],
                "marriedStatus": i[5],
                "age": i[6],
                "addrLine1": i[7],
                "addrLine2": i[8],
                "addrLine3": i[9],
                "addrLine4": i[10],
                "occupation": i[11]
            }
            temp.append(id_index)
        if temp == []:
            return 0
        else:
            return temp
    except Exception as msg:
        logging.error('Error in getting Profiles' + str(msg))
        raise
        
def personalProfileEditDataByIdService(id, data):
    try:
        from_editdbid = updateProfileDataFromDbById(id, data)
    except Exception as msg:
        logging.error('Error in updating Profiles' + str(msg))
        raise
        
def personalProfileDataService():
    try:
        profiles = getProfileData()
        temp = []
        for profile in profiles:
            prof = {
                'ID': profile[0],
                "registeredMobile": profile[1],
                "firstName": profile[2],
                "lastName": profile[3],
                "email": profile[4],
                "marriedStatus": profile[5],
                "age": profile[6],
                "addrLine1": profile[7],
                "addrLine2": profile[8],
                "addrLine3": profile[9],
                "addrLine4": profile[10],
                "occupation": profile[11]
            }
            temp.append(prof)
        return temp
    except Exception as msg:
        logging.error('Error in getting Profiles' + str(msg))
        raise
