from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from account.serializers import UserRegistrationSerializer,UserLoginSerializer,ChangePasswordSerializer,SendPasswordRestEmailSerializer,UserPasswordRestSerializer
from account.models import User
from django.contrib.auth import authenticate
from account.jwtauth import get_token_for_user
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class UserRegistrationView(APIView):
    def post(self,request):
        serializer=UserRegistrationSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.save()
            token = get_token_for_user(user)
            return Response({'tokens':token},status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    
    
    def get(self,request):
        dt = UserRegistrationSerializer(User.objects.all(),many=True).data
        return Response(dt)
    
    
class UserLoginView(APIView):
    def post(self,request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            email=serializer.data.get('email')
            password=serializer.data.get('password')
            user = authenticate(email=email, password=password)
            print(user)
            if user is not None:
                token = get_token_for_user(user)

                return Response({"tokens":token,"msg":"User Login success"},status=status.HTTP_200_OK)
            else:
                return Response({'errors':["login crediential not fount"]},status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)   
    
    
class UserChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        serializer = ChangePasswordSerializer(data=request.data,context={'user':request.user})
        if serializer.is_valid(raise_exception=True):
            return Response({'msg':'password Changed successfully'},status=status.HTTP_200_OK)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

        
class SendPasswordRestEmailView(APIView):
    # permission_classes= [IsAuthenticated]
    def post(self,request):
        print(request.data,'dddddddddddddddddd')

        serializer=SendPasswordRestEmailSerializer(data=request.data) 
        if serializer.is_valid(raise_exception=True):
            return Response({"msg":"Password Rest link send. please check your mail"},status=status.HTTP_200_OK)   
            
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

        
        
        
class UserPasswordRestView(APIView):
    def post(self,request,uid,token):
        serializer=UserPasswordRestSerializer(data=request.data,context={'uid':uid,'token':token})
        if serializer.is_valid(raise_exception=True):
            return Response({'msg':'password reset successfully'},status=status.HTTP_200_OK)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        