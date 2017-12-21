from django.contrib.auth.decorators import login_required
from models import Category, Polar, VNAComboCable, VNAComboCableForm
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render_to_response, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from front_display.settings import RESULT_NUM_PER_PAGE
from django.views.decorators.csrf import csrf_exempt


def vna_combo_cable_product(request):

    polar = Polar.objects.all()

    context = {'polar': polar,
               }

    return render(request, 'page_example/product_vna_combo_cable.html', context)


def admin_add_vna_combo_cable(request):
    """

    :param request:
    :return:
    """
    vna_combo_cable_form = VNAComboCableForm(request.POST, request.FILES)
    if vna_combo_cable_form.is_valid():
        new_vna_combo_cable = vna_combo_cable_form.save()
        recent_vna_combo_cable = VNAComboCable.objects.all().order_by("-time")[0:1]

        return render_to_response("admin_pages/vna_combo_cable_pages/vna_combo_cable_recent_table.html", locals())
    else:
        print vna_combo_cable_form.errors

        return JsonResponse(vna_combo_cable_form.errors)


def admin_filter_vna_combo_cable(request):
    """
    :param request:
    :return:
    """
    vna_combo_cable_res = VNAComboCable.objects.all()
    print request.POST
    try:
        if request.POST['a_category']:
            vna_combo_cable_res = vna_combo_cable_res.filter(a_content_type=request.POST['a_category'])

        if request.POST['a_polar']:
            polar = Polar.objects.get(content=request.POST['a_polar'])
            vna_combo_cable_res = vna_combo_cable_res.filter(a_polar_type=polar)

        if request.POST['b_category']:
            vna_combo_cable_res = vna_combo_cable_res.filter(b_content_type=request.POST['b_category'])

        if request.POST['b_polar']:
            polar = Polar.objects.get(content=request.POST['b_polar'])
            vna_combo_cable_res = vna_combo_cable_res.filter(b_polar_type=polar)

        paginator = Paginator(vna_combo_cable_res, RESULT_NUM_PER_PAGE)
        page = request.POST.get('page')

        try:
            vna_combo_cable_res = paginator.page(page)
        except PageNotAnInteger:
            vna_combo_cable_res = paginator.page(1)
        except EmptyPage:
            vna_combo_cable_res = paginator.page(paginator.num_pages)

        read_only = request.POST.get('readonly')
        if read_only:
            return render_to_response('admin_pages/vna_combo_cable_pages/vna_combo_cable_table_readonly.html', locals())

        print "here"
        return render_to_response("admin_pages/vna_combo_cable_pages/vna_combo_cable_table.html", locals())

    except Exception,e:
        return render_to_response("admin_pages/vna_combo_cable_pages/vna_combo_cable_table.html")


def admin_load_vna_combo_cable_mod_form(request):
    """

    :param request:
    :return:
    """
    if 'witc' in request.POST:
        witc = request.POST['witc']

        try:
            vna_combo_cable_obj = VNAComboCable.objects.filter(full_witc=witc).first()
            vna_combo_cable_form = VNAComboCableForm(instance=vna_combo_cable_obj)
            return render_to_response("admin_pages/vna_combo_cable_pages/vna_combo_cable_form_tbl.html", locals())

        except Exception, e:
            print str(e)
            return HttpResponse(-1)

    return HttpResponse(-1)


def admin_modify_vna_combo_cable(request):
    """

    :param request:
    :return:
    """
    witc = request.POST['raw_witc']
    raw_obj = VNAComboCable.objects.get(full_witc=str(witc))
    vna_combo_cable_form = VNAComboCableForm(request.POST, request.FILES, instance=raw_obj)
    if vna_combo_cable_form.is_valid():
        vna_combo_cable_form.save()
        return HttpResponse(1)
    else:
        print vna_combo_cable_form.errors
        return HttpResponse(-1)


@csrf_exempt
def admin_delete_vna_combo_cable(request):
    """

    :param request:
    :return:
    """
    if 'witc' in request.POST:
        witc = request.POST['witc']

        try:
            VNAComboCable.objects.filter(full_witc=witc).delete()
            vna_combo_cable_res = VNAComboCable.objects.all()
            return render_to_response("admin_pages/vna_combo_cable_pages/vna_combo_cable_table.html", locals())

        except Exception, e:
            return HttpResponse(-1)
    return HttpResponse(-1)


@login_required(login_url="page_example/admin_login")
def admin_vna_combo_cable_product(request):

    polar = Polar.objects.all()
    vna_combo_cable_res = VNAComboCable.objects.all()
    vna_combo_cable_form = VNAComboCableForm()
    context = {'polar': polar,
               'vna_combo_cable_form': vna_combo_cable_form,
               'vna_combo_cable_res': vna_combo_cable_res,
               }

    return render(request, 'admin_pages/product_vna_combo_cable.html', context)


def cable_combo_product_vna(request):
    polar = Polar.objects.all()

    return render(request, 'page_example/product_vna_combo_cable.html', locals())