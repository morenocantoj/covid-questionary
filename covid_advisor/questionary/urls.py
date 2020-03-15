from django.urls import path
from rest_framework import routers

from . import views

urlpatterns = [
    path('questionaries', views.QuestionaryList.as_view())
]
