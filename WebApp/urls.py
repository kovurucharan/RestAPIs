from django.contrib import admin
from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [
    path('home/',views.Home),
    path('rapi/',views.EmpList.as_view()),
    path('detail/',views.EmployeeDetail.as_view()),
    path('detail/<int:pk>/',views.EmployeeDetail.as_view()),

]
