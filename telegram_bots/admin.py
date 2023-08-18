from django.contrib import admin
from .models import TelegramToken
from .models import TelegramMessage

admin.site.register(TelegramToken)
admin.site.register(TelegramMessage)
