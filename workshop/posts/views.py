# Create your views here.
from django.template import RequestContext
from django.shortcuts import render_to_response

from workshop.posts.models import Post

def all_posts(request):
    template = 'posts/all_posts.html'
    posts = Post.objects.all()
    ctx = { 'posts': posts }
    ctx = RequestContext(request, ctx)
    return render_to_response(template, ctx)

