from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from blog.forms import PostCreateForm
from blog.models import Post


posts = Post.objects.all()


def index(request):
    context_data = {
        "posts": posts,
        "title": "Home",
        'range': range(10-len(posts)),
    }
    return render(request, "index.html", context_data)


def post_add(request):
    if request.method == "POST":
        posts.create(
            title=request.POST['title'],
            about=request.POST['about'],
            image=request.FILES['file[]'],
            published_date=timezone.now()
        )
        return HttpResponseRedirect('/')
    form = PostCreateForm()
    context_data = {
        "title": "Home",
        'form': form
    }
    return render(request, 'post.html', context_data)


def get_post(request, post_id):
    myobject = get_object_or_404(Post, pk=post_id)
    context_data = {
        "post": myobject,
    }
    return render(request, 'one_post.html', context_data)
