from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    deleted = models.BooleanField(default=False)

    def delete(self):
        self.deleted = True
        return super(User, self).delete()
