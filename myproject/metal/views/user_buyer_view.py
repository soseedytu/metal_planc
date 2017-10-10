from django.shortcuts import render

app_label = 'metal'


def index(request):
    print('index')
    return render(request, 'user_buyer/index.html')


def timeline(request):
    print('timeline')
    return render(request, 'user_buyer/timeline.html')


# list RFQ
def rfqs(request):
    return render(request, 'user_buyer/rfq_list.html')


# create/update RFQ
def rfq(request, rfq_id):
    return render(request, 'user_buyer/rfq_edit.html')


def rfq_view(request, rfq_id):
    return render(request, 'user_buyer/rfq_view.html')


def quotations(request):
    return render(request, 'user_buyer/quotation_list.html')


def quotation_view(request, quotation_id):
    return render(request, 'user_buyer/quotation_view.html')

def user_profile(request, user_id):
    return render(request, 'user_buyer/profile.html')
