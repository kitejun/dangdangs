from django.contrib import admin
from django.urls import path, include
import board.views
from django.conf import settings
from django.conf.urls.static import static
import board.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', board.views.home, name="home"),

    path('board/', include('board.urls')), # 게시판 urls
    path('calendar/', include('cal.urls')), # 캘린더 urls
    path('accounts/',include('accounts.urls')), #계정기능 urls
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)