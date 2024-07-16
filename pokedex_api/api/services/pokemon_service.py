from ..repositories import pokemon_repository


def get_pokemon_by_id(id):
    return pokemon_repository.get_pokemon_by_id(id)


def update_pokemon(id, data):
    return pokemon_repository.update_pokemon(id, data)


def delete_pokemon(name):
    return pokemon_repository.delete_pokemon(name)


def get_pokemon_by_name(name):
    return pokemon_repository.get_pokemon_by_name(name)


def update_pokemon_by_name(name, data):
    return pokemon_repository.update_pokemon_by_name(name, data)


def delete_pokemon_by_name(name):
    return pokemon_repository.delete_pokemon_by_name(name)


def get_pokemon_by_type(identifier):
    return pokemon_repository.get_pokemon_by_type(identifier)


def get_my_pokemon(user):
    # Call to repository and handle potential empty results
    result = pokemon_repository.get_my_pokemon(user)
    if not result:
        return {'error': 'No Pokémon found or user not properly serialized.'}
    return result
