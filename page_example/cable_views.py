from django.contrib.auth.decorators import login_required
from models import Cable, CableCategory, CableForm
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render_to_response, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from front_display.settings import RESULT_NUM_PER_PAGE
from django.views.decorators.csrf import csrf_exempt


def admin_add_cable(request):
    """

    :param request:
    :return:
    """
    cable_form = CableForm(request.POST, request.FILES)
    if cable_form.is_valid():
        new_cable = cable_form.save()
        recent_cable = Cable.objects.all().order_by("-time")[0:3]

        return render_to_response("admin_pages/cable_pages/cable_recent_table.html", locals())
    else:
        print cable_form.errors

        return JsonResponse(cable_form.errors)


def admin_filter_cable(request):
    """
    :param request:
    :return:
    """
    cable_res = Cable.objects.all()
    print request.POST

    try:
        if request.POST['category_type']:
            category = CableCategory.objects.get(content=request.POST['category_type'])
            cable_res = cable_res.filter(category_type=category)

        paginator = Paginator(cable_res, RESULT_NUM_PER_PAGE)
        page = request.POST.get('page')

        try:
            cable_res = paginator.page(page)
        except PageNotAnInteger:
            cable_res = paginator.page(1)
        except EmptyPage:
            cable_res = paginator.page(paginator.num_pages)

        read_only = request.POST.get('readonly')

        if read_only:
            return render_to_response('admin_pages/cable_pages/cable_table_readonly.html', locals())
        return render_to_response("admin_pages/cable_pages/cable_table.html", locals())

    except Exception,e:
        return render_to_response("admin_pages/cable_pages/cable_table.html")


def admin_load_cable_mod_form(request):
    """

    :param request:
    :return:
    """
    if 'witc' in request.POST:
        witc = request.POST['witc']

        try:
            cable_obj = Cable.objects.filter(full_witc=witc).first()
            cable_form = CableForm(instance=cable_obj)
            return render_to_response("admin_pages/cable_pages/cable_form_tbl.html", locals())

        except Exception, e:
            print str(e)
            return HttpResponse(-1)

    return HttpResponse(-1)


def admin_modify_cable(request):
    """

    :param request:
    :return:
    """
    witc = request.POST['raw_witc']
    raw_obj = Cable.objects.get(full_witc=str(witc))
    cable_form = CableForm(request.POST, request.FILES, instance=raw_obj)
    if cable_form.is_valid():
        cable_form.save()
        return HttpResponse(1)
    else:
        print cable_form.errors
        return HttpResponse(-1)


@csrf_exempt
def admin_delete_cable(request):
    """

    :param request:
    :return:
    """
    if 'witc' in request.POST:
        witc = request.POST['witc']

        try:
            Cable.objects.filter(full_witc=witc).delete()
            cable_res = Cable.objects.all()
            return render_to_response("admin_pages/cable_pages/cable_table.html", locals())

        except Exception, e:
            return HttpResponse(-1)
    return HttpResponse(-1)



@login_required(login_url="page_example/admin_login")
def admin_cable_product(request):

    category = CableCategory.objects.all()
    cable_res = Cable.objects.all()
    cable_form = CableForm()

    return render(request, 'admin_pages/product_cable.html', locals())



def cable_product(request):

    category = CableCategory.objects.all()
    cable_form = CableForm()

    return render(request, 'page_example/product_cable.html', locals())