from metal.models.MasterData import User_Profile
from metal.business.repository.repo_base import BaseRepository
from django.contrib.auth.models import UserManager
from datetime import datetime


class UserRepository(BaseRepository):
    def create_django_user(self, new_user_object):
        user_Mgr = UserManager()
        django_user = user_Mgr.create_user(
            new_user_object['user_name'],
            new_user_object['email_address'],
            new_user_object['password'])
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
