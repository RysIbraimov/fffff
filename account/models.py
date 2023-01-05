from django.db import models
from django.contrib.auth.views import get_user_model

User = get_user_model()

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_sender = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username