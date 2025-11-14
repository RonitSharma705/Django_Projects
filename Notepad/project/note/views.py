from django.shortcuts import render
from rest_framework import viewsets
from .models import Notes
from .serializers import NotesSerializer


class NoteView(viewsets.ModelViewSet):
    queryset = Notes.objects.all().order_by('-Created_at')
    serializer_class = NotesSerializer