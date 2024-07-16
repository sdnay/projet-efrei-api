from django.db import models


class Stats(models.Model):
    damage_class_id = models.IntegerField(null=True, blank=True)
    identifier = models.CharField(max_length=79)
    is_battle_only = models.BooleanField()
    game_index = models.IntegerField(null=True, blank=True)

    class Meta:
        db_table = 'stats'
        managed = False  # vu que la base données du prof contient déjà cette table
