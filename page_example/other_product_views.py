# -*- coding: utf-8 -*-
from django.contrib.auth.decorators import login_required
from models import OtherProductType, OtherProduct, OtherProductForm
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render_to_response, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from front_display.settings import RESULT_NUM_PER_PAGE
from django.views.decorators.csrf import csrf_exempt


@login_required
def admin_add_other_product(request):
    """

    :param request:
    :return:
    """
    other_product_form = OtherProductForm(request.POST, request.FILES)
    if other_product_form.is_valid():
        new_other_product = other_product_form.save()
        recent_other_product = OtherProduct.objects.all().order_by("-time")[0:3]

        return render_to_response("admin_pages/other_product_pages/other_product_recent_table.html", locals())
    else:
        print other_product_form.errors

        return JsonResponse(other_product_form.errors)


@login_required
def admin_filter_other_product(request):
    """
    :param request:
    :return:
    """
    other_product_res = OtherProduct.objects.all()
    print request.POST

    try:
        if request.POST['product_type']:
            other_product_res = other_product_res.filter(product_type=request.POST['product_type'])

        paginator = Paginator(other_product_res, RESULT_NUM_PER_PAGE)
        page = request.POST.get('page')

        try:
            other_product_res = paginator.page(page)
        except PageNotAnInteger:
            other_product_res = paginator.page(1)
        except EmptyPage:
            other_product_res = paginator.page(paginator.num_pages)

        read_only = request.POST.get('readonly')

        if read_only:
            return render_to_response('admin_pages/other_product_pages/other_product_table_readonly.html', locals())
        return render_to_response("admin_pages/other_product_pages/other_product_table.html", locals())

    except Exception,e:
        print e
        return render_to_response("admin_pages/other_product_pages/other_product_table.html")


@login_required
def admin_load_other_product_mod_form(request):
    """

    :param request:
    :return:
    """
    if 'witc' in request.POST:
        witc = request.POST['witc']

        try:
            other_product_obj = OtherProduct.objects.filter(full_witc=witc).first()
            other_product_form = OtherProductForm(instance=other_product_obj)
            return render_to_response("admin_pages/other_product_pages/other_product_form_tbl.html", locals())

        except Exception, e:
            print str(e)
            return HttpResponse(-1)

    return HttpResponse(-1)


@login_required
def admin_modify_other_product(request):
    """

    :param request:
    :return:
    """
    witc = request.POST['raw_witc']
    raw_obj = OtherProduct.objects.get(full_witc=str(witc))
    other_product_form = OtherProductForm(request.POST, request.FILES, instance=raw_obj)
    if other_product_form.is_valid():
        other_product_form.save()
        return HttpResponse(1)
    else:
        print other_product_form.errors
        return HttpResponse(-1)


@login_required
@csrf_exempt
def admin_delete_other_product(request):
    """

    :param request:
    :return:
    """
    if 'witc' in request.POST:
        witc = request.POST['witc']

        try:
            OtherProduct.objects.filter(full_witc=witc).delete()
            other_product_res = OtherProduct.objects.all()
            return render_to_response("admin_pages/other_product_pages/other_product_table.html", locals())

        except Exception, e:
            return HttpResponse(-1)
    return HttpResponse(-1)


@login_required
def admin_other_product_product(request):

    category = OtherProductType.objects.all()
    other_product_res = OtherProduct.objects.all()
    other_product_form = OtherProductForm()

    return render(request, 'admin_pages/product_other_product.html', locals())


def other_product_product(request):

    category = OtherProductType.objects.all()
    other_product_form = OtherProductForm()

    return render(request, 'page_example/product_other_product.html', locals())


def instrument_product(request):

    category = OtherProductType.objects.filter(content='器件')

    other_product_res = OtherProduct.objects.filter(product_type=category)

    return render(request, 'page_example/product_instrument.html', locals())


def tool_product(request):
    category = OtherProductType.objects.filter(content='工具设备')

    other_product_res = OtherProduct.objects.filter(product_type=category)
    return render(request, 'page_example/product_tool.html', locals())