from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('add/', views.add, name="add"),
    path('address/', views.address, name="address"),
    path('delete/<int:id>', views.delete, name='delete'),
    path('update/<int:id>', views.update, name='update'),
    path('uprec/<int:id>', views.uprec, name='uprec')
  
    
    
    
    
]