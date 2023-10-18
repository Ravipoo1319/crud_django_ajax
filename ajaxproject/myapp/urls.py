from django.urls import path
from . import views

urlpatterns = [
    path("",views.home,name="home"),
    path("save/",views.saveData,name="save"),
    path("delete/",views.delete_data,name="delete"),
    path("update/",views.update_data,name="update"),
]