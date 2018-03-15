from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from blog.models import Post
from django.utils import timezone

# Create your views here.
def get_index(request):
   
    posts = Post.objects.filter(created_date__lte=timezone.now()
                               ).order_by('-created_date')
    return render(request, "home/post_list.html",{'posts':posts})
    
    
 