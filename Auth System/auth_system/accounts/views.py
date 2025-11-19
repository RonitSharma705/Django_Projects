from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SignupSerializers

class SignupView(APIView):
    def post(self,request):
        serializer =SignupSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'Message':"User Created SuccessFully"},status=201)
        return Response(serializer.errors,status=400)