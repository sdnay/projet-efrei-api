from django.db import models

from .users import User
from .roles import Role


class UserRoles(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_roles')
    role = models.ForeignKey(Role, on_delete=models.CASCADE, related_name='user_roles')

    class Meta:
        db_table = 'user_roles'
