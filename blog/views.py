from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from blog.models import Post
from .forms import NewPostForm


# Create your views here.
def post_detail(request,id):
    item=get_object_or_404(Post,pk=id)
    item.read=True
    item.save()
    return render(request, "blog/post_detail.html",{'item':item})
    
def new_post(request):
    if request.method=='POST':
        form=NewPostForm(request.POST)
        if form.is_valid():
            post=form.save(commit=False)
            post.sender=request.user
            post.save()
            return redirect('home')
    else:
        form=NewPostForm()
    return render(request, 'blog/new_post.html',{'form':form})
    
 


    
    
    
   