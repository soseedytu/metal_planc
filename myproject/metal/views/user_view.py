from django.shortcuts import render


app_label = 'metal'


def registration_main(request):
    return render(request, 'register/index.html')



