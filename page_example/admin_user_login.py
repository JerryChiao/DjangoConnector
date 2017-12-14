from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render
from django.utils.translation import ugettext as _

def user_login(request):
    """

    :param request:
    :return:
    """
    user_name = request.POST['username']
    passwd = request.POST['password']
    print user_name, passwd
    user = authenticate(username=user_name, password=passwd)
    if user is not None:
        if user.is_active:
            login(request, user)
            return HttpResponse('1')
        else:
            return HttpResponse('0')

    else:
        return HttpResponse('-1')


def user_logout(request):
    """

    :param request:
    :return:
    """
    logout(request)
    print "logout"
    # redirect to another page
    return render(request, 'page_example/admin_login.html')

