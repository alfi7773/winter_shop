from django.urls import path
from . import views

urlpatterns = [
    path('detail/<int:id>/', views.detail, name='detail'),
    path('', views.main, name='base'),
    # path('main/', views.main2, name='main'),
    
]

