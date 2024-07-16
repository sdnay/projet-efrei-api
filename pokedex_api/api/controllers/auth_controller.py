from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..services import auth_service


@api_view(['POST'])
def login_user(request):
    data = request.data
    result = auth_service.login(data)
    if result['success']:
        return Response(data=result['token'], status=status.HTTP_200_OK)
    else:
        return Response(data={'message': result['message']}, status=status.HTTP_401_UNAUTHORIZED)


@api_view(['POST'])
def register_user(request):
    result = auth_service.register(request.data)
    if result['success']:
        return Response(data=result['message'], status=status.HTTP_201_CREATED)
    else:
        return Response(data=result['message'], status=status.HTTP_400_BAD_REQUEST)
