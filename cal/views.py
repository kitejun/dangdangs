# cal/views.py

from datetime import datetime, timedelta, date
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.contrib import messages
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

        # d = get_date(self.request.GET.get('day', None))
        d = get_date(self.request.GET.get('month',None))
        cal = Calendar(d.year, d.month)
        html_cal = cal.formatmonth(withyear=True, group=group)
        # html_cal = html_cal.replace('<td','<td width="50"')
    
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        context['daily'] = daily(self.request)
       
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
    
    plans = Event.objects.filter(groupid=request.user.groupid).order_by('date')
    # 해당 그룹 & 시간 오름차순 정렬
    return render(request, 'cal/total.html', {'plans': plans})

# 저장된 daily 값들을 불러오는 함수
def daily(request): 

    daily = Daily.objects.filter(date=timezone.now(), groupid=request.user.groupid).first() # 현재 날짜와 같은 오브젝트
    if daily:
        instance = daily
    else: # 해당 오브젝트가 없으면 생성
        instance = Daily()
        instance.groupid = request.user.groupid
        instance.save()

    form = DailyForm(request.POST or None, instance=instance)

    return form


# daily를 저장하는 함수
def daily_count(request):
    
    daily = Daily.objects.filter(date=timezone.now(), groupid=request.user.groupid).first() # 현재 날짜와 같은 오브젝트

    form = DailyForm(request.POST or None, instance=daily)
    
    if request.POST and form.is_valid(): # 제출시 form 내용 DB에 저장
        daily = form.save(commit=False)
        daily.groupid = request.user.groupid 
        daily.save()
        messages.warning(request,'저장되었습니다!')

    return HttpResponseRedirect(reverse('cal:calendar'))