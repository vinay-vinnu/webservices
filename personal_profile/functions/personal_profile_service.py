from personal_profile.functions.database import getLookUpValues,getLookUpID,savePersonalProfileDB,getPersonalProfileQuestionsDB
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