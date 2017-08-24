from django.shortcuts import render
from django.http import JsonResponse
from django.utils.translation import ugettext as _
# Create your views here.

def index(request):
    """
    main page
    """
    print request.LANGUAGE_CODE
    return render(request, 'page_example/new_home.html')


def connector_product(request):
    """
    """
    return render(request, 'page_example/product_connector.html')


def converter_product(request):
    return render(request, 'page_example/product_converter.html')


def cable_product(request):
    return render(request, 'page_example/product_cable.html')
    

def cable_combo_product_vna(request):
    return render(request, 'page_example/product_cable_combo_vna.html')


def cable_combo_product_normal(request):
    return render(request, 'page_example/product_cable_combo_normal.html')

def cable_combo_product_gb(request):
    return render(request, 'page_example/product_cable_combo_bg.html')


def instrument_product(request):
    return render(request, 'page_example/product_instrument.html')


def tool_product(request):
    return render(request, 'page_example/product_tool.html')

def admin_login(request):
    return render(request, 'page_example/admin_login.html')

def notify_test(request):
    print "get notification"
    json = {'result': _('i know'),
            "aa": 'bb'}
    return JsonResponse(json)