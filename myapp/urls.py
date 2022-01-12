from django.urls import path
from .views import home,tabledelete,tableupdate,tablecreate

urlpatterns = [
    path('home/',home,name="home"),
    path('home/add/',tablecreate,name="create"),
    path('home/update/<int:pk>',tableupdate,name="update"),
    path('home/delete/<int:pk>',tabledelete,name="delete"),
]
