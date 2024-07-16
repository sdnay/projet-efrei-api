from ..repositories import user_repository


def get_all_users():
    users = user_repository.fetch_all_users()
    return [user.serialize() for user in users]
