from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render
from log.connector_logging import log

def user_login(request):
    """

    :param request:
    :return:
    """
    user_name = request.POST['username']
    passwd = request.POST['password']
    user = authenticate(username=user_name, password=passwd)
    if user is not None:
        if user.is_active:
            login(request, user)
            log.info("user " + user_name + "login")
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
    log.info("user " + request.user.username + " logout")
    logout(request)

    # redirect to another page
    return render(request, 'page_example/admin_login.html')

