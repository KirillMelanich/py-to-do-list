from django.db import models


class Tag(models.Model):
    tag = models.CharField(max_length=255)

    def __str__(self):
        return self.tag


class Task:
    content = models.TextField()
    datetime = models.DateTimeField(auto_now=True)
    deadline = models.DateTimeField(blank=True, null=True)
    done = models.BooleanField()
    tag = models.ManyToManyField(Tag, related_name="tags")
