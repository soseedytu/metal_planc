from django.shortcuts import render
import os


def index(request):
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    print('-----------')
    print(os.path.join(base_dir, 'static/'))
    print('-----------')
    return render(request, 'public/index.html')

