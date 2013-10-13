from django.template import RequestContext
from django.contrib.auth.models import User
from django.shortcuts import render_to_response

def home(request):
    template = 'home.html'
    users = User.objects.all()
    ctx = { 'users': users }
    ctx = RequestContext(request, ctx)
    return render_to_response(template, ctx)
