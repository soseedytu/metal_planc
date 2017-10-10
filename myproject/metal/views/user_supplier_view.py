from django.shortcuts import render

app_label = 'metal'


def index(request):
    return render(request, 'user_supplier/index.html')


def timeline(request):
    return render(request, 'user_supplier/timeline.html')


def rfqs(request):
    return render(request, 'user_supplier/rfq_list.html')


# view RFQ
def rfq_view(request, rfq_id):
    return render(request, 'user_supplier/rfq_view.html')


def quotations(request):
    return render(request, 'user_supplier/quotation_list.html')


def quotation(request, quotation_id):
    return render(request, 'user_supplier/quotation_edit.html')


def quotation_view(request, quotation_id):
    return render(request, 'user_supplier/quotation_view.html')


def user_profile(request, user_id):
    return render(request, 'user_supplier/profile.html')

