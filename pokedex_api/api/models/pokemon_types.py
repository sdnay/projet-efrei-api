from django.db import models

from .pokemon import Pokemon
from .types import Type


class PokemonType(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, related_name="pokemon_types")
    type = models.ForeignKey(Type, on_delete=models.CASCADE, related_name="pokemon_types")
    slot = models.IntegerField()

    class Meta:
        db_table = 'pokemon_types'
        managed = False  # vu que la base données du prof contient déjà cette table
