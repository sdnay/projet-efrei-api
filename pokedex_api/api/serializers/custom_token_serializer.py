from abc import ABC

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        # Generate token with the parent class method
        token = super().get_token(user)

        # Add basic user information to the token
        token['username'] = user.username
        token['email'] = user.email

        # Retrieve the user's role and permissions
        role = user.get_role()  # Ensure to call the method if it's not a property
        if role:
            token['role'] = role.name  # Assign the role name to the token
            permissions = user.get_permissions()  # Get permissions using the method
            token['permissions'] = permissions  # Assign permissions list to the token

        return token
