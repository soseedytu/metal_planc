from django import forms
from django.contrib.auth.models import User

class RegistrationForm(forms.Form):

    company_uen = forms.CharField(max_length=50)
    company_name = forms.CharField(max_length=50)
    contact_number = forms.CharField(max_length=50)
    tags = forms.CharField(required=False)
    user_name = forms.CharField(max_length=50)
    title = forms.CharField(max_length=50)
    email_address = forms.CharField(max_length=50)
    user_password = forms.PasswordInput()
    services = forms.CharField(required=False)
    register_as_supplier = forms.CharField()
    tags_text = forms.CharField(required=False)
    services_text = forms.CharField(required=False)

    #def clean(self):
        #password = self.cleaned_data.get("user_password")
        # email = self.cleaned_data.get("EmailAddress")
        # print("password")
        # print(upass)
        # auth_user = User.objects.filter(username=email)
        # #user = MUser.objects.get(EmailAddress=email)
        # print(auth_user)
        # if auth_user is None:
        #     print("error!")
        #     raise forms.ValidationError("User does not exist!")
        # else:
        #     print('found user!')
        #     return auth_user