from django.contrib import admin
from django.urls import path
from .views import home, detail

urlpatterns = [
    path('', home, name='home'),
    path('detail_my_book_k/<int:id>/', detail, name='detail_my_book_k'),
]