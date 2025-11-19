from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import SignupSerializers,LoginSerializers
from rest_framework_simplejwt.tokens import RefreshToken

class SignupView(APIView):
    def post(self,request):
        serializer =SignupSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({'Message':"User Created SuccessFully"},status=201)
        return Response(serializer.errors,status=400)
    
class LoginView(APIView):
    def post(self,request):
        serializer=LoginSerializers(data=request.data)
        if serializer.is_valid():
            user=serializer.validated_data['user']
            refresh=RefreshToken.for_user(user)

            return Response({
                "message":"Login SuccessFully",
                "refresh":str(refresh),
                "access":str(refresh.access_token),
            })
        return Response(serializer.errors, status=400)