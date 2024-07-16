from django.db import models


class PokemonFormGeneration(models.Model):
    pokemon_form_id = models.IntegerField()
    generation_id = models.IntegerField()
    game_index = models.IntegerField()

    class Meta:
        db_table = 'pokemon_form_generations'
        managed = False  # vu que la base données du prof contient déjà cette table
