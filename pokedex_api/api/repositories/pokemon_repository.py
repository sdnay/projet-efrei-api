# api/repositories/pokemon_repository.py
from ..models import Pokemon, Type, PokemonType, UserPokemon


def get_pokemon_by_id(id):
    try:
        return Pokemon.objects.get(pk=id).serialize()
    except Pokemon.DoesNotExist:
        return None


def update_pokemon(id, data):
    try:
        pokemon = Pokemon.objects.get(pk=id)
        for key, value in data.items():
            setattr(pokemon, key, value)
        pokemon.save()
        return {'success': True, 'pokemon': pokemon.serialize(), 'message': 'Pokemon changed'}
    except Pokemon.DoesNotExist:
        return {'success': False, 'message': 'Pokemon not found'}


def delete_pokemon(id):
    try:
        pokemon = Pokemon.objects.get(pk=id)
        pokemon.delete()
        return True
    except Pokemon.DoesNotExist:
        return False


def get_pokemon_by_name(name):
    try:
        return Pokemon.objects.get(identifier=name).serialize()
    except Pokemon.DoesNotExist:
        return None


def update_pokemon_by_name(name, data):
    try:
        pokemon = Pokemon.objects.get(identifier=name)
        for key, value in data.items():
            setattr(pokemon, key, value)
        pokemon.save()
        return {'success': True, 'pokemon': pokemon.serialize(), 'message': 'Pokemon changed'}
    except Pokemon.DoesNotExist:
        return {'success': False, 'message': 'Pokemon not found'}


def delete_pokemon_by_name(name):
    try:
        pokemon = Pokemon.objects.get(identifier=name)
        pokemon.delete()
        return True
    except Pokemon.DoesNotExist:
        return False


def get_pokemon_by_type(identifier):
    try:
        type_instance = Type.objects.get(identifier=identifier)

        pokemons = Pokemon.objects.filter(pokemon_types__type=type_instance).distinct()
        return [pokemon.serialize() for pokemon in pokemons]
    except Type.DoesNotExist:
        return []


def get_my_pokemon(user):
    try:
        user_data = user.serialize()

        user_pokemons = UserPokemon.objects.filter(user=user).select_related('pokemon')
        pokemon_data = [up.pokemon.serialize() for up in user_pokemons]

        return {
            'user': user_data,
            'pokemons': pokemon_data
        }
    except UserPokemon.DoesNotExist:
        return []
