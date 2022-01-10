from django.shortcuts import render
from django.http import HttpResponse


def signup(request):
    return render(request, 'signup.html')


def login(request):
    return HttpResponse('LOGIN PAGE')




################################
# FIRST VERSION (WITH NO HTML) #
################################

# def signup(request):
#     return HttpResponse('SIGNUP PAGE')


# def login(request):
#     return HttpResponse('LOGIN PAGE')