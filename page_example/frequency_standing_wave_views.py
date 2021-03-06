from django.contrib.auth.decorators import login_required
from models import Category, Polar, FrequencyPoint, FrequencyStandingWave
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render_to_response, render
from django.views.decorators.csrf import csrf_exempt


@login_required
def admin_frequency_standing_wave(request):

    category = Category.objects.all()
    polar = Polar.objects.all()

    return render(request, 'admin_pages/product_others_frequency_standing_wave.html', locals())


@login_required
def admin_filter_frequency_standing_wave(request):

    request_form = request.POST

    category = request_form.get('category_type')
    polar = request_form.get('polar_type')

    if not category or not polar:
        return HttpResponse(-1)

    category_obj = Category.objects.filter(content=category)
    polar_obj = Polar.objects.filter(content=polar)
    frequency_objs = FrequencyPoint.objects.all()

    frequency_standing_wave_res = []
    for obj in frequency_objs:
        real_res = FrequencyStandingWave.objects.filter(category_type=category_obj,
                                                        polar_type=polar_obj,
                                                        frequency=obj).first()

        if real_res:
            tmp = {
                'frequency': obj.frequency,
                'standing_wave': real_res.standing_wave,
            }
        else:
            tmp = {
                'frequency': obj.frequency,
                'standing_wave': '',
            }

        frequency_standing_wave_res.append(tmp)

    category_content = category
    polar_content = polar

    return render(request, 'admin_pages/frequency_standing_wave_pages/frequency_standing_wave_table.html', locals())


@login_required
@csrf_exempt
def admin_insert_frequency_standing_wave(request):
    """

    :param request:
    :return:
    """
    print request.POST
    try:
        category_content = request.POST.get('category')
        if not category_content:
            return HttpResponse(-1)

        category_obj = Category.objects.get(content=category_content)

        polar_content = request.POST.get('polar')
        if not polar_content:
            return HttpResponse(-1)

        polar_obj = Polar.objects.get(content=polar_content)

        frequency = request.POST.get('frequency')

        if not frequency:
            return HttpResponse(-1)

        frequency_obj = FrequencyPoint.objects.get(frequency=frequency)

        standing_wave = request.POST.get('standing_wave')

        obj = FrequencyStandingWave.objects.filter(category_type=category_obj,
                                                   polar_type=polar_obj,
                                                   frequency=frequency_obj)

        if obj:
            obj.update(standing_wave=standing_wave)
        else:
            FrequencyStandingWave.objects.create(category_type=category_obj,
                                                 polar_type=polar_obj,
                                                 frequency=frequency_obj,
                                                 standing_wave=standing_wave)
        return HttpResponse(0)

    except Exception,e:

        return HttpResponse(-1)






