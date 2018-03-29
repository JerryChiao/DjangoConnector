# coding:utf8
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render_to_response, render
from django.views.decorators.csrf import csrf_exempt
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from models import ConnectorPcbForm, ConnectorPcb, ConnectorCableForm, ConnectorCable, Polar, OutLook, \
    Category, InstallType, CombineType, RecentProduct
from django.core.files import File
from front_display.settings import RESULT_NUM_PER_PAGE


@login_required
def admin_add_pcb_connector(request):
    """

    :param request:
    :return:
    """
    connector_form = ConnectorPcbForm(request.POST, request.FILES)

    if connector_form.is_valid():
        new_pcb = connector_form.save()

        description_str = new_pcb.content_type.content + u',' + new_pcb.polar_type.content
        property_str = str(new_pcb.install_type) + ',' + str(new_pcb.outlook_type) + ',' + str(new_pcb.property)
        uploaded_image = new_pcb.image
        uploaded_document = new_pcb.document
        recent_prod_obj = RecentProduct(
            product_type="适配PCB连接器",
            description=description_str,
            property=property_str,
            image=File(uploaded_image, uploaded_image.name),
            full_witc=new_pcb.full_witc,
            r_witc=new_pcb.full_witc + "_connector_pcb",
            document=File(uploaded_document, uploaded_document.name)
                                        )
        recent_prod_obj.save()
        recent_connector_pcb = ConnectorPcb.objects.all().order_by("-time")[0:1]

        return render_to_response("admin_pages/connector_pages/connector_recent_table.html", locals())
    else:
        return render_to_response("admin_pages/connector_pages/connector_errors.html", locals())


@login_required
def admin_add_cable_connector(request):
    """

    :param request:
    :return:
    """
    connector_form = ConnectorCableForm(request.POST, request.FILES)
    try:
        if connector_form.is_valid():
            new_connector_cable = connector_form.save()
            description_str = new_connector_cable.content_type.content + u',' + new_connector_cable.polar_type.content
            property_str = str(new_connector_cable.install_type) + ',' + str(new_connector_cable.outlook_type) + ',' + \
                           str(new_connector_cable.property)
            uploaded_image = new_connector_cable.image
            uploaded_document = new_connector_cable.document
            recent_prod_obj = RecentProduct(
                product_type='适配电缆连接器',
                description=description_str,
                property=property_str,
                image=File(uploaded_image, uploaded_image.name),
                full_witc=new_connector_cable.full_witc,
                r_witc=new_connector_cable.full_witc + "_connector_cable",
                document=File(uploaded_document, uploaded_document.name)
            )
            recent_prod_obj.save()
            recent_connector_pcb = ConnectorCable.objects.all().order_by("-time")[0:1]

            return render_to_response("admin_pages/connector_pages/connector_recent_table.html", locals())
        else:
            return render_to_response("admin_pages/connector_pages/connector_errors.html", locals())

    except Exception, e:
        print(e)
        return HttpResponse(-1)


@login_required
def admin_filter_connector_pcb(request):
    """
    :param request:
    :return:
    """
    connector_pcb_res = ConnectorPcb.objects.all().order_by('time')
    try:
        if request.POST['category']:
            connector_pcb_res = connector_pcb_res.filter(content_type=request.POST['category'])

        if request.POST['polar']:
            polar = Polar.objects.get(content=request.POST['polar'])
            connector_pcb_res = connector_pcb_res.filter(polar_type=polar)

        if request.POST['install_type']:
            install_type = InstallType.objects.get(content=request.POST['install_type'])
            connector_pcb_res = connector_pcb_res.filter(install_type=install_type)

        if request.POST['outlook']:
            outlook = OutLook.objects.get(content=request.POST['outlook'])
            connector_pcb_res = connector_pcb_res.filter(outlook_type=outlook)

        paginator = Paginator(connector_pcb_res, RESULT_NUM_PER_PAGE)
        page = request.POST.get('page')
        print(page)
        try:
            connector_pcb_res = paginator.page(page)
        except PageNotAnInteger:
            connector_pcb_res = paginator.page(1)
        except EmptyPage:
            connector_pcb_res = paginator.page(paginator.num_pages)
        # read_only = request.POST.get('readonly')
        # if read_only:
        #     return render_to_response('admin_pages/connector_pages/connector_pcb_table_readonly.html', locals())
        return render_to_response("admin_pages/connector_pages/connector_pcb_table.html", locals())

    except Exception,e:
        return render_to_response("admin_pages/connector_pages/connector_pcb_table.html")


def load_filter_connector_pcb(request):
    """
    :param request:
    :return:
    """
    connector_pcb_res = ConnectorPcb.objects.all()
    print request.POST
    try:
        if request.POST['category']:
            connector_pcb_res = connector_pcb_res.filter(content_type=request.POST['category'])

        if request.POST['polar']:
            polar = Polar.objects.get(content=request.POST['polar'])
            connector_pcb_res = connector_pcb_res.filter(polar_type=polar)

        if request.POST['install_type']:
            install_type = InstallType.objects.get(content=request.POST['install_type'])
            connector_pcb_res = connector_pcb_res.filter(install_type=install_type)

        if request.POST['outlook']:
            outlook = OutLook.objects.get(content=request.POST['outlook'])
            connector_pcb_res = connector_pcb_res.filter(outlook_type=outlook)

        paginator = Paginator(connector_pcb_res, RESULT_NUM_PER_PAGE)
        page = request.POST.get('page')

        try:
            connector_pcb_res = paginator.page(page)
        except PageNotAnInteger:
            connector_pcb_res = paginator.page(1)
        except EmptyPage:
            connector_pcb_res = paginator.page(paginator.num_pages)

        return render_to_response('admin_pages/connector_pages/connector_pcb_table_readonly.html', locals())

    except Exception,e:
        return render_to_response("admin_pages/connector_pages/connector_pcb_table.html", locals())


@login_required
def admin_filter_connector_cable(request):
    """
    :param request:
    :return:
    """

    connector_cable_res = ConnectorCable.objects.all()
    print request.POST
    try:
        if request.POST['category']:
            connector_cable_res = connector_cable_res.filter(content_type=request.POST['category'])

        if request.POST['polar']:
            polar = Polar.objects.get(content=request.POST['polar'])
            connector_cable_res = connector_cable_res.filter(polar_type=polar)

        if request.POST['install_type']:
            install_type = InstallType.objects.get(content=request.POST['install_type'])
            connector_cable_res = connector_cable_res.filter(install_type=install_type)

        if request.POST['outlook']:
            outlook = OutLook.objects.get(content=request.POST['outlook'])
            connector_cable_res = connector_cable_res.filter(outlook_type=outlook)

        if request.POST['cable_type']:
            connector_cable_res = connector_cable_res.filter(cable_type=request.POST['cable_type'])

        paginator = Paginator(connector_cable_res, RESULT_NUM_PER_PAGE)

        page = request.POST.get('page')

        try:
            connector_cable_res = paginator.page(page)
        except PageNotAnInteger:
            connector_cable_res = paginator.page(1)
        except EmptyPage:
            connector_cable_res = paginator.page(paginator.num_pages)

        read_only = request.POST.get('readonly')
        print(read_only)
        if read_only:
            return render_to_response('admin_pages/connector_pages/connector_cable_table_readonly.html', locals())

        return render_to_response("admin_pages/connector_pages/connector_cable_table.html", locals())

    except Exception,e:
        print str(e)
        return render_to_response("admin_pages/connector_pages/connector_cable_table.html")


def load_filter_connector_cable(request):
    """
    :param request:
    :return:
    """

    connector_cable_res = ConnectorCable.objects.all()
    print request.POST
    try:
        if request.POST['category']:
            connector_cable_res = connector_cable_res.filter(content_type=request.POST['category'])

        if request.POST['polar']:
            polar = Polar.objects.get(content=request.POST['polar'])
            connector_cable_res = connector_cable_res.filter(polar_type=polar)

        if request.POST['install_type']:
            install_type = InstallType.objects.get(content=request.POST['install_type'])
            connector_cable_res = connector_cable_res.filter(install_type=install_type)

        if request.POST['outlook']:
            outlook = OutLook.objects.get(content=request.POST['outlook'])
            connector_cable_res = connector_cable_res.filter(outlook_type=outlook)

        if request.POST['cable_type']:
            connector_cable_res = connector_cable_res.filter(cable_type=request.POST['cable_type'])

        paginator = Paginator(connector_cable_res, RESULT_NUM_PER_PAGE)

        page = request.POST.get('page')

        try:
            connector_cable_res = paginator.page(page)
        except PageNotAnInteger:
            connector_cable_res = paginator.page(1)
        except EmptyPage:
            connector_cable_res = paginator.page(paginator.num_pages)

        read_only = request.POST.get('readonly')
        return render_to_response('admin_pages/connector_pages/connector_cable_table_readonly.html', locals())

    except Exception,e:
        print str(e)
        return render_to_response("admin_pages/connector_pages/connector_cable_table.html")


@login_required
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
            return render_to_response("admin_pages/connector_pages/connector_pcb_form_tbl.html", locals())

        except Exception, e:
            print str(e)
            return HttpResponse(-1)

    return HttpResponse(-1)


@login_required
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
            return render_to_response("admin_pages/connector_pages/connector_cable_form_tbl.html", locals())

        except Exception, e:
            print str(e)
            return HttpResponse(-1)

    return HttpResponse(-1)


@login_required
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


@login_required
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


@login_required
@csrf_exempt
def admin_delete_pcb_connector(request):
    """

    :param request:
    :return:
    """
    if 'witc' in request.POST:
        witc = request.POST['witc']
        r_witc = witc + "_connector_pcb"
        try:
            ConnectorPcb.objects.filter(full_witc=witc).delete()
            RecentProduct.objects.filter(r_witc=r_witc).delete()

            connector_pcb_res = ConnectorPcb.objects.all()
            return render_to_response("admin_pages/connector_pages/connector_pcb_table.html", locals())

        except Exception, e:
            print(e)
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
        r_witc = witc + "_connector_cable"
        try:
            ConnectorCable.objects.filter(full_witc=witc).delete()
            RecentProduct.objects.filter(r_witc=r_witc).delete()
            connector_cable_res = ConnectorCable.objects.all()
            return render_to_response("admin_pages/connector_pages/connector_cable_table.html", locals())

        except Exception, e:
            return HttpResponse(e)
    return HttpResponse(-1)


@login_required
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


def connector_product(request):
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
               'out_look': out_look,
               }
    return render(request, 'page_example/product_connector.html', context)