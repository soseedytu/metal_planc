"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from metal.test_views import my_first_view
from metal.views import public_view
from metal.views import market_view
from metal.views import user_view
from metal.views import user_buyer_view
from metal.views import user_supplier_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', public_view.index),

    # Public App
    # http://localhost:8000/public/
    url(r'^public/$', public_view.index, name="public_index"),

    # Market App
    # http://localhost:8000/register/
    url(r'^register/$', user_view.registration_main, name="register_user_index"),
    # http://localhost:8000/market/
    url(r'^market/$', market_view.index, name="market_index"),

    # Buyer
    # http://localhost:8000/buyer/
    url(r'^buyer/$', user_buyer_view.index, name="user_buyer_index"),
    # http://localhost:8000/buyer/timeline
    url(r'^buyer/timeline/$', user_buyer_view.timeline, name="user_buyer_timeline"),
    # http://localhost:8000/buyer/rfqs
    url(r'^buyer/rfqs/$', user_buyer_view.rfqs, name="user_buyer_rfq_list"),
    # http://localhost:8000/buyer/rfq
    url(r'^buyer/rfq/(?P<rfq_id>[0-9]+)/$', user_buyer_view.rfq, name="user_buyer_rfq_create"),
    # http://localhost:8000/buyer/rfq/view
    url(r'^buyer/rfq/view/(?P<rfq_id>[0-9]+)$', user_buyer_view.rfq_view, name="user_buyer_rfq_view"),
    # http://localhost:8000/buyer/quotations
    url(r'^buyer/quotations/$', user_buyer_view.quotations, name="user_buyer_quotation_list"),
    # http://localhost:8000/buyer/1
    url(r'^buyer/(?P<user_id>[0-9]+)$', user_buyer_view.user_profile, name="user_buyer_profile"),

    # Supplier
    # http://localhost:8000/supplier/
    url(r'^supplier/$', user_supplier_view.index, name="user_supplier_index"),
    # http://localhost:8000/supplier/timeline
    url(r'^supplier/timeline/$', user_supplier_view.timeline, name="user_supplier_timeline"),
    # http://localhost:8000/supplier/rfq
    url(r'^supplier/rfqs/$', user_supplier_view.rfqs, name="user_supplier_rfq_list"),
    # http://localhost:8000/supplier/rfq/view
    url(r'^supplier/rfq/(?P<rfq_id>[0-9]+)$', user_supplier_view.rfq_view, name="user_supplier_rfq_view"),
    # http://localhost:8000/supplier/quotations
    url(r'^supplier/quotations/$', user_supplier_view.quotations, name="user_supplier_quotation_list"),
    # http://localhost:8000/supplier/1
    url(r'^supplier/(?P<user_id>[0-9]+)$', user_supplier_view.user_profile, name="user_supplier_profile"),
]
