# coding:utf8
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from models import Category, Polar, InstallType, CombineType, OutLook, Converter, ConverterForm, RecentProduct
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render_to_response, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from front_display.settings import RESULT_NUM_PER_PAGE
from django.views.decorators.csrf import csrf_exempt
from django.core.files import File


def converter_product(request):

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

    return render(request, 'page_example/product_converter.html', context)


@login_required
def admin_add_converter(request):
    """

    :param request:
    :return:
    """
    converter_form = ConverterForm(request.POST, request.FILES)
    if converter_form.is_valid():
        new_converter = converter_form.save()

        description_str = new_converter.a_content_type.content + u',' + new_converter.a_polar_type.content + u'\n' + \
                          new_converter.b_content_type.content + u',' + new_converter.b_polar_type.content

        property_str = str(new_converter.install_type) + ',' + str(new_converter.outlook_type) + ',' + \
                       str(new_converter.property) + ',驻波：' + str(new_converter.standing_wave)
        uploaded_image = new_converter.image
        uploaded_document = new_converter.document
        recent_prod_obj = RecentProduct(
            product_type="转接器",
            description=description_str,
            property=property_str,
            image=File(uploaded_image, uploaded_image.name),
            r_witc=new_converter.full_witc + "_converter",
            full_witc=new_converter.full_witc,
            document=File(uploaded_document, uploaded_document.name)
        )

        recent_prod_obj.save()
        recent_converter = Converter.objects.all().order_by("-time")[0:1]

        return render_to_response("admin_pages/converter_pages/converter_recent_table.html", locals())
    else:
        return render_to_response("admin_pages/converter_pages/converter_errors.html", locals())


@login_required
def admin_filter_converter(request):
    """
    :param request:
    :return:
    """
    converter_res = Converter.objects.all()

    try:
        if request.POST['a_category']:
            converter_res = converter_res.filter(a_content_type=request.POST['a_category'])

        if request.POST['a_polar']:
            polar = Polar.objects.get(content=request.POST['a_polar'])
            converter_res = converter_res.filter(a_polar_type=polar)

        if request.POST['b_category']:
            converter_res = converter_res.filter(b_content_type=request.POST['b_category'])

        if request.POST['b_polar']:
            polar = Polar.objects.get(content=request.POST['b_polar'])
            converter_res = converter_res.filter(b_polar_type=polar)

        paginator = Paginator(converter_res, RESULT_NUM_PER_PAGE)
        page = request.POST.get('page')

        try:
            converter_res = paginator.page(page)
        except PageNotAnInteger:
            converter_res = paginator.page(1)
        except EmptyPage:
            converter_res = paginator.page(paginator.num_pages)

        read_only = request.POST.get('readonly')
        if read_only:
            return render_to_response('admin_pages/converter_pages/converter_table_readonly.html', locals())

        return render_to_response("admin_pages/converter_pages/converter_table.html", locals())

    except Exception,e:
        return render_to_response("admin_pages/converter_pages/converter_table.html")


def load_filter_converter(request):
    """
    :param request:
    :return:
    """
    converter_res = Converter.objects.all()

    try:
        if request.POST['a_category']:
            converter_res = converter_res.filter(a_content_type=request.POST['a_category'])

        if request.POST['a_polar']:
            polar = Polar.objects.get(content=request.POST['a_polar'])
            converter_res = converter_res.filter(a_polar_type=polar)

        if request.POST['b_category']:
            converter_res = converter_res.filter(b_content_type=request.POST['b_category'])

        if request.POST['b_polar']:
            polar = Polar.objects.get(content=request.POST['b_polar'])
            converter_res = converter_res.filter(b_polar_type=polar)

        paginator = Paginator(converter_res, RESULT_NUM_PER_PAGE)
        page = request.POST.get('page')

        try:
            converter_res = paginator.page(page)
        except PageNotAnInteger:
            converter_res = paginator.page(1)
        except EmptyPage:
            converter_res = paginator.page(paginator.num_pages)

        read_only = request.POST.get('readonly')

        return render_to_response('admin_pages/converter_pages/converter_table_readonly.html', locals())

    except Exception,e:
        return render_to_response("admin_pages/converter_pages/converter_table.html")


@login_required
def admin_load_converter_mod_form(request):
    """

    :param request:
    :return:
    """
    if 'witc' in request.POST:
        witc = request.POST['witc']
        try:
            converter_obj = Converter.objects.filter(full_witc=witc).first()
            converter_form = ConverterForm(instance=converter_obj)
            return render_to_response("admin_pages/converter_pages/converter_form_tbl.html", locals())

        except Exception, e:
            print str(e)
            return HttpResponse(-1)

    return HttpResponse(-1)


@login_required
def admin_modify_converter(request):
    """

    :param request:
    :return:
    """
    witc = request.POST['raw_witc']

    raw_obj = Converter.objects.get(full_witc=str(witc))
    converter_form = ConverterForm(request.POST, request.FILES, instance=raw_obj)
    if converter_form.is_valid():
        converter_form.save()
        return HttpResponse(1)
    else:
        print converter_form.errors
        return HttpResponse(-1)


@csrf_exempt
def admin_delete_converter(request):
    """

    :param request:
    :return:
    """
    if 'witc' in request.POST:
        witc = request.POST['witc']

        try:
            Converter.objects.filter(full_witc=witc).delete()
            r_witc = witc + "_converter"
            RecentProduct.objects.filter(r_witc=r_witc).delete()
            converter_res = Converter.objects.all()
            return render_to_response("admin_pages/converter_pages/converter_table.html", locals())

        except Exception, e:
            return HttpResponse(-1)
    return HttpResponse(-1)


@login_required
def admin_converter_product(request):

    category = Category.objects.all()
    polar = Polar.objects.all()
    install_type = InstallType.objects.all()
    combine_type = CombineType.objects.all()
    out_look = OutLook.objects.all()
    converter_res = Converter.objects.all()
    converter_form = ConverterForm()
    context = {'polar': polar,
               'category': category,
               'install_type': install_type,
               'combine_type': combine_type,
               'out_look': out_look,
               'converter_form': converter_form,
               'converter_res': converter_res,
               }

    return render(request, 'admin_pages/product_converter.html', context)
