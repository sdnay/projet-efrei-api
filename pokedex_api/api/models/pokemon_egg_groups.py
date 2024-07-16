from django.db import models

from .egg_groups import EggGroup
from .pokemon import Pokemon


class PokemonEggGroup(models.Model):
    species_id = models.ForeignKey(Pokemon, on_delete=models.CASCADE, db_column='species_id')
    egg_group = models.ForeignKey(EggGroup, on_delete=models.CASCADE)

    class Meta:
        db_table = 'pokemon_egg_groups'
        managed = False  # vu que la base données du prof contient déjà cette table
