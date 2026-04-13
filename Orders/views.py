from rest_framework import viewsets, status, permissions
from rest_framework.response import Response
from .models import Order
from .serializers import OrderSerializer
from accounts.permissions import IsAdminRole, IsCustomerRole 

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer

    def get_queryset(self):
        user = self.request.user
       
        if hasattr(user, 'role') and user.role and user.role.name == 'Admin':
            return Order.objects.all()
      
        return Order.objects.filter(user=user)

    def get_permissions(self):
        
        if self.action == 'create':
           
            permission_classes = [IsCustomerRole]
        elif self.action in ['update', 'partial_update', 'destroy']:
           
            permission_classes = [IsAdminRole]
        else:
            permission_classes = [permissions.IsAuthenticated]
        
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
       
        serializer.save(user=self.request.user)
        order = serializer.save(user=self.request.user)