from django.db import models
from users.models import CustomUser


class TelegramToken(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    key = models.CharField(max_length=255, unique=True)
