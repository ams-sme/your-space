from django.db import models
from django.contrib.auth import get_user_model

from common.models import TimeStampModel

User = get_user_model()

class Post(TimeStampModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    image = models.ImageField(upload_to='post_images/', blank=True, null=True)
    likers = models.ManyToManyField(User, related_name='liked_posts')

    
    def __str__(self):
        return f"{self.user.username} - {self.created_date}"
    
class Comment(TimeStampModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    
    def __str__(self):
        return f"{self.user.username} - {self.created_date}"
