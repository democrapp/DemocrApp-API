import os
import requests
import json
from django.http import JsonResponse, HttpResponseNotAllowed
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from ..models import Meeting, Session
from democrapp_api.settings import GRK_SECRET


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[-1].strip()
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


@csrf_exempt
def check_token(request, meeting_id):
    token = request.POST['token']
    recaptcha = request.POST['recaptcha']

    # Google Recaptcha v2 - https://developers.google.com/recaptcha/docs/verify
    grk_post_data = {
        'secret': GRK_SECRET,
        'response': recaptcha,
        'remoteip': get_client_ip(request)
        }
    grk_response = requests.post('https://www.google.com/recaptcha/api/siteverify', data=grk_post_data)
    grk_content = json.loads(grk_response.content)

    if not grk_content['success']:
        return HttpResponseNotAllowed('Google Recaptcha failed: ' + grk_content['error-codes'])

    meeting = get_object_or_404(Meeting, pk=meeting_id)
    current_set = meeting.tokenset_set.latest('created_at')
    if current_set.authtoken_set.filter(pk=token).exists():
        s = Session(auth_token_id=token)
        s.save()
        sessions = Session.objects.filter(auth_token_id=token)
        response = {
            "success": True,
            "session_token": s.id,
            "num_sessions": sessions.count(),
            "active_sessions": sessions.exclude(channel=None).count(),
        }
        response = JsonResponse(response)
    else:
        response = JsonResponse({"success": False, "reason": "BadToken"})
    return response