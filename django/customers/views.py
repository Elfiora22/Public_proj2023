from django.http.response import HttpResponse
from rest_framework import generics
from .serializers import CustomerSerializer, MyOrderdSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from orders.models import Order



class GetAuthCustomer(generics.RetrieveAPIView):
    serializer_class = CustomerSerializer


class MyOrders(generics.ListAPIView):
    serializer_class = MyOrderdSerializer
    authentication_classes = (JWTAuthentication, )
    permission_classes = (IsAuthenticated, )

    def get_queryset(self):
        return Order.objects.filter(customer__user = self.request.user)



    


