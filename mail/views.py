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
        from_email = request.POST.get('from_email')
        from_pass = request.POST.get('from_pass')
        to_email = request.POST.get('to_email')
        description = request.POST.get('description')
        title = request.POST.get('title')
        subject = ""
        is_send, error = send_confirmation(from_email, from_pass, to_email, subject, description, title)
        response = {'status': is_send}
        if not is_send:
            response = {'status': is_send, 'error': error}
        return JsonResponse(response)
    else:
        print("GET")
        return JsonResponse({'status': True})
