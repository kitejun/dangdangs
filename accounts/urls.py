from django.urls import path
from . import views
<<<<<<< HEAD
  
urlpatterns = [
        path('signup/', views.signup, name='signup'),
        path('login/', views.login, name='login'),
        path('logout/', views.logout, name='logout'),    
=======

urlpatterns = [
    path('signup/',views.signup,name='signup'), #회원가입시
    path('login/',views.login,name='login'),    #로그인시
    path('logout/', views.logout, name='logout'), #로그아웃시


>>>>>>> 1eb28f560adbbac798c6db725c646f0fb4d2a119
]