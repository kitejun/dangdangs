from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib.auth import get_user_model
from django.contrib import messages

User = get_user_model()
from .models import Group
import random
# Create your views here.


def signup(request):
    if request.method == 'POST':
        if request.POST['password1'] == request.POST['password2']:
            groupid_copy=request.POST['groupid']
 
            ba = request.POST.get("groupjudge", None)
            if ba is None: # 가족들이 가입하지 않은 신규회원이면
                ra = random.randint(1,1000000001)
                group = Group()
                group.groupid= ra
                group.save()
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'], groupid=ra)
            else:   #이미 가입한 가족이 있다. 
                event = Group.objects.filter(groupid=groupid_copy).first() 
                if event: #가입한 가족코드가 존재하면 
                    user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'],groupid=request.POST['groupid'])
                    return redirect('home')
                else:
                    messages.warning(request,'입력하신 가족코드에 해당하는 가족이 없습니다.')
                    return render(request, 'accounts/signup.html')

            return redirect('home')
       
        messages.warning(request,'비밀번호가 일치하지 않습니다.')



    return render(request, 'accounts/signup.html')


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

def mypage(request):
    return render(request, 'accounts/mypage.html')