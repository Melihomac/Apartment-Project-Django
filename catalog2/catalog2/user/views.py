import imp
import django
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)
            messages.add_message(request, messages.SUCCESS, 'Login Success')
            return redirect('index')
        else:
            messages.add_message(request, messages.ERROR, 'Login Error')
            return redirect('login')
    else:
        return render(request, 'user/login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        repassword = request.POST['repassword']

        if password == repassword:
            if User.objects.filter(username = username).exists():
                messages.add_message(request, messages.WARNING, 'This username is already taken')
                return redirect('register')
            else:
                if User.objects.filter(email = email).exists():
                    messages.add_message(request, messages.WARNING, 'This email is already taken')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username = username, password = password, email = email)
                    user.save()
                    messages.add_message(request, messages.SUCCESS, 'Its Done !')
                    return redirect('login')

        else:
            messages.add_message(request, messages.ERROR('Passwords are not same !'))
            return redirect('register')
    else:
        return render(request, 'user/register.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.add_message(request, messages.SUCCESS, 'Logout Success')
        return redirect('index')
    else:
        return render(request, 'user/logout.html')
