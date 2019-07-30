from django.forms import ModelForm, DateInput
from cal.models import Event
<<<<<<< HEAD
from datetime import datetime
=======
>>>>>>> 1eb28f560adbbac798c6db725c646f0fb4d2a119

class EventForm(ModelForm):
  class Meta:
    model = Event
    # datetime-local is a HTML5 input type, format to make date time show on fields
    widgets = {
<<<<<<< HEAD
      'start_date': DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
      # 'update_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
    }
    fields = ['title','todo','context','start_date']
=======
      'start_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
      'end_time': DateInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
    }
    fields = '__all__'
>>>>>>> 1eb28f560adbbac798c6db725c646f0fb4d2a119

  def __init__(self, *args, **kwargs):
    super(EventForm, self).__init__(*args, **kwargs)
    # input_formats to parse HTML5 datetime-local input to datetime field
<<<<<<< HEAD
    self.fields['start_date'].input_formats = ('%Y-%m-%d',)
    # self.fields['update_time'].input_formats = ('%Y-%m-%dT%H:%M',)
=======
    self.fields['start_time'].input_formats = ('%Y-%m-%dT%H:%M',)
    self.fields['end_time'].input_formats = ('%Y-%m-%dT%H:%M',)
>>>>>>> 1eb28f560adbbac798c6db725c646f0fb4d2a119
