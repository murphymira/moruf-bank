from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from .models import Account, User
from .serializer import AccountSerializer, UserSerializer


# Create your views here.

class AccountViewSet(ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
