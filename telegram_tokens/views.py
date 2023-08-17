from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import TelegramToken
import random
import string


class GenerateTelegramTokenView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        user = request.user
        token, created = TelegramToken.objects.get_or_create(user=user)
        token.key = ''.join(random.choices(string.ascii_letters + string.digits, k=32))
        token.save()
        return Response({'token': token.key}, status=status.HTTP_201_CREATED)
