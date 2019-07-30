from django.contrib import admin
from django.urls import path, include
<<<<<<< HEAD
=======
import board.views
>>>>>>> 1eb28f560adbbac798c6db725c646f0fb4d2a119
from django.conf import settings
from django.conf.urls.static import static
import board.views

import board.views
import cal.views
import accounts.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', board.views.home, name="home"),

    path('board/', include('board.urls')), # 게시판 urls
    path('calendar/', include('cal.urls')), # 캘린더 urls
<<<<<<< HEAD
    path('accounts/',include('accounts.urls')), # 로그인 urls 
=======
    path('accounts/',include('accounts.urls')), #계정기능 urls
    
>>>>>>> 1eb28f560adbbac798c6db725c646f0fb4d2a119
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)