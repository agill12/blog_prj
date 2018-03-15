from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from blog.models import Post
from .forms import NewPostForm
from django.utils import timezone


# Create your views here.
def post_detail(request,id):
    post=get_object_or_404(Post,pk=id)
    post.read=True
    post.views+=1
    post.save()
    
    return render(request, "blog/post_detail.html",{'post':post})
    
def new_post(request):
    if request.method=='POST':
        form=NewPostForm(request.POST,request.FILES)
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.save()
            return redirect('home')
    else:
        form=NewPostForm()
    return render(request, 'blog/new_post.html',{'form':form})
    
def edit_panel(request):
    
    return render(request,'blog/edit_panel.html')

def edit_post(request,id):
    post=get_object_or_404(Post,pk=id)
    if post.author==request.user:
        if request.method=='POST':
            form=NewPostForm(request.POST,request.FILES,instance=post)
            if form.is_valid():
                post.published_date=timezone.now()
               # post=form.save(commit=False)
                #post.author=request.user
                form.save()
                return redirect('home')
        form=NewPostForm(instance=post)        
        return render(request, 'blog/new_post.html',{'form':form})    
    return redirect('home')
        
def delete_post(request, id):
    post = get_object_or_404(Post, pk=id)
    post.delete()
    return redirect('home')


    
    

    
    
    
