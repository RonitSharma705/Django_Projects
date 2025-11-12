from django.shortcuts import render
from rest_framework import viewsets
from .models import Todo
from .serializers import TodoSerializers


# Create your views here.

class TodoViews(viewsets.ModelViewSet):
    queryset= Todo.objects.all().order_by('-Created_at')
    serializer_class = TodoSerializers