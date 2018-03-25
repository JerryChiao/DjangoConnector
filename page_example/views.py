# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.utils.translation import ugettext as _
from models import ConnectorPcb, Converter, Cable
from log.connector_logging import log
from django.views.decorators.csrf import csrf_exempt

from models import *


# Create your views here.


def test(request):

    return render(request, 'page_example/test_page.html')


def index(request):
    """
    main page
    """
    print request.LANGUAGE_CODE
    return render(request, 'page_example/new_home.html')


def cable_product(request):
    return render(request, 'page_example/product_cable.html')


def cable_combo_product_normal(request):
    return render(request, 'page_example/product_cable_combo_normal.html')


def cable_combo_product_gb(request):
    return render(request, 'page_example/product_cable_combo_bg.html')


def admin_login(request):
    next_url = request.POST.get('next')
    if next_url:
        return HttpResponseRedirect(next_url)

    return render(request, 'page_example/admin_login.html')


def notify_test(request):
    print "get notification"
    json = {'result': _('i know'),
            "aa": 'bb'}
    return JsonResponse(json)


@login_required
def admin_home(request):
    return render(request, 'admin_pages/new_home.html', {'user': request.user})


@login_required
def admin_cable_product(request):
    return render(request, 'admin_pages/product_cable.html')


@login_required
def admin_cable_combo_product_vna(request):
    return render(request, 'admin_pages/product_cable_combo_vna.html')


@login_required
def admin_cable_combo_product_normal(request):
    return render(request, 'admin_pages/product_cable_combo_normal.html')


@login_required
def admin_cable_combo_product_gb(request):
    return render(request, 'admin_pages/product_cable_combo_bg.html')


@login_required
def admin_instrument_product(request):
    return render(request, 'admin_pages/product_instrument.html')


@login_required
def admin_tool_product(request):
    return render(request, 'admin_pages/product_tool.html')


@login_required
def admin_others_install_type(request):
    install_type_res = InstallType.objects.all()
    content = {'install_types': install_type_res}
    return render(request, 'admin_pages/product_others_install_type.html', content)


@login_required
def admin_add_install_type(request):
    install_type = request.POST['content']
    install_code = request.POST['code']
    try:
        InstallType.objects.get(content=install_type, code=install_code)
        return HttpResponse('-1')
    except Exception, e:
        InstallType.objects.create(content=install_type, code=install_code)
        return HttpResponse('1')


@login_required
def admin_modify_install_type(request):
    old_type = request.POST['old_content']
    old_code = request.POST['old_code']
    new_type = request.POST['new_content']
    new_code = request.POST['new_code']

    try:
        obj = InstallType.objects.get(content=old_type, code=old_code)
        obj.content = new_type
        obj.code = new_code
        obj.save()
        return HttpResponse('1')

    except Exception, e:
        return HttpResponse('-1')


@login_required
def admin_delete_install_type(request):

    install_type = request.POST['content']
    install_code = request.POST['code']

    try:
        InstallType.objects.filter(content=install_type, code=install_code).delete()
        return HttpResponse('1')
    except Exception, e:
        print str(e)
        return HttpResponse('-1')


@login_required
def admin_others_outlook(request):
    out_look_res = OutLook.objects.all()
    content = {'out_look': out_look_res}
    return render(request, 'admin_pages/product_others_outlook.html', content)


@login_required
def admin_add_outlook(request):

    outlook_type = request.POST['content']
    outlook_code = request.POST['code']
    try:
        OutLook.objects.get(content=outlook_type, code=outlook_code)
        return HttpResponse('-1')
    except Exception, e:
        OutLook.objects.create(content=outlook_type, code=outlook_code)
        return HttpResponse('1')


@login_required
def admin_modify_outlook(request):

    old_type = request.POST['old_content']
    old_code = request.POST['old_code']
    new_type = request.POST['new_content']
    new_code = request.POST['new_code']
    try:
        obj = OutLook.objects.get(content=old_type, code=old_code)
        obj.content = new_type
        obj.code = new_code
        obj.save()
        return HttpResponse('1')
    except Exception, e:
        print str(e)
        return HttpResponse('-1')


@login_required
def admin_delete_outlook(request):

    outlook_type = request.POST['content']
    outlook_code = request.POST['code']

    try:
        OutLook.objects.filter(content=outlook_type, code=outlook_code).delete()
        return HttpResponse('1')
    except Exception, e:
        print str(e)
        return HttpResponse('-1')


@login_required
def admin_others_category(request):
    category_res = Category.objects.all()
    content = {'category': category_res}
    return render(request, 'admin_pages/product_others_category.html', content)


@login_required
def admin_add_category(request):

    outlook_type = request.POST['content']
    outlook_code = request.POST['code']
    try:
        Category.objects.get(content=outlook_type, code=outlook_code)
        return HttpResponse('-1')
    except Exception, e:
        Category.objects.create(content=outlook_type, code=outlook_code)
        return HttpResponse('1')


@login_required
def admin_modify_category(request):

    old_type = request.POST['old_content']
    old_code = request.POST['old_code']
    new_type = request.POST['new_content']
    new_code = request.POST['new_code']
    try:
        obj = Category.objects.get(content=old_type, code=old_code)
        obj.content = new_type
        obj.code = new_code
        obj.save()
        return HttpResponse('1')
    except Exception, e:
        print str(e)
        return HttpResponse('-1')


@login_required
def admin_delete_category(request):

    outlook_type = request.POST['content']
    outlook_code = request.POST['code']

    try:
        Category.objects.filter(content=outlook_type, code=outlook_code).delete()
        return HttpResponse('1')
    except Exception, e:
        print str(e)
        return HttpResponse('-1')


@login_required
def admin_others_combo_type(request):
    install_type_res = CombineType.objects.all()
    content = {'combo_types': install_type_res}
    return render(request, 'admin_pages/product_others_combo_type.html', content)


@login_required
def admin_add_combo_type(request):
    install_type = request.POST['content']
    install_code = request.POST['code']
    try:
        CombineType.objects.get(content=install_type, code=install_code)
        return HttpResponse('-1')
    except Exception,e:

        CombineType.objects.create(content=install_type, code=install_code)
        return HttpResponse('1')


@login_required
def admin_modify_combo_type(request):
    old_type = request.POST['old_content']
    old_code = request.POST['old_code']
    new_type = request.POST['new_content']
    new_code = request.POST['new_code']

    try:
        obj = CombineType.objects.get(content=old_type, code=old_code)
        obj.content = new_type
        obj.code = new_code
        obj.save()
        return HttpResponse('1')

    except Exception, e:
        return HttpResponse('-1')


@login_required
def admin_delete_combo_type(request):

    install_type = request.POST['content']
    install_code = request.POST['code']

    try:
        CombineType.objects.filter(content=install_type, code=install_code).delete()
        return HttpResponse('1')
    except Exception, e:
        print str(e)
        return HttpResponse('-1')

@csrf_exempt
def load_recent_product(request):
    try:
        converter_res = Converter.objects.all().order_by('-time')[0:1]
        recent_res = Cable.objects.all().order_by('-time')[0:1]

        return render_to_response('page_example/recent_product_table_readonly.html', locals())
    except Exception, e:
        print(e)
        return HttpResponse()

