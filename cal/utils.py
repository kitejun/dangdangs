from datetime import datetime, timedelta
from calendar import HTMLCalendar, month_name, _localized_day
from .models import Event


class Calendar(HTMLCalendar):
   def __init__(self, year=None, month=None):
      self.year = year
      self.month = month
      super(Calendar, self).__init__()

   # formats a day as a td
   # filter events by day
   def formatday(self, day, events, group):
      events_per_day = events.filter(date__day=day)
      d = ''
      group = group

      for event in events_per_day:
         if event.groupid == group.groupid:  
            d += f'<li> {event.get_html_url}</li>' # {event.groupid_id}그룹 : {group.groupid} -> 현재 그룹, 일정 그룹 확인용

      if day != 0:
         if datetime.today().day == day and datetime.today().month == self.month and datetime.today().year == self.year:
            return f"<td><span class='today'>{day}</span><ul> {d} </ul></td>"
         else:
            return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>"
      return '<td></td>'

   # formats a week as a tr
   def formatweek(self, theweek, events, group):
      week = ''
      group = group
      for d, weekday in theweek:
         week += self.formatday(d, events, group)
      return f'<tr> {week} </tr>'


   def formatmonth(self, withyear=True, group=0):
      events = Event.objects.filter(date__year=self.year, date__month=self.month)

      group = group

      cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
      cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
      cal += f'{self.formatweekheader()}\n'
      for week in self.monthdays2calendar(self.year, self.month):
         cal += f'{self.formatweek(week, events, group)}\n'
      return cal
   
    # 캘린더 Month 헤더 
   def formatmonthname(self, theyear, month, withyear=True):
          
      month_name_kr = ["12월", "1월", "2월", "3월", "4월", "5월", "6월", "7월", "8월", "9월", "10월", "11월"]
      if withyear:
         s = '%s년 %s' % (theyear, month_name_kr[month % 12])
      else:
         s = '%s' % month_name_kr[month]
      return '<tr><th colspan="7" class="month">%s</th></tr>' %s

   # 캘린더 Week 헤더 (Return a weekday name as a table header.)
   def formatweekday(self, day):
 
      day_abbr = ["월", "화", "수", "목", "금", "토", "일"]
      
      return '<th class="%s">%s</th>' % (self.cssclasses_weekday_head[day], day_abbr[day])