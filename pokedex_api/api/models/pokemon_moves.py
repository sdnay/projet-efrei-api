from django.db import models
from .pokemon import Pokemon
from .move import Move


class PokemonMove(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE)
    move = models.ForeignKey(Move, on_delete=models.CASCADE)
    level = models.IntegerField()
    order = models.IntegerField(null=True)

    class Meta:
        db_table = 'pokemon_moves'
        managed = False  # vu que la base données du prof contient déjà cette table
