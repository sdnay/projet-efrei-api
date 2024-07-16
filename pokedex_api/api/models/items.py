from django.db import models


class Items(models.Model):
    identifier = models.CharField(max_length=79)
    category_id = models.IntegerField()
    cost = models.IntegerField()
    fling_power = models.IntegerField(null=True, blank=True)
    fling_effect_id = models.IntegerField(null=True, blank=True)

    def serialize(self):
        return {
            'id': self.id,
            'identifier': self.identifier,
            'category_id': self.category_id,
            'cost': self.cost,
            'fling_power': self.fling_power if self.fling_power is not None else "N/A",
            'fling_effect_id': self.fling_effect_id if self.fling_effect_id is not None else "N/A",
        }

    class Meta:
        db_table = 'items'
        managed = False  # vu que la base données du prof contient déjà cette table
