from django.shortcuts import render
from django.http.response import JsonResponse
from django.views import generic
from .utils import send_confirmation
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

@csrf_exempt
def send_email(request):
    if request.method == 'POST':
        """ POST Method """
        print(request.POST)
        from_email = request.POST.get('from_email')
        from_pass = request.POST.get('from_pass')
        to_email = request.POST.get('to_email')
        description = request.POST.get('description')
        title = request.POST.get('title')
        subject = ""
        is_send = send_confirmation(from_email, from_pass, to_email, subject, description, title)
        return JsonResponse({'status': is_send})
    else:
        print("GET")
        return JsonResponse({'status': True})
