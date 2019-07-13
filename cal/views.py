# cal/views.py

from datetime import datetime, timedelta, date
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from django.utils.safestring import mark_safe

import calendar

from .models import *
from .utils import Calendar
from .forms import *

def index(request):
    return HttpResponse('hello')

class CalendarView(generic.ListView):
    model = Event
    template_name = 'cal/calendar.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        # use today's date for the calendar
        # d = get_date(self.request.GET.get('day', None))
        d = get_date(self.request.GET.get('month',None))
        # Instantiate our calendar class with today's year and date
        cal = Calendar(d.year, d.month)

        # Call the formatmonth method, which returns our calendar as a table
        html_cal = cal.formatmonth(withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
       
        return context
 
    def event(request, event_id=None): # 일정 추가
        instance = Event()
        if event_id:
            instance = get_object_or_404(Event, pk=event_id)
        else:
            instance = Event()
    
        form = EventForm(request.POST or None, instance=instance)

        if request.POST and form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('cal:calendar'))
        return render(request, 'cal/event.html', {'form': form})
        # return render(request, 'cal/detail.html', {'instance' : instance})
    
def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month' + str(prev_month.year) + '-' + str(prev_month.month)
    return month

def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month    

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()


def event(request, event_id=None): # 일정 추가 & 수정
    instance = Event()
    if event_id:
        instance = get_object_or_404(Event, pk=event_id)
    else:
        instance = Event()
    
    form = EventForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse('cal:calendar'))
    return render(request, 'cal/event.html', {'form': form})

# 일정을 삭제하는 함수
def delete(request, event_id=None): 
    plan = get_object_or_404(Event, pk=event_id)
    plan.delete()

    return HttpResponseRedirect(reverse('cal:calendar'))

# 해당 날짜의 일정을 불러오는 함수
def detail(request, event_id=None):
    plan = Event()
    plan = get_object_or_404(Event, pk=event_id)

    return render(request, 'cal/detail.html', {'plan':plan })

# 전체 일정을 불러오는 함수
def total(request):
    plans = Event.objects.order_by('start_time') # 시간 오름차순 정렬
    return render(request, 'cal/total.html',{'plans': plans})