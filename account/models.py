from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_sender = models.BooleanField()

    def __str__(self):
        return self.user.username

