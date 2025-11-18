from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import bookserializer
from .models import Books

# Create your views here.
class Bookview(APIView):
    def get(self, request):
        books = Books.objects.all()
        serializer = bookserializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def post(self, request):
        serializer = bookserializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Book Created Successfully!", "data": serializer.data},
                status=status.HTTP_201_CREATED
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
