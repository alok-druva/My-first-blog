from django.db import models
from django.utils import timezone


# Create your models here.

class Post(models.Model):
    author=models.ForeignKey('auth.user')
    title=models.TextField(max_length=20,blank=False,null=False)
    text=models.TextField()
    created_date=models.DateTimeField(default=timezone.now)
    published_date=models.DateTimeField(blank=False,null=False)

    def publish(self):
        self.published_date=timezone.now()
        self.save()
        '''You should save the updated field within the model method if you cannot expect the caller to save
        the entire instance at a later point'''

    def __str__(self):
        return self.title




