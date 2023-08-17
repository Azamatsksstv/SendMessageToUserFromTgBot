from django.urls import path
from .views import GenerateTelegramTokenView

urlpatterns = [
    path('generateTgToken/', GenerateTelegramTokenView.as_view(), name='generate_tg_token'),
]
