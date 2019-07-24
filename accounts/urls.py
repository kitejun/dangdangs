from django.urls import path
from . import views

urlpatterns = [
    path('signup/',views.signup,name='signup'), #회원가입시
    path('login/',views.login,name='login'),    #로그인시
    path('logout/', views.logout, name='logout'), #로그아웃시


]