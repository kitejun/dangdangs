from django.urls import path
from . import views

urlpatterns = [
    path('', views.board, name="board"),
    path('detail/<int:board_id>/', views.detail, name="detail"),
    path('new/', views.new, name='new'),
    
    path('update/<int:board_id>/', views.update, name='update'),
    path('delete/<int:board_id>/', views.delete, name='delete'),
]