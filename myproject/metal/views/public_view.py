import os
from django.shortcuts import render
from metal.business.viewmodels.vm_login import LoginForm
from metal.models.MasterData import User_Profile
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.forms.utils import ErrorList
from django.contrib import messages
from django import forms
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.urls import reverse


def index(request):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print('-----------')
    print(os.path.join(base_dir, 'static/'))
    print('-----------')
    return render(request, 'public/index.html')


def login(request):
    # TODO: Please add Get Logic
    # TODO: please add Post Logic
    context = {}
    print('Validation Started')
    username = "not logged in"
    _url = 'site/index.html'
    if request.method == 'POST':
        print (request.method)
        form = LoginForm(request.POST)
        print(form.is_valid())
        # TODO: split between buyer and supplier
        _url = 'user_buyer/index.html'
        # check if form is valid
        if form.is_valid():
            print ('form is valid')
            _email = request.POST['EmailAddress']
            password = request.POST['Password']
            try:
                username = User.objects.get(email=_email.lower()).username
                _user = User.objects.get(email=_email.lower())
            except ObjectDoesNotExist:
                username = None
                #raise  Http404("User does not exist")
                print('user does not exist')
                #context['error'] = 'User not exists'
                messages.error(request, 'You don''t have authorization. Please register first.')
                return HttpResponseRedirect(reverse('public_index'))
                #_url = 'site/index.html'
            if username is not None:
                print (username)
                user = authenticate(request,username=username,password=password)
                try:
                    user_type = User_Profile.objects.get(user=_user).User_Type
                    user_type = user_type.Name.lower()
                    print(user_type)
                except ObjectDoesNotExist:
                    print('user does not exist')
                    messages.error(request, 'Insufficient authorization')
                    return HttpResponseRedirect(reverse('public_index'))
                if user is not None:
                    print ('authenticated')
                    if user.is_active:
                        print ('user is active')
                        auth_login(request,user)
                        if user_type == 'supplier':
                            _url = 'user_supplier/index.html'
                            return HttpResponseRedirect(reverse('user_supplier_index'))
                        elif user_type == 'buyer':
                            _url = 'user_buyer/index.html'
                            return HttpResponseRedirect(reverse('user_buyer_index'))
                        #return render(request, 'buyer/Dashboard.html')
                    else:
                        print ('user is not active')
                        context['error'] = 'Non Active User'
                        messages.error(request, 'Non Active User.')
                        #_url = 'site/index.html'
                        return HttpResponseRedirect(reverse('public_index'))
                else:
                    print ('Invalid Username or Password.')
                    #return HttpResponse('username or password wrong')
                    #raise forms.ValidationError(form.fields['EmailAddress'].error_messages['Bad Username or Password'])
                    messages.error(request, 'Invalid Username or Password.')
                    #_url = 'site/index.html'
                    return HttpResponseRedirect(reverse('public_index'))
        else:
            messages.error(request, 'E92: Form is not valid.')
            #_url = 'site/index.html'
            #messages.error(request, 'Please check your input.')
            return HttpResponseRedirect(reverse('public_index'))
    else:
        form = LoginForm()
    return render(request, _url)

def sign_out(request):
    print('Sign Out Started')
    return HttpResponseRedirect(reverse('public_index'))