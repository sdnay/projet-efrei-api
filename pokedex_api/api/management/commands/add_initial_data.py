from django.core.management.base import BaseCommand
from django.contrib.auth.hashers import make_password

from ...models import Permission, User, UserRoles, Role, RolePermissions


class Command(BaseCommand):
    help = 'Initializes roles, permissions, and an admin user'

    def handle(self, *args, **kwargs):
        # Permissions
        permissions_list = [
            'create_pokemon', 'read_pokemon', 'update_pokemon', 'delete_pokemon',
            'create_user', 'read_user', 'update_user', 'delete_user'
        ]
        permissions = {}
        for perm_name in permissions_list:
            permission, created = Permission.objects.get_or_create(name=perm_name)
            permissions[perm_name] = permission

        # Roles
        admin_role, _ = Role.objects.get_or_create(name='admin')
        member_role, _ = Role.objects.get_or_create(name='membre')

        # Associate Permissions with Admin Role
        all_permissions = permissions.values()
        for permission in all_permissions:
            RolePermissions.objects.get_or_create(role=admin_role, permission=permission)

        # Associate CRUD Pokemon Permissions with Member Role
        for perm_name in permissions_list[:4]:  # CRUD for Pokemon
            permission = permissions[perm_name]
            RolePermissions.objects.get_or_create(role=member_role, permission=permission)

        # Create an Admin User
        admin_user, created = User.objects.get_or_create(
            username='admin',
            defaults={
                'email': 'admin@example.com',
                'password_hash': make_password('amine123456')  # Use a secure password
            }
        )
        if created:
            UserRoles.objects.get_or_create(user=admin_user, role=admin_role)

        self.stdout.write(self.style.SUCCESS('Successfully initialized roles, permissions, and admin user'))
