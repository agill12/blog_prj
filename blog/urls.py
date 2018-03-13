from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^post_detail/(\d+)', post_detail, name="post_detail"),
    url(r'^new_post/', new_post, name="new_post"),
    
   
    
]