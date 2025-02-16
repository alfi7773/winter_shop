from django.urls import path
from . import views

urlpatterns = [
    path('detail/<int:id>/', views.detail, name='detail'),
    path('category/<int:id>', views.category, name='category'),
    path('type/<int:id>', views.type, name='type'),
    path('', views.main, name='base'),
    # path('main/', views.main2, name='main'),
    
]

