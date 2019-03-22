from django.contrib import admin

from django.urls import path, include
from .views import *


app_name = 'kumbi'

urlpatterns = [
    path('', home_view, name='home'),
    path('reg_hall/', register, name='registration'),

]
