from django.urls import path
from . import views
  
urlpatterns = [
        path('signup/', views.signup, name='signup'),
        path('login/', views.login, name='login'),
        path('logout/', views.logout, name='logout'),    
        path('mypage/', views.mypage, name='mypage'),
        path('info/', views.info, name='info'),
        path('map/',views.map, name='map'),
        path('doginfo/',views.doginfo,name='doginfo'),

        path('people/', views.people, name='people'),
]