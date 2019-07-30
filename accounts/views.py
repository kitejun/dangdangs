from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import get_user_model
<<<<<<< HEAD
import random
from .models import Group
=======
>>>>>>> 1eb28f560adbbac798c6db725c646f0fb4d2a119
User = get_user_model()
# Create your views here.


def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
<<<<<<< HEAD
            
            user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'],groupid=request.POST['groupid'])

            group = Group()
            group.groupid= user.groupid
            group.save()
            auth.login(request, user)
            return redirect('home')
    return render(request, 'accounts/signup.html')


=======
            user = User.objects.create_user( username=request.POST['username'], password=request.POST['password1'],groupid= request.POST['groupid'])
            auth.login(request, user)
            return redirect('')
    return render(request, 'accounts/signup.html')




>>>>>>> 1eb28f560adbbac798c6db725c646f0fb4d2a119
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            return render(request, 'accounts/login.html', {'error': 'username or password is incorrect.'})
    else:
        return render(request, 'accounts/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    return render(request, 'accounts/signup.html')