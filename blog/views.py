from django.shortcuts import render, redirect, get_object_or_404
from .models import Author, Post, Tag, About

def home_page(request):
    post = Post.objects.all().order_by('-id')
    context = {
        'posts': post
    }
    return render(request, 'index.html', context)

def blog(request):
    blog = Post.objects.all().order_by('-id')
    context = {'blogs': blog}
    return render(request, 'blog.html', context)
def  about(request):
    about = Post.objects.all().order_by('-id')
    context = {'abouts': about}
    return render(request, 'about.html', context)

def contact(request):
    return render(request, 'contact.html')