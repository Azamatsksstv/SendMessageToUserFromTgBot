from django.urls import path
from .views import GenerateTelegramTokenView, BindChatIdToUserView
from .views import SendTelegramMessageView

urlpatterns = [
    path('generateTgToken/', GenerateTelegramTokenView.as_view(), name='generate_tg_token'),
    path('bindChatToUser/', BindChatIdToUserView.as_view(), name='bind_chat_to_user'),
    path('sendMessage/', SendTelegramMessageView.as_view(), name='send_telegram_message'),
]
