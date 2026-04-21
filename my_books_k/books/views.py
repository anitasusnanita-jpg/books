# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect

from .models import Book, Category

# Create your views here.
def home(request):
    books = Book.objects.filter(status=Book.ACTIVE).order_by('-created_at')
    context = {
        'books': books
    }
    return render(request, 'books/home.html', context)

def detail(request, id):
    book = get_object_or_404(Book, id=detail_books , status=Book.ACTIVE)

    context = {
        'book': book,
    }  
    return render (request, 'books/detail.html',context)