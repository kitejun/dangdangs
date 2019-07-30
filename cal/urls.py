# cal/urls.py

from django.urls import path
from . import views

app_name = 'cal'
urlpatterns = [
    path('', views.CalendarView.as_view(), name='calendar'),
    path('event/new/', views.event, name='event_new'), # 일정 생성
    path('event/total/', views.total, name='event_total'), # 전체 일정
    path('event/edit/<int:event_id>', views.event, name='event_edit'), # 일정 수정
   
    path('event/detail/<int:event_id>', views.detail, name='event_detail'), # datail        
    path('event/delete/<int:event_id>', views.delete, name='event_delete'), # delete 

    path('daily', views.count_up, name='count'), # daily count
]