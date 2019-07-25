# cal/urls.py

from django.urls import path
from . import views

app_name = 'cal'
urlpatterns = [
    path('calendar/', views.CalendarView.as_view(), name='calendar'),
    path('calendar/event/new/', views.CalendarView.event, name='event_new'), # 일정 생성
    path('calendar/event/total/', views.total, name='event_total'), # 전체 일정
    path('calendar/event/edit/<int:event_id>', views.CalendarView.event, name='event_edit'), # 일정 수정
   
    path('calendar/event/detail/<int:event_id>', views.detail, name='event_detail'), # datail        
    path('calendar/event/delete/<int:event_id>', views.delete, name='event_delete'), # delete 
]