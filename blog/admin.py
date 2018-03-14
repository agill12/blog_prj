from django.contrib import admin
from blog.models import Post
# Register your models here.
admin.site.register(Post)



# class PostAdmin(admin.ModelAdmin):    
#         if not request.user.is_superuser and request.user.has_perm('items.read_item'):
#             return [f.name for f in self.model._meta.fields]        
#         return super(ItemAdmin, self).get_readonly_fields(
#             request, obj=obj
#         )

# admin.site.register(Item, ItemAdmin)