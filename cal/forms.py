from django.forms import ModelForm, DateInput
from cal.models import Event, Daily
from datetime import datetime

class EventForm(ModelForm):
  class Meta:
    model = Event
    # datetime-local is a HTML5 input type, format to make date time show on fields
    widgets = {
      'date': DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
      # 'update_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
    }
    fields = ['title','todo','context','date']

  def __init__(self, *args, **kwargs):
    super(EventForm, self).__init__(*args, **kwargs)
    # input_formats to parse HTML5 datetime-local input to datetime field
    self.fields['date'].input_formats = ('%Y-%m-%d',)
    # self.fields['update_time'].input_formats = ('%Y-%m-%dT%H:%M',)


class DailyForm(ModelForm):
  class Meta:
    model = Daily
    fields = ['saryo_count', 'water_count', 'gansic_count']

  def __init__(self, *args, **kwargs):
    super(DailyForm, self).__init__(*args, **kwargs)
   
   