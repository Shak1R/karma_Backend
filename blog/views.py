from django.shortcuts import render
from .models import Post


# Create your views here.
def post_index(request):
    return render(request, 'blog.html', {'posts':  Post.objects.all()})

