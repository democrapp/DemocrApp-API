import requests
from django.shortcuts import render, redirect
from democrapp_api.settings import DEBUG, MANAGER_URL, CLIENT_SECRET, CLIENT_ID, ALLOWED_HOSTS
from django.contrib.auth.models import User
from django.contrib.auth import login


# Create your views here.
def authorized(request):
    if request.GET.get('code'):
        protocol = "http" if DEBUG else "https"
        response = requests.post('{}://{}/o/token/'.format(protocol, MANAGER_URL),
                                 data={
                                     'code': request.GET.get('code'),
                                     'grant_type': 'authorization_code',
                                     'client_id': CLIENT_ID,
                                     'client_secret': CLIENT_SECRET,
                                 })
        headers = {'Authorization': 'Bearer {}'.format(response.json()['access_token'])}
        response = requests.get('{}://{}/api/profile'.format(protocol, MANAGER_URL),
                                headers=headers)
        r = response.json()
        my_slug = ALLOWED_HOSTS.split('.', 1)[0]
        if my_slug in r['slugs']:
            # get or create user
            u = User.objects.get_or_create(is_superuser=True, is_staff=True, username=r['username'])
            login(request, u)
            return redirect(request, '/admin')
