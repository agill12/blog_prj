from django.db import models
from django.utils import timezone


class Post(models.Model):
    """
    Here we'll define our Post model
    """

    # author is linked to a registered
    # user in the 'auth_user' table.
    author = models.ForeignKey('auth.User', blank=False, related_name="posts_made")
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    published_date = models.DateTimeField(blank=True, null=True)
    views = models.IntegerField(default=0)
    tag = models.CharField(max_length=30, blank=True, null=True)
    image = models.ImageField(upload_to="images", blank=True, null=True)
   
    # class Meta:
    #     ordering = ['-created_date',]
    #     # permissions = (
    #     #     ('edit_item','Can edit item'),
    #     # )

        
    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title