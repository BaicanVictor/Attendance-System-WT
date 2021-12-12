from django.urls import path
from .views import LoginPage, logout_view, register

urlpatterns = [
    path('login/', LoginPage.as_view(), name='login'),
    path('logout/', logout_view, name='logout'),
    path('register/', register, name='register'),
]
