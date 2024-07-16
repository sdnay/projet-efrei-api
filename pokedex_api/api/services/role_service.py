from ..repositories import role_repository


def get_all_roles():
    roles = role_repository.fetch_all_roles()
    return [role.serialize() for role in roles]
