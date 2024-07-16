from ..repositories import user_repository
from ..serializers import CustomTokenObtainPairSerializer


def login(data):
    user = user_repository.find_by_email(data['email'])
    if user and user.check_password(data['password']):
        # Utiliser le sérialiseur personnalisé
        token_serializer = CustomTokenObtainPairSerializer(data={'email': data['email'], 'password': data['password']})
        if token_serializer.is_valid():
            return {'success': True, 'token': token_serializer.validated_data}
        else:
            return {'success': False, 'message': 'Token could not be created', 'errors': token_serializer.errors}
    else:
        return {'success': False, 'message': 'Invalid credentials'}


def register(data):
    if user_repository.email_exists(data['email']):
        return {'success': False, 'message': 'Email already exists'}
    else:
        user = user_repository.create_user(data)
        return {'success': True, 'message': 'User registered successfully'}
