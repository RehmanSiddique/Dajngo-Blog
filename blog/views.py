from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.

def home(request):
    posts=Post.objects.all()
    

    context = {
        "posts": posts
    }
    return render(request,'blog/home.html',context)
def about(request):
    return render(request,'blog/about.html')
def contact(request):
    return render(request,'blog/contact.html')
def post_detail(request,id):
    post=get_object_or_404(Post, id=id)
    return render(request, 'blog/post_details.html', {"post":post})