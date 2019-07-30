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
        group = self.request.user

        # dailys_per_day = Daily.objects.filter(date=timezone.now) # 현재 날짜와 같은 daily 데이터가 있는지

        # use today's date for the calendar
        # d = get_date(self.request.GET.get('day', None))
        d = get_date(self.request.GET.get('month',None))
        # Instantiate our calendar class with today's year and date
        cal = Calendar(d.year, d.month)
        # html_cal = cal.formatmonth(withyear=True)
        html_cal = cal.formatmonth(withyear=True, group=group)

        # html_cal = html_cal.replace('<td','<td width="50"')
        #context['daily'] = dailys_per_day
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
       
        return context
    
def prev_month(d): # 이전 달 url return 
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month) 
    return month

def next_month(d): # 다음 달 url return
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month) 
    return month    

def get_date(req_month):
    if req_month:
        year, month = (int(x) for x in req_month.split('-'))
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
        plan = form.save(commit=False)
        plan.groupid = request.user.groupid 
        plan.save()
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
    plans = Event.objects.order_by('start_date') # 시간 오름차순 정렬
    return render(request, 'cal/total.html', {'plans': plans})


# Daily의 count up 함수
def count_up(request): # POST 방식으로 object를 받아와서 현재시간과 같은 object를 filter하고 DB에 저장
    if request.POST and form.is_valid():
        daily = Daily.objects.filter(date=timezone.now)
        if daily: # DB에 있으면 업데이트 
             daily = Daily.objects.filter(date=timezone.now)
        else:
            daily = Daily() # 없으면 
    form = EventForm(request.POST or None, instance=daily)

    daily = get_object_or_404(Daily, pk=pk) # 1 : 사료, 2 : 물, 3 : 간식
    daily.count = daily.count + 1 
    daily.save()
    return render(request, 'cal/calendar.html', {'daily': daily})