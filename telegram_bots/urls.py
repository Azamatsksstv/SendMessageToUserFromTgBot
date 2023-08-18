from django.urls import path
from .views import GenerateTelegramTokenView, SetChatIdToUserView
from .views import SendTelegramMessageView

urlpatterns = [
    path('generateTgToken/', GenerateTelegramTokenView.as_view(), name='generate_tg_token'),
    path('setTgBotTokenToUser/', SetChatIdToUserView.as_view(), name='set-tg-bot-token'),
    path('sendMessage/', SendTelegramMessageView.as_view(), name='send_telegram_message'),
]
