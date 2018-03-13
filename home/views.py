from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from messenger.models import Message

# Create your views here.
def get_index(request):
    
    return render(request, "home/post_list.html")