from django.shortcuts import render,get_object_or_404
from.models import Post
from django.utils import timezone

# Create your views here.
def post_list(request):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_list.html', {'posts':posts})
