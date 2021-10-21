from django.contrib import admin
from django.urls import path, include
from django.conf import settings

from . import views

urlpatterns = [
    path('',views.login, name='login'),
    path('display', views.display, name='display'),
    path('login',views.login, name='login'),
    path('signup',views.signup,name='signup'),
    path('admin',views.admin,name='admin'),
    path('leave',views.leave,name='leave'),
    path('leave_action',views.leave_action,name='leave_action'),
    path('clockout',views.clockout,name='clockout'),
    path('timesheet',views.timesheet,name='timesheet'),
]