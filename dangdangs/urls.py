from django.contrib import admin
<<<<<<< Updated upstream
from django.urls import path
import board.views
from django.conf import settings
from django.conf.urls.static import static
=======
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

import board.views
import cal.views
import accounts.views
>>>>>>> Stashed changes

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',board.views.board, name="board"),
    path('board/<int:board_id>/',board.views.detail,name='detail'),
    # path('board/new/', board.views.new, name='new'),
    path('board/create/', board.views.create, name='create'),

<<<<<<< Updated upstream
    path('board/update/<int:board_id>/', board.views.update, name='update'),
    path('board/delete/<int:board_id>/', board.views.delete, name='delete'),
    
=======
    path('board/', include('board.urls')), # 게시판 urls
    path('calendar/', include('cal.urls')), # 캘린더 urls
    path('accounts/',include('accounts.urls')), # 로그인 urls 
>>>>>>> Stashed changes
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)