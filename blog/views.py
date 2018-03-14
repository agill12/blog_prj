from django.shortcuts import render,get_object_or_404,redirect
from django.contrib.auth.decorators import login_required
from blog.models import Post
from .forms import NewPostForm


# Create your views here.
def post_detail(request,id):
    item=get_object_or_404(Post,pk=id)
    item.read=True
    item.views+=1
    item.save()
    
    return render(request, "blog/post_detail.html",{'item':item})
    
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
    post_to_edit=get_object_or_404(Post,pk=id)
    if post_to_edit.author==request.user:
        if request.method=='POST':
            form=NewPostForm(request.POST,request.FILES,instance=post_to_edit)
            if form.is_valid():
               # post=form.save(commit=False)
                #post.author=request.user
                form.save()
                return redirect('home')
        form=NewPostForm(instance=post_to_edit)        
        return render(request, 'blog/edit_post.html',{'form':form})    
    return redirect('home')
        



    
    

    
    
    
