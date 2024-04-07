from django.urls import path
from . import views


app_name="home"
#start
urlpatterns = [
    path("",views.home,name="main")
]