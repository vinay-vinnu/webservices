from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from metadata.functions.metadata import getConfig, configureLogging
import logging
import json
from rest_framework.decorators import api_view
from registration.functions.registration_service import saveClientPasswordService


@csrf_exempt
@api_view(['PUT'])
def savePassword(request):
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
       
        if request.method == "PUT":
            print(json.loads(request.body.decode('utf-8')))
            saveClientPasswordService(json.loads(request.body.decode('utf-8')))
            #print(json.loads(request.body.decode('utf-8')))
            response['statusCode'] = 0
            response['data'] = 'Client password saved successfully'
                 
    except Exception as e:
        logging.error(str(e))
        response['data'] = 'Error in saving client password'
        response['error'] = str(e)
    return JsonResponse(response)

    