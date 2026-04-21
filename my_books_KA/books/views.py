# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect

from .models import Book, Category

# Create your views here.
def home(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'books/home.html', context)

def detail(request, id):
    book = get_object_or_404(Book, id=id)

    context = {
        'book': book,
    }  
    return render (request, 'books/detail.html', context)