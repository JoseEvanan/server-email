import requests
import json

from django.conf import settings
from django.shortcuts import render
from django.http.response import JsonResponse
from django.views import generic
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

@csrf_exempt
def get_dni(request):
    if request.method == 'POST':
        """ POST Method """
        dni = request.POST.get('dni')
        print(request.POST)
        url_ = "https://tecactus.com/api/reniec/dni"
        data = json.dumps({'dni': '47291815'})
        headers = {
            'content-type': "application/x-www-form-urlencoded",
            'accept': "application/json",
            'authorization': "Bearer " + settings.TOKEN_TECACTUS,
        }
        r = requests.post(url_, data={'dni': dni}, headers=headers)

        return JsonResponse({'status': True, 'data': r.text })
    else:
        return JsonResponse({'status': False})


@csrf_exempt
def get_ruc(request):
    if request.method == 'POST':
        """ POST Method """
        document_type = request.POST.get('document_type')#dni-ruc
        document = request.POST.get('document')

        url_ = "https://tecactus.com/api/sunat/query/" + document_type
        headers = {
            'content-type': "application/x-www-form-urlencoded",
            'accept': "application/json",
            'authorization': "Bearer " + settings.TOKEN_TECACTUS,
        }
        r = requests.post(url_, data={document_type: document}, headers=headers)

        return JsonResponse({'status': True, 'data': r.text })
    else:
        return JsonResponse({'status': False})
