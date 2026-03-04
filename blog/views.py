from django.shortcuts import render, redirect, get_object_or_404
from .models import  Post, Tag, Contacts,Comment
from django.contrib.auth.decorators import login_required
from .form import CommentForm, ContactForm
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
def article_detail(request,pk):
    post = get_object_or_404(Post, pk=pk)
    comment = Comment.objects.filter(post=pk)
    teg = Tag.objects.all()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('detail', pk=post.pk)
    else:
        form = CommentForm()
    context = {
        'post': post,
        'teg': teg,
        "form": form,
        "comment": comment

    }
    return render(request,'blog-single.html', context)

# @login_required
# def contact_page(request, name):
#     contacts = Contact.objects.filter(name__icontains=name)
#     context = {'contacts': contacts}
#     return render(request, 'contact.html', context)



def contact_page(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact')
    else:
        form = ContactForm()
    context = {
        'form': form
    }
    return render(request, 'contact.html', context)