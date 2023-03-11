from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    name = models.CharField(max_length=256)
    password = models.CharField(max_length=256)
    department_id = models.SmallIntegerField()
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(default=timezone.now)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title