from models import NormalComboCableForm
from django.shortcuts import render_to_response, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from models import ConnectorCable
from front_display.settings import RESULT_NUM_PER_PAGE


def normal_combo_cable_product(request):
    normal_combo_cable_filter_form = NormalComboCableForm()

    normal_combo_cable_res = []

    return render(request, 'page_example/product_normal_combo_cable.html', locals())


def admin_filter_normal_combo_cable(request):
    try:
        normal_combo_input_form = NormalComboCableForm(request)
        normal_combo_cable_res = []
        connectors = ConnectorCable.objects.all()

        if normal_combo_input_form.a_category_type:
            connector_1 = connectors.filter(content_type=normal_combo_input_form.a_category_type)

        if normal_combo_input_form.a_category_type:
            connector_2= connectors.filter(content_type=normal_combo_input_form.a_category_type)

        if connector_1 and connector_2:
            combo_res = {'a_content_type': connector_1.content_type.content,
                         'a_polar_type': connector_1.polar.content,
                         'a_install_type': connector_1.instann_type.content,
                         'a_outlook_type': connector_1.outlook.content,
                         'b_content_type': connector_2.content_type.content,
                         'b_polar_type': connector_2.polar.content,
                         'b_install_type': connector_2.instann_type.content,
                         'b_outlook_type': connector_2.outlook.content,

            }

            normal_combo_cable_res.append(combo_res)

        paginator = Paginator(normal_combo_cable_res, RESULT_NUM_PER_PAGE)
        page = request.POST.get('page')

        try:
            normal_combo_cable_res = paginator.page(page)
        except PageNotAnInteger:
            normal_combo_cable_res = paginator.page(1)
        except EmptyPage:
            normal_combo_cable_res = paginator.page(paginator.num_pages)

        read_only = request.POST.get('readonly')
        if read_only:
            return render_to_response('admin_pages/normal_combo_cable_pages/converter_table_readonly.html', locals())

        return render_to_response("admin_pages/normal_combo_cable_pages/converter_table.html", locals())

    except Exception, e:
        return render_to_response("admin_pages/converter_pages/converter_table.html")
