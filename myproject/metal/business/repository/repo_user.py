from metal.models.MasterData import User_Profile
from metal.business.repository.repo_base import BaseRepository
from django.contrib.auth.models import UserManager
from django.contrib.auth.models import User
from datetime import datetime


class UserRepository(BaseRepository):
    def create_django_user(self, new_user_object):
        user_Mgr = UserManager()
        username = new_user_object['user_name']
        email = new_user_object['email_address']
        password = new_user_object['user_password']
        email = user_Mgr.normalize_email(email)
        django_user = User.objects.create_user(
            username,
            email,
            password)
        return django_user

    def register_user(self, new_user_object, user_type_code, company_obj, django_user):
        profile = User_Profile(
            user=django_user,
            User_Type=user_type_code,
            Rfq_Count=0,
            Quotation_Count=0,
            Version=datetime.now(),
            Title=new_user_object['title'],
            Contact_Number=new_user_object['contact_number'],
            Company=company_obj,
            Created_Date=datetime.now(),
            Created_By=new_user_object['user_name'],
            Modified_Date=datetime.now(),
            Modified_By=new_user_object['user_name'],
            Status=1
        )
        profile.save()
        return profile

    def get_user(self, _email):
        #_username = User.objects.get(email=_email.lower()).username
        _user = User.objects.get(email=_email.lower())
        return _user

    def get_user_profile(self, _user):
        user_profile = User_Profile.objects.get(user=_user)
        return user_profile