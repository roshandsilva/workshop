from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=256)
    timestamp = models.DateTimeField(blank=True)
    author = models.ForeignKey(User)
    text = models.TextField()

    def save(self):
        if not self.id:
            self.timestamp = timezone.now()
        super(Post, self).save()

    def __unicode__(self):
        return self.title
