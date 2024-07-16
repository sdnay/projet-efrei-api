from django.contrib.auth.hashers import make_password
from ..models import User, Role, UserRoles


def find_by_email(email):
    try:
        return User.objects.get(email=email)
    except User.DoesNotExist:
        return None


def email_exists(email):
    return User.objects.filter(email=email).exists()


def create_user(data):
    user = User.objects.create(
        username=data['username'],
        email=data['email'],
        password_hash=make_password(data['password'])
    )
    try:
        member_role = Role.objects.get(name='membre')
        UserRoles.objects.create(user=user, role=member_role)
    except Role.DoesNotExist:
        print("Le rôle 'membre' n'existe pas. Veuillez le créer.")
        # Vous pouvez aussi choisir de lever une exception ou de gérer cela d'une autre manière.

    return user


def fetch_all_users():
    return User.objects.all()
