import logging

from django.db import models
logger = logging.getLogger(__name__)


class Pokemon(models.Model):
    identifier = models.CharField(max_length=79)
    species_id = models.IntegerField()
    height = models.IntegerField()
    weight = models.IntegerField()
    base_experience = models.IntegerField()
    order = models.IntegerField()
    is_default = models.BooleanField()

    def serialize(self):
        return {
            "id": self.id,
            "identifier": self.identifier,
            "species_id": self.species_id,
            "height": self.height,
            "weight": self.weight,
            "base_experience": self.base_experience,
            "order": self.order,
            "is_default": self.is_default
        }

    class Meta:
        db_table = 'pokemon'
        managed = False  # vu que la base données du prof contient déjà cette table
