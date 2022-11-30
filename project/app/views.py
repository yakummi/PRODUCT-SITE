from django.shortcuts import render
from rest_framework.filters import SearchFilter
from rest_framework.viewsets import ModelViewSet
from app.models import Category, Comment, Product
from app.serializers import CategorySerializer, CommentSerializer, ProductSerializer
from django_filters.rest_framework import DjangoFilterBackend


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]

class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]

