from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('board/', include('board.urls')), # 게시판 urls
    path('cal', include('cal.urls')), # 캘린더 urls
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)