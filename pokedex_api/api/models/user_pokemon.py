from django.db import models
from .users import User
from .pokemon import Pokemon


class UserPokemon(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_pokemon')
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, related_name='user_pokemon')

    def serialize_user_pokemons(user):
        try:
            user_pokemons = UserPokemon.objects.filter(user=user).select_related('pokemon')
            return [up.pokemon.serialize() for up in user_pokemons]
        except UserPokemon.DoesNotExist:
            return []
    class Meta:
        db_table = 'user_pokemon'
