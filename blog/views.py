from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from blog.models import Post


# Create your views here.
def post_detail(request,id):
    item=get_object_or_404(Post,pk=id)
    item.read=True
    item.save()
    return render(request, "blog/post_detail.html",{'item':item})
    
    
   