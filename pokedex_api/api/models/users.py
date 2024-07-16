from django.contrib.auth.hashers import make_password
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.contrib.auth.hashers import check_password


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=255, unique=True)
    password_hash = models.CharField(max_length=255, default=make_password('123456.*'))
    created_at = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def check_password(self, raw_password):
        return check_password(raw_password, self.password_hash)

    def get_role(self):
        from api.models import UserRoles
        try:
            user_role = UserRoles.objects.get(user=self)
            return user_role.role
        except UserRoles.DoesNotExist:
            return None

    def get_permissions(self):
        role = self.get_role()
        permissions = set()
        if role:
            from api.models import RolePermissions
            role_permissions = RolePermissions.objects.filter(role=role)
            for rp in role_permissions:
                permissions.add(rp.permission.name)
        return list(permissions)

    def serialize(self):
        return {
            'id': self.id,
            'username': self.username
        }

    class Meta:
        db_table = 'users'
