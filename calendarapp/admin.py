from django.contrib import admin
<<<<<<< Updated upstream:calendarapp/admin.py

# Register your models here.
=======
from cal.models import Event, Daily

# Register your models here.

admin.site.register(Event)
admin.site.register(Daily)
>>>>>>> Stashed changes:cal/admin.py
