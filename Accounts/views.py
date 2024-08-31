from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from .models import UserAccount
from django.contrib.auth import authenticate

from rest_framework.decorators import api_view,permission_classes
from rest_framework.views import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from rest_framework.permissions import IsAuthenticated


# @api_view(['POST'])
# def register_user(request):
#     if request.method == 'POST':
#         serializer = UseraccountSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['POST'])
def login_user(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')
        
        if not username or not password:
            return JsonResponse({'error': 'Username and password are required'}, status=status.HTTP_400_BAD_REQUEST)
        
        user = authenticate(username=username, password=password)
        
        if user is None:
            return JsonResponse({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        
        token, _ = Token.objects.get_or_create(user=user)
        return JsonResponse({'token': token.key}, status=status.HTTP_200_OK)
    
    return JsonResponse({'error': 'Invalid request method'}, status=status.HTTP_405_METHOD_NOT_ALLOWED)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_user(request):
    if request.method == 'POST':
        try:
            request.user.auth_token.delete()
            return JsonResponse({'message': 'Successfully logged out.'}, status=status.HTTP_200_OK)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
