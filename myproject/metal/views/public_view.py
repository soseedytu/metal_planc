import os, sys, json, smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from string import Template
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
from django.core.mail import send_mail
from metal.business.common.async_lib import AsyncLibrary


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
        print(request.method)
        form = LoginForm(request.POST)
        print(form.is_valid())
        # TODO: split between buyer and supplier
        _url = 'user_buyer/index.html'
        # check if form is valid
        if form.is_valid():
            print('form is valid')
            _email = request.POST['EmailAddress']
            password = request.POST['Password']
            try:
                username = User.objects.get(email=_email.lower()).username
                _user = User.objects.get(email=_email.lower())
            except ObjectDoesNotExist:
                username = None
                # raise  Http404("User does not exist")
                print('user does not exist')
                # context['error'] = 'User not exists'
                messages.error(request, 'You don''t have authorization. Please register first.')
                return HttpResponseRedirect(reverse('public_index'))
                # _url = 'site/index.html'
            if username is not None:
                print(username)
                user = authenticate(request, username=username, password=password)
                try:
                    user_type = User_Profile.objects.get(user=_user).User_Type
                    user_type = user_type.Name.lower()
                    print(user_type)
                except ObjectDoesNotExist:
                    print('user does not exist')
                    messages.error(request, 'Insufficient authorization')
                    return HttpResponseRedirect(reverse('public_index'))
                if user is not None:
                    print('authenticated')
                    if user.is_active:
                        print('user is active')
                        auth_login(request, user)
                        if user_type == 'supplier':
                            _url = 'user_supplier/index.html'
                            return HttpResponseRedirect(reverse('user_supplier_index'))
                        elif user_type == 'buyer':
                            _url = 'user_buyer/index.html'
                            return HttpResponseRedirect(reverse('user_buyer_index'))
                            # return render(request, 'buyer/Dashboard.html')
                    else:
                        print('user is not active')
                        context['error'] = 'Non Active User'
                        messages.error(request, 'Non Active User.')
                        # _url = 'site/index.html'
                        return HttpResponseRedirect(reverse('public_index'))
                else:
                    print('Invalid Username or Password.')
                    # return HttpResponse('username or password wrong')
                    # raise forms.ValidationError(form.fields['EmailAddress'].error_messages['Bad Username or Password'])
                    messages.error(request, 'Invalid Username or Password.')
                    # _url = 'site/index.html'
                    return HttpResponseRedirect(reverse('public_index'))
        else:
            messages.error(request, 'E92: Form is not valid.')
            # _url = 'site/index.html'
            # messages.error(request, 'Please check your input.')
            return HttpResponseRedirect(reverse('public_index'))
    else:
        form = LoginForm()
    return render(request, _url)


def sign_out(request):
    print('Sign Out Started')
    return HttpResponseRedirect(reverse('public_index'))

def email(request):

    if request.method == 'POST':
        name = request.POST['name']
        sender_email = request.POST['email']
        message = request.POST['message']
        subject = 'Enquiry from public site - ' + name
        metalpolis_email = 'info@metalpolis.com'

        EMAIL_HOST = 'smtp.zoho.com'
        EMAIL_PORT = 465
        EMAIL_HOST_USER = 'info@metalpolis.com'
        EMAIL_HOST_PASSWORD = '12345678'

        message = """
        Enquiry From
        -------------
        Name: """ + name + """
        Email: """ + sender_email + """
        
        -------------
        """ + message

        try:
            msg = MIMEText(message)
            msg['Subject'] = subject
            msg['From'] = metalpolis_email
            msg['To'] = metalpolis_email
            mail_body = msg.as_string()

            s = smtplib.SMTP_SSL(host=EMAIL_HOST, port=EMAIL_PORT)
            s.login(EMAIL_HOST_USER, EMAIL_HOST_PASSWORD)
            s.sendmail(metalpolis_email, metalpolis_email, mail_body)
            s.quit()

            reg_result = {
                'result': 'Email sent.',
                'errors': '',
            }
            return HttpResponse(json.dumps(reg_result), content_type="application/json")

        except:
            print("Unexpected error:", sys.exc_info()[0])
            reg_result = {
                'result': 'error',
                'errors': "Something wrong when sending email.",
            }
            return HttpResponse(json.dumps(reg_result), content_type="application/json")

    else:
        reg_result = {
            'result': 'invalid request',
            'errors': 'invalid request'
        }
        return HttpResponse(json.dumps(reg_result), content_type="application/json")







