from django.conf.urls import url

from .views import *

urlpatterns = [
    url(r'^post_detail/(\d+)', post_detail, name="post_detail"),
    url(r'^new_post/', new_post, name="new_post"),
    url(r'^edit_panel/', edit_panel, name="edit_panel"),
    url(r'^edit_post/(\d+)', edit_post, name="edit_post"),
    url(r'delete/(\d+)$', delete_post, name="delete"),

]