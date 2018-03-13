from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^post_detail/(\d+)', post_detail, name="post_detail"),
   
    
]