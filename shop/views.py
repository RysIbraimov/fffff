from django.shortcuts import render
from rest_framework import viewsets, authentication


from .models import Category,Item,Order
from .serializers import CategorySerializer
from .permissions import IsSenderOrReadOnly

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    authentication_classes = [authentication.TokenAuthentication, ]
    permission_classes = [IsSenderOrReadOnly,]