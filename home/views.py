from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from blog.models import Post


# Create your views here.
def get_index(request):
    
    return render(request, "home/post_list.html")
    
    
 