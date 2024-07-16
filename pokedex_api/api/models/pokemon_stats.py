# api/models/pokemon_types.py
from django.db import models

from .pokemon import Pokemon
from .stats import Stats


class PokemonStat(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, related_name='pokemon_stats')
    stat = models.ForeignKey(Stats, on_delete=models.CASCADE)
    base_stat = models.IntegerField()
    effort = models.IntegerField()

    class Meta:
        db_table = 'pokemon_stats'
        managed = False  # vu que la base données du prof contient déjà cette table
