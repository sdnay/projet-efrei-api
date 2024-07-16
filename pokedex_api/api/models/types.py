from django.db import models


class Type(models.Model):
    identifier = models.CharField(max_length=79)
    generation_id = models.IntegerField()
    damage_class_id = models.IntegerField(null=True)

    class Meta:
        db_table = 'types'
        managed = False  # vu que la base données du prof contient déjà cette table
