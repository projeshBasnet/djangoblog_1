from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    dateposted = models.DateTimeField(default= timezone.now)
    user = models.ForeignKey(User,on_delete= models.CASCADE)

    def __repr__(self):
        return f'Post("{self.title}", "{self.user}")'

    def get_absolute_url(self):
        return reverse('detail-post', kwargs={'pk':self.pk})    
