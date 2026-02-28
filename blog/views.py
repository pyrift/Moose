from django.shortcuts import render, redirect, get_object_or_404
from .models import Author, Post, Tag, About,Contact
from django.contrib.auth.decorators import login_required
def home_page(request):
    post = Post.objects.all().order_by('-id')
    context = {
        'posts': post
    }
    return render(request, 'index.html', context)

def blog_page(request):
    blog = Post.objects.all().order_by('-id')
    context = {'blogs': blog}
    return render(request, 'blog.html', context)
def about_page(request):
    about = Post.objects.all().order_by('-id')
    context = {'abouts': about}
    return render(request, 'about.html', context)

@login_required
def contact_page(request, name):
    contacts = Contact.objects.filter(name__icontains=name)
    context = {'contacts': contacts}
    return render(request, 'contact.html', context)
