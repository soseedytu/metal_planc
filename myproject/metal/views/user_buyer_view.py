from django.shortcuts import render

app_label = 'metal'


def index(request):
    return render(request, 'user_buyer/index.html')
