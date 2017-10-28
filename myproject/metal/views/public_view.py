import os
from django.shortcuts import render
from metal.business.viewmodels.vm_login import LoginForm

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User

from django.forms.utils import ErrorList
from django.contrib import messages
from django import forms
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.urls import reverse
from metal.business.services.svs_user import UserService



def index(request):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print('-----------')
    print(os.path.join(base_dir, 'static/'))
    print('-----------')
    return render(request, 'public/index.html')


def login(request):
    print('Validation Started')
    username = "not logged in"
    _url = 'site/index.html'
    if request.method == 'POST':
        print (request.method)
        form = LoginForm(request.POST)
        print(form.is_valid())
        _url = 'user_buyer/index.html'
        # check if form is valid
        if form.is_valid():
            print ('form is valid')
            _email = request.POST['EmailAddress']
            _password = request.POST['Password']
            usr_svc = UserService()
            _ret = usr_svc.validate_user(request, _email, _password)
            return HttpResponseRedirect(reverse(_ret))
        else:
            messages.error(request, 'E92: Form is not valid.')
            return HttpResponseRedirect(reverse('public_index'))
    else:
        form = LoginForm()
    return render(request, _url)

def sign_out(request):
    print('Sign Out Started')
    return HttpResponseRedirect(reverse('public_index'))