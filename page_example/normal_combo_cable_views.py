from models import NormalComboCableForm
from django.shortcuts import render_to_response, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from models import ConnectorCable, Cable
from front_display.settings import RESULT_NUM_PER_PAGE
from django.contrib.auth.decorators import login_required


def normal_combo_cable_product(request):
    normal_combo_cable_filter_form = NormalComboCableForm()

    normal_combo_cable_res = []

    return render(request, 'page_example/product_normal_combo_cable.html', locals())


def order_witc(witc1, witc2):
    if cmp(witc1, witc2) > 0:
        return witc1, witc2
    return witc2, witc1


@login_required
def admin_filter_normal_combo_cable(request):
    # try:

    normal_combo_input_form = NormalComboCableForm(request.POST)
    normal_combo_cable_res = []
    connectors = ConnectorCable.objects.all()
    connector_1, connector_2 = None, None

    if normal_combo_input_form['a_category_type']:
        connector_1 = connectors.filter(content_type=normal_combo_input_form['a_category_type'].value())

    if normal_combo_input_form['b_category_type']:
        connector_2 = connectors.filter(content_type=normal_combo_input_form['b_category_type'].value())

    if normal_combo_input_form['cable_length']:
        cable = Cable.objects.filter(upper_frequency__gte=normal_combo_input_form['cable_length'].value())

    if connector_1 and connector_2:
        for obj_1 in connector_1:
            for obj_2 in connector_2:

                user_frequency = min(obj_1.upper_frequency, obj_2.upper_frequency)
                user_frequency = min(user_frequency, normal_combo_input_form['frequency'].value())
                dc = normal_combo_input_form['frequency'].value()
                max_witc, min_witc = order_witc(obj_1.full_witc, obj_2.full_witc)
                # print "1: " + str(obj_1.calculated_standing_wave(user_frequency)) + "fre: " + str(user_frequency)
                # print "2: " + str(obj_2.calculated_standing_wave(user_frequency)) + "fre: " + str(user_frequency)
                standing_wave = max( obj_1.calculated_standing_wave(user_frequency),
                                     obj_2.calculated_standing_wave(user_frequency)
                                     )

                for cable_obj in cable:
                    loss_value = obj_1.calculated_loss_value(user_frequency) + obj_2.calculated_loss_value(user_frequency) +\
                                 cable_obj.calculated_loss_value(user_frequency)

                    combo_res = {'full_witc': max_witc +
                                              "-" + min_witc +
                                              "-" + normal_combo_input_form['cable_length'].value(),
                                 'a_content_type': obj_1.content_type.content,
                                 'a_polar_type': obj_1.polar_type.content,
                                 'a_install_type': obj_1.install_type.content,
                                 'a_outlook_type': obj_1.outlook_type.content,
                                 'b_content_type': obj_2.content_type.content,
                                 'b_polar_type': obj_2.polar_type.content,
                                 'b_install_type': obj_2.install_type.content,
                                 'b_outlook_type': obj_2.outlook_type.content,
                                 'frequency': dc,
                                 'loss_value': loss_value,
                                 'standing_wave': standing_wave
                                 }

                    normal_combo_cable_res.append(combo_res)

    paginator = Paginator(normal_combo_cable_res, RESULT_NUM_PER_PAGE)

    page = None
    if 'page' in request.POST:
        page = request.POST['page']

    try:
        normal_combo_cable_res = paginator.page(page)
    except PageNotAnInteger:
        normal_combo_cable_res = paginator.page(1)
    except EmptyPage:
        normal_combo_cable_res = paginator.page(paginator.num_pages)

    read_only = None

    if 'readonly' in request.POST:
        read_only = request.POST['readonly']

    if read_only:
        if normal_combo_cable_res:
            return render_to_response('admin_pages/normal_combo_cable_pages/normal_combo_cable_table_readonly.html', locals())
        else:
            return render_to_response('admin_pages/normal_combo_cable_pages/normal_combo_cable_table_readonly_empty.html', locals())

    return render_to_response("admin_pages/normal_combo_cable_pages/normal_combo_cable_table_readonly.html", locals())

    # except Exception, e:
    #     print str(e)
    #     return render_to_response("admin_pages/normal_combo_cable_pages/normal_combo_cable_table_readonly.html")
