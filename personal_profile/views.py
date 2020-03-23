from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from metadata.functions.metadata import getConfig, configureLogging
from personal_profile.functions.personal_profile_service import savePersonalProfileService,getPersonalProfileQuestionsService
import logging
import json
from rest_framework.decorators import api_view


@csrf_exempt
@api_view(['GET', 'POST'])
def personalProfileView(request):
    response = {
        'data':None,
        'error':None,
        'statusCode': 1
    }
    try:
        if 'userName' in request.COOKIES:
            print(request.COOKIES['userName'])
        else:
            raise Exception("Authentication failure")   

        config=getConfig()
        log=config['log']
        configureLogging(log)
       
        if request.method == "POST":
            #print(request.POST)
            savePersonalProfileService(json.loads(request.body.decode('utf-8')))
            #print(json.loads(request.body.decode('utf-8')))
            response['statusCode'] = 0
            response['data'] = 'Personal Profile data saved successfully'
        elif request.method == "GET":
             print(type(request.GET.get("g")))
                 
    except Exception as e:
        logging.error(str(e))
        response['data'] = 'Error in saving Personal Profile data'
        response['error'] = str(e)
    return JsonResponse(response)


@csrf_exempt
@api_view(['GET'])
def personalProfileQuestionsView(request):
    response = {
        'data':None,
        'error':None,
        'statusCode': 1
    }
    try:
        if 'userName' in request.COOKIES:
            print(request.COOKIES['userName'])
        else:
            raise Exception("Authentication failure")   

        config=getConfig()
        log=config['log']
        configureLogging(log)
       
        if request.method == "GET":
            #print(request.POST)
            profileQuestions=getPersonalProfileQuestionsService()
            #print(json.loads(request.body.decode('utf-8')))
            response['statusCode'] = 0
            response['data'] = profileQuestions
                 
    except Exception as e:
        logging.error(str(e))
        response['data'] = 'Error in retrieving Personal Profile questions'
        response['error'] = str(e)
    return JsonResponse(response)

