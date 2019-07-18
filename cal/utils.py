from datetime import datetime, timedelta
from calendar import HTMLCalendar, month_name
from .models import Event

class Calendar(HTMLCalendar):
   def __init__(self, year=None, month=None):
      self.year = year
      self.month = month
      super(Calendar, self).__init__()

   # formats a day as a td
   # filter events by day
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

      cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
      cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
      cal += f'{self.formatweekheader()}\n'
      for week in self.monthdays2calendar(self.year, self.month):
         cal += f'{self.formatweek(week, events)}\n'
      return cal
   
   
    # 캘린더 이전, 다음 달로 넘어가는 < > 표시 
   def formatmonthname(self, theyear, month, withyear=True):

      if withyear:
         s = '%s %s' % (month_name[month], theyear)
      else:
         s = '%s' % month_name[month]
      return '<tr><th colspan="7" class="month" color="#D7B8A5">%s</th></tr>' %s