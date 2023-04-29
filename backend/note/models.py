from django.db import models
from user.models import User


class Note(models.Model):
    title = models.CharField(max_length=255, unique=True)
    detail = models.TextField()
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        ordering = ("-updated_at",)

    def __str__(self):
        return self.title

    def delete(self):
        self.deleted = True
        return super(Note, self).delete()
