from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import TelegramMessage
from telegram import Bot
from users.models import CustomUser
from .models import TelegramToken
import random
import string

from .serializers import TelegramTokenSerializer


class GenerateTelegramTokenView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        user = request.user
        token, created = TelegramToken.objects.get_or_create(user=user)
        token.key = ''.join(random.choices(string.ascii_letters + string.digits, k=32))
        token.save()
        return Response({'token': token.key}, status=status.HTTP_201_CREATED)


class SetChatIdToUserView(APIView):
    def post(self, request, *args, **kwargs):
        print("yehu")
        serializer = TelegramTokenSerializer(data=request.data)
        if serializer.is_valid():
            chat_id = serializer.validated_data['chat_id']
            telegram_token_key = serializer.validated_data['token']

            try:
                user = CustomUser.objects.get(telegramtoken__key=telegram_token_key)
                user.telegram_chat_id = chat_id
                user.save()
            except CustomUser.DoesNotExist:
                print("Пользователь с таким токеном не найден.")

            return Response({'detail': 'Chat ID saved successfully.'}, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)





class SendTelegramMessageView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        user = request.user
        text = request.data.get('message', '')

        if text:
            TelegramMessage.objects.create(user=user, text=text)

            chat_id = user.telegram_chat_id
            if chat_id:
                bot_token = '6620893650:AAGgx_QzkcgZ4pz_UZUZCpZs4NtB-PGNifQ'
                bot = Bot(token=bot_token)
                bot.send_message(chat_id=chat_id, text=text)

                return Response({'detail': 'Telegram message sent successfully.'}, status=status.HTTP_201_CREATED)
            else:
                return Response({'detail': 'User chat_id not found.'}, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response({'detail': 'No message provided.'}, status=status.HTTP_400_BAD_REQUEST)
