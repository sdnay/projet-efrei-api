from ..models import Role


def fetch_all_roles():
    return Role.objects.all()
