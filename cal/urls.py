# cal/urls.py

from django.conf.urls import url
from . import views

app_name = 'cal'
urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^calendar/$', views.CalendarView.as_view(), name='calendar'), # 캘린더 
    url(r'^calendar/event/new/$', views.CalendarView.event, name='event_new'), # 일정 생성
    url(r'^calendar/event/total/$', views.total, name='event_total'), # 전체 일정
    url(r'^calendar/event/edit/(?P<event_id>\d+)/$', views.CalendarView.event, name='event_edit'), # 일정 수정
    
    # url(r'^event/new/$', views.event, name='event_new'),
    # url(r'^event/edit/(?P<event_id>\d+)/$', views.event, name='event_edit'),

    url(r'^calendar/event/detail/(?P<event_id>\d+)/$', views.detail, name='event_detail'), # datail        
    url(r'^calendar/event/delete/(?P<event_id>\d+)/$', views.delete, name='event_delete'), # delete 
]