from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.utils.translation import ugettext as _
from django.contrib.auth.decorators import login_required

from models import *
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

@login_required(login_url="page_example/admin_login")
def admin_home(request):
    return render(request, 'admin_pages/new_home.html', {'user': request.user})


@login_required(login_url="page_example/admin_login")
def admin_connector_product(request):
    """
    """
    category = Category.objects.all()
    polar = Polar.objects.all()
    install_type = InstallType.objects.all()
    combine_type = CombineType.objects.all()
    out_look = OutLook.objects.all()
    context = {'polar': polar,
               'category': category,
               'install_type': install_type,
               'combine_type': combine_type,
               'out_look': out_look
               }
    return render(request, 'admin_pages/product_connector.html', context)


@login_required(login_url="page_example/admin_login")
def admin_converter_product(request):
    return render(request, 'admin_pages/product_converter.html')


@login_required(login_url="page_example/admin_login")
def admin_cable_product(request):
    return render(request, 'admin_pages/product_cable.html')


@login_required(login_url="page_example/admin_login")
def admin_cable_combo_product_vna(request):
    return render(request, 'admin_pages/product_cable_combo_vna.html')


@login_required(login_url="page_example/admin_login")
def admin_cable_combo_product_normal(request):
    return render(request, 'admin_pages/product_cable_combo_normal.html')


@login_required(login_url="page_example/admin_login")
def admin_cable_combo_product_gb(request):
    return render(request, 'admin_pages/product_cable_combo_bg.html')


@login_required(login_url="page_example/admin_login")
def admin_instrument_product(request):
    return render(request, 'admin_pages/product_instrument.html')


@login_required(login_url="page_example/admin_login")
def admin_tool_product(request):
    return render(request, 'admin_pages/product_tool.html')


def admin_modify_connector(request):
    return render(request, 'admin_pages/modify_product_connector.html')


def admin_others_install_type(request):
    install_type_res = InstallType.objects.all()
    content = {'install_types': install_type_res}
    return render(request, 'admin_pages/product_others_install_type.html', content)


def admin_add_install_type(request):
    install_type = request.POST['content']
    install_code = request.POST['code']
    obj = InstallType.objects.get(content=install_type, code=install_code)
    if not obj:
        InstallType.objects.create(content=install_type, code=install_code)
        return HttpResponse('1')
    else:
        return HttpResponse('-1')


def admin_modify_install_type(request):
    old_type = request.POST['old_content']
    old_code = request.POST['old_code']
    new_type = request.POST['new_content']
    new_code = request.POST['new_code']
    obj = InstallType.objects.get(content=old_type, code=old_code)
    if obj:
        obj.content = new_type
        obj.code = new_code
        obj.save()
        return HttpResponse('1')
    else:
        return HttpResponse('-1')


