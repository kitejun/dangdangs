from datetime import datetime, timedelta
<<<<<<< HEAD
from calendar import HTMLCalendar, month_name, _localized_day
from .models import Event


=======
from calendar import HTMLCalendar, month_name
from .models import Event

>>>>>>> 1eb28f560adbbac798c6db725c646f0fb4d2a119
class Calendar(HTMLCalendar):
   def __init__(self, year=None, month=None):
      self.year = year
      self.month = month
      super(Calendar, self).__init__()

   # formats a day as a td
   # filter events by day
<<<<<<< HEAD
   def formatday(self, day, events, group):
      events_per_day = events.filter(start_date__day=day)
      d = ''
      img = ''
      group = group

      for event in events_per_day:
         if event.groupid == group.groupid:
            if event.todo == "병원":
               img += f'<img src="/static/img/hospital.png" alt="병원">'
            elif event.todo == "산책":
               img += f'<img src="/static/img/walk.png" alt="산책">'       
            elif event.todo == "목욕":
               img += f'<img src="/static/img/bubble.png" alt="목욕">'    
            d += f'<li> {event.get_html_url} </li>'


      if day != 0:
         if datetime.today().day == day and datetime.today().month == self.month and datetime.today().year == self.year:
            return f"<td><span class='today'>{day}</span>{img}<ul> {d} </ul></td>"
         else:
            return f"<td><span class='date'>{day}</span>{img}<ul> {d} </ul></td>"
      return '<td></td>'

   # formats a week as a tr
   def formatweek(self, theweek, events, group):
      week = ''
      group = group
      for d, weekday in theweek:
         week += self.formatday(d, events, group)
      return f'<tr> {week} </tr>'


   def formatmonth(self, withyear=True, group=0):
      events = Event.objects.filter(start_date__year=self.year, start_date__month=self.month)

      group = group
=======
   def formatday(self, day, events):
      events_per_day = events.filter(start_time__day=day)
      d = ''
      for event in events_per_day:
         d += f'<li> {event.get_html_url} </li>'

      if day != 0:
         return f"<td><span class='date'>{day}</span><ul> {d} </ul></td>"
      return '<td></td>'

   # formats a week as a tr
   def formatweek(self, theweek, events):
      week = ''
      for d, weekday in theweek:
         week += self.formatday(d, events)
      return f'<tr> {week} </tr>'


   def formatmonth(self, withyear=True):
      events = Event.objects.filter(start_time__year=self.year, start_time__month=self.month)
>>>>>>> 1eb28f560adbbac798c6db725c646f0fb4d2a119

      cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
      cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
      cal += f'{self.formatweekheader()}\n'
      for week in self.monthdays2calendar(self.year, self.month):
<<<<<<< HEAD
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
=======
         cal += f'{self.formatweek(week, events)}\n'
      return cal
   
   
    # 캘린더 이전, 다음 달로 넘어가는 < > 표시 
   def formatmonthname(self, theyear, month, withyear=True):

      if withyear:
         s = '%s %s' % (month_name[month], theyear)
      else:
         s = '%s' % month_name[month]
      return '<tr><th colspan="7" class="month" color="#D7B8A5">%s</th></tr>' %s
>>>>>>> 1eb28f560adbbac798c6db725c646f0fb4d2a119
