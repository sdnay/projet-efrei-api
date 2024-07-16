from rest_framework.permissions import BasePermission
from ..models import UserRoles, Role


class IsAdminUserCustom(BasePermission):
    """
    Allows access only to admin users.
    """

    def has_permission(self, request, view):
        if not request.user.is_authenticated:
            return False

        # Fetch user roles via the UserRole table
        user_roles = UserRoles.objects.filter(user=request.user)
        # Check if any of the user's roles are named 'admin'
        return any(role.role.name == 'admin' for role in user_roles)
