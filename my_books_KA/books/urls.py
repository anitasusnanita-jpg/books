from django.contrib import admin
from django.urls import path
from .views import home, detail

urlpatterns = [
    path('', home, name='home'),
    path('detail_book/<int:id>/', detail, name='detail_book'),
]