from django.urls import path
from . import views
app_name = 'get_video'

urlpatterns = [
    path('',views.index,name = 'index')
]