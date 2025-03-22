from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from django.db.models import Prefetch
from .models import CustomUser, CryptoWalletItem, VirtualWalletItem
from .serializers import UserProfileSerializer


class UserProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = (
            CustomUser.objects
            .select_related('crypto_wallet', 'virtual_wallet')
            .prefetch_related(
                Prefetch(
                    'crypto_wallet__items',
                    queryset=CryptoWalletItem.objects.select_related('currency')
                ),
                Prefetch(
                    'virtual_wallet__items',
                    queryset=VirtualWalletItem.objects.select_related('currency')
                )
            )
            .get(id=request.user.id)
        )

        serializer = UserProfileSerializer(user)
        return Response(serializer.data)
