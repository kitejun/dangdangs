from django.contrib import admin
from django.urls import path, include
import board.views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',board.views.board, name="board"),
    path('board/<int:board_id>/',board.views.detail,name='detail'),
    # path('board/new/', board.views.new, name='new'),
    path('board/create/', board.views.create, name='create'),

    path('board/update/<int:board_id>/', board.views.update, name='update'),
    path('board/delete/<int:board_id>/', board.views.delete, name='delete'),

     path('', include('cal.urls')), # 캘린더 urls
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)