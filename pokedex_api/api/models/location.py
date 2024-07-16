from django.db import models


class Location(models.Model):
    region_id = models.IntegerField(null=True, blank=True)
    identifier = models.CharField(max_length=79)

    class Meta:
        db_table = 'locations'
        managed = False  # vu que la base données du prof contient déjà cette table
