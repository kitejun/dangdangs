from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

import board.views
import cal.views
import accounts.views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', board.views.home, name="home"),

    path('share/',board.views.share, name="share"),
    
    path('board/', include('board.urls')), # 게시판 urls
    path('calendar/', include('cal.urls')), # 캘린더 urls
    path('accounts/',include('accounts.urls')), # 로그인 urls 

    path('like_link/',board.views.like_link, name='like_link') #인기글 링크
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)