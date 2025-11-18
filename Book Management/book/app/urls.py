from django.urls import path
from .views import Bookview

urlpatterns = [
    path('books/', Bookview.as_view()),
]