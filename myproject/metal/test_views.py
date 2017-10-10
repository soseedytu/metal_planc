from django.shortcuts import render

def my_first_view(request):
	return render(request, 'metalpolis/hello.html')