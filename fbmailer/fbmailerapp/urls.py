from django.urls import path
from . import views

urlpatterns = [
    path('', views.code),
    path('mailer/', views.msg)
]
