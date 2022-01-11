from django.contrib import messages
from django.contrib.messages import constants
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.contrib import auth


def signup(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, 'signup.html')
    
    elif request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if (len(username.strip()) == 0 or len(email.strip()) == 0 or
            len(password.strip()) == 0):
            
            messages.add_message(
                request,
                constants.ERROR,
                'Fill all the fields.'
            )
            return redirect('/auth/signup')
        
        user = User.objects.filter(username = username)
        
        if user.exists():
            messages.add_message(
                request, 
                constants.ERROR,
                'This username is not available. Choose another one.'
            )
            return redirect('/auth/signup')

        try:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password
            )
            user.save()
            messages.add_message(
                request,
                constants.SUCCESS,
                'The new user info has been successfully saved.')
            return redirect('/auth/login')
        
        except:
            messages.add_message(
                request, 
                constants.ERROR,
                'Internal system error.'
            )
            return redirect('/auth/signup')


def login(request):
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/')
        return render(request, 'login.html')
    
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = auth.authenticate(username=username,
                                 password=password)
        
        if not user:
            messages.add_message(
                request,
                constants.ERROR,
                'Authentication failed.'
            )
            return redirect('/auth/login')
        
        else:
            auth.login(request, user)
            return redirect('/')
                
        
        return HttpResponse(f'{username}')


############################
# 4TH VERSION FOR signup ###
# returning info from form #
############################

# def signup(request):
#     if request.method == 'GET':
#         return render(request, 'signup.html')
#     elif request.method == 'POST':
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         return HttpResponse(f'{username}, {email}, {password}')

############################
# THIRD VERSION FOR signup #
# methods and print(POST) ##
############################

# def signup(request):
#     if request.method == 'GET':
#         return render(request, 'signup.html')
#     elif request.method == 'POST':
#         print('\n\n', request.POST, '\n\n')
#         return HttpResponse('POSTED!')

###################################
# SECOND VERSION (RENDERING HTML) #
###################################

# def signup(request):
#     return render(request, 'signup.html')


# def login(request):
#     return render(request, 'login.html')


################################
# FIRST VERSION (WITH NO HTML) #
################################

# def signup(request):
#     return HttpResponse('SIGNUP PAGE')


# def login(request):
#     return HttpResponse('LOGIN PAGE')