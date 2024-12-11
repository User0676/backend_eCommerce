from rest_framework import viewsets, permissions
from .models import Payment
from .serializers import PaymentSerializer

class PaymentViewSet(viewsets.ModelViewSet):
    queryset = Payment.objects.all()
    serializer_class = PaymentSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        # Пользователь видит платежи только по своим заказам
        return Payment.objects.filter(order__user=self.request.user)

    def perform_create(self, serializer):
        # Перед созданием платежа можно проверить, действительно ли заказ принадлежит пользователю
        order = serializer.validated_data['order']
        if order.user != self.request.user:
            raise PermissionError("You do not have permission to pay for this order.")
        return serializer.save()
