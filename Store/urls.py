from django.urls import path

from Store.views import index,get_user_feedback
from . import models

app_name = 'Store'

urlpatterns = [
    path('',index,name='index'),
    path('feedback',get_user_feedback,name='feedback'),

]