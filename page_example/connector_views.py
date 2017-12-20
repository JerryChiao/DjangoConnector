from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render_to_response, render
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from page_example.models import ConnectorPcbForm, ConnectorPcb, ConnectorCableForm, ConnectorCable, Polar, OutLook, \
    Category, InstallType, CombineType


def admin_add_pcb_connector(request):
    """

    :param request:
    :return:
    """
    connector_form = ConnectorPcbForm(request.POST, request.FILES)
    if connector_form.is_valid():
        new_pcb = connector_form.save()
        recent_connector_pcb = ConnectorPcb.objects.all().order_by("-time")[0:3]

        return render_to_response("admin_pages/connector_recent_table.html", locals())
    else:
        print connector_form.errors

        return JsonResponse(connector_form.errors)


def admin_add_cable_connector(request):
    """

    :param request:
    :return:
    """
    connector_form = ConnectorCableForm(request.POST, request.FILES)
    if connector_form.is_valid():
        new_pcb = connector_form.save()
        recent_connector_pcb = ConnectorCable.objects.all().order_by("-time")[0:3]

        return render_to_response("admin_pages/connector_recent_table.html", locals())
    else:
        print connector_form.errors

        return JsonResponse(connector_form.errors)


def admin_filter_connector_pcb(request):
    """
    :param request:
    :return:
    """
    connector_pcb_res = ConnectorPcb.objects.all()
    try:
        if request.POST['category']:
            connector_pcb_res = connector_pcb_res.filter(content_type=request.POST['category'])

        if request.POST['polar']:
            polar = Polar.objects.get(content=request.POST['polar'])
            connector_pcb_res = connector_pcb_res.filter(polar_type=polar)

        if request.POST['install_type']:
            install_type = Polar.objects.get(content=request.POST['install_type'])
            connector_pcb_res = connector_pcb_res.filter(install_type=install_type)

        if request.POST['outlook']:
            outlook = OutLook.objects.get(content=request.POST['outlook'])
            connector_pcb_res = connector_pcb_res.filter(outlook_type=outlook)

        return render_to_response("admin_pages/connector_pcb_table.html", locals())

    except Exception,e:
        return render_to_response("admin_pages/connector_pcb_table.html")


global connector_cable_cache
global connector_pcb_cache


def admin_filter_connector_cable(request):
    """
    :param request:
    :return:
    """
    if request.method == 'POST':
        connector_cable_res = ConnectorCable.objects.all()
        print request.POST
        try:
            if request.POST['category']:
                connector_cable_res = connector_cable_res.filter(content_type=request.POST['category'])

            if request.POST['polar']:
                polar = Polar.objects.get(content=request.POST['polar'])
                connector_cable_res = connector_cable_res.filter(polar_type=polar)

            if request.POST['install_type']:
                install_type = Polar.objects.get(content=request.POST['install_type'])
                connector_cable_res = connector_cable_res.filter(install_type=install_type)

            if request.POST['outlook']:
                outlook = OutLook.objects.get(content=request.POST['outlook'])
                connector_cable_res = connector_cable_res.filter(outlook_type=outlook)

            paginator = Paginator(connector_cable_res, 3)

            page = request.GET.get('page')

            try:
                connector_cable_res = paginator.page(page)
            except PageNotAnInteger:
                connector_cable_res = paginator.page(1)
            except EmptyPage:
                connector_cable_res = paginator.page(paginator.num_pages)

            print connector_cable_res.has_next()
            print connector_cable_res.has_previous()
            print connector_cable_res.next_page_number()
            print connector_cable_res.number
            return render_to_response("admin_pages/connector_cable_table.html", locals())

        except Exception,e:
            print str(e)
            return render_to_response("admin_pages/connector_cable_table.html")


def admin_load_connector_pcb_mod_form(request):
    """

    :param request:
    :return:
    """
    if 'witc' in request.POST:
        witc = request.POST['witc']

        try:
            connector_pcb_obj = ConnectorPcb.objects.filter(full_witc=witc).first()
            connector_pcb_form = ConnectorPcbForm(instance=connector_pcb_obj)
            return render_to_response("admin_pages/connector_pcb_form_tbl.html", locals())

        except Exception, e:
            print str(e)
            return HttpResponse(-1)

    return HttpResponse(-1)


def admin_load_connector_cable_mod_form(request):
    """

    :param request:
    :return:
    """
    if 'witc' in request.POST:
        witc = request.POST['witc']

        try:
            connector_cable_obj = ConnectorCable.objects.filter(full_witc=witc).first()
            connector_cable_form = ConnectorCableForm(instance=connector_cable_obj)
            return render_to_response("admin_pages/connector_cable_form_tbl.html", locals())

        except Exception, e:
            print str(e)
            return HttpResponse(-1)

    return HttpResponse(-1)


def admin_modify_connector_pcb(request):
    """

    :param request:
    :return:
    """
    witc = request.POST['raw_witc']
    raw_obj = ConnectorPcb.objects.get(full_witc=str(witc))
    connector_form = ConnectorPcbForm(request.POST, request.FILES, instance=raw_obj)
    if connector_form.is_valid():
        connector_form.save()
        return HttpResponse(1)
    else:
        print connector_form.errors
        return HttpResponse(-1)


def admin_modify_connector_cable(request):
    """

    :param request:
    :return:
    """
    witc = request.POST['raw_witc']
    print witc
    raw_obj = ConnectorCable.objects.get(full_witc=str(witc))
    connector_form = ConnectorCableForm(request.POST, request.FILES, instance=raw_obj)
    if connector_form.is_valid():
        connector_form.save()
        return HttpResponse(1)
    else:
        print connector_form.errors
        return HttpResponse(-1)


@csrf_exempt
def admin_delete_pcb_connector(request):
    """

    :param request:
    :return:
    """
    if 'witc' in request.POST:
        witc = request.POST['witc']

        try:
            ConnectorPcb.objects.filter(full_witc=witc).delete()
            connector_pcb_res = ConnectorPcb.objects.all()
            return render_to_response("admin_pages/connector_pcb_table.html", locals())

        except Exception, e:
            return HttpResponse(-1)
    return HttpResponse(-1)


@csrf_exempt
def admin_delete_cable_connector(request):
    """

    :param request:
    :return:
    """
    if 'witc' in request.POST:
        witc = request.POST['witc']

        try:
            ConnectorCable.objects.filter(full_witc=witc).delete()
            connector_cable_res = ConnectorCable.objects.all()
            return render_to_response("admin_pages/connector_cable_table.html", locals())

        except Exception, e:
            return HttpResponse(-1)
    return HttpResponse(-1)


@login_required(login_url="page_example/admin_login")
def admin_connector_product(request):
    """
    """
    category = Category.objects.all()
    polar = Polar.objects.all()
    install_type = InstallType.objects.all()
    combine_type = CombineType.objects.all()
    out_look = OutLook.objects.all()
    connector_pcb_res = ConnectorPcb.objects.all()
    connector_pcb_form = ConnectorPcbForm()
    connector_cable_form = ConnectorCableForm()
    # connector_pcb_filter_form = ConnectorFilterForm()
    context = {'polar': polar,
               'category': category,
               'install_type': install_type,
               'combine_type': combine_type,
               'out_look': out_look,
               'connector_pcb_form': connector_pcb_form,
               'connector_cable_form': connector_cable_form,
               'connector_pcb_res': connector_pcb_res,
               }

    return render(request, 'admin_pages/product_connector.html', context)