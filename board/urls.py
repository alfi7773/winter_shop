from django.urls import path
from . import views

urlpatterns = [
    path('detail/<int:id>/', views.detail, name='detail'),
    path('category/<int:id>', views.category, name='category'),
    path('cat/<int:id>', views.at_category, name='cat'),
    path('type/<int:id>', views.type, name='type'),
    path('catalogue/', views.catalogue, name='catalogue'),
    path('', views.main, name='base'),
    # path('main/', views.main2, name='main'),
    
]

