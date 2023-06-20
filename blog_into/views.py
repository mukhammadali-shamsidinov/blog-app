from django.shortcuts import render
from .models import Blog
# Create your views here.
def blog_list_views(request):
    blog = Blog.objects.all()
    context = {
        "blogs":blog
    }

    return render(request,"index.html",context=context)

def details_list_views(request,id):
    blog = Blog.objects.get(id = id)
    context = {
        "blog":blog
    }

    return render(request,"details.html",context=context)