from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
import logging
from . serializers import UserRegisterSerializer
from rest_framework.authtoken.models import Token

logger = logging.getLogger(__name__)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def test_token(request):
    logger.debug(f"User: {request.user}")
    logger.debug(f"Token: {request.auth}")
    return Response({"message": "Token is valid"}, status=status.HTTP_200_OK)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout_user(request):
    logger.debug(f"User: {request.user}")
    logger.debug(f"Token: {request.auth}")
    if request.method == 'POST':
        request.user.auth_token.delete()
        return Response({"Message": "Logged Out Successfully"}, status=status.HTTP_200_OK)


@api_view(['POST'])
def user_register(request):
    if request.method == 'POST':
        serializer = UserRegisterSerializer(data=request.data)
        
        data = {}
        
        if serializer.is_valid():
            account = serializer.save()
            
            data['response'] = 'Account has been created'
            data['username'] = account.username
            data['email'] = account.email
            
            token = Token.objects.get(user=account).key
            data['token'] = token
        else:
            data = serializer.errors
            
        return Response(data)
            
            
            