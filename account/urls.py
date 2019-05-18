from django.urls import path

from account import views

urlpatterns = [
    path('register/', views.UserCreate.as_view(), name='account-create'),
]