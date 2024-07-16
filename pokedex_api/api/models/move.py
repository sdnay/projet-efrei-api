from django.db import models


class Move(models.Model):
    identifier = models.CharField(max_length=79)
    generation_id = models.IntegerField()
    type_id = models.IntegerField()
    power = models.SmallIntegerField(null=True)
    pp = models.SmallIntegerField(null=True)
    accuracy = models.SmallIntegerField(null=True)
    priority = models.SmallIntegerField()
    target_id = models.IntegerField()
    damage_class_id = models.IntegerField()
    effect_id = models.IntegerField()
    effect_chance = models.IntegerField(null=True)
    contest_type_id = models.IntegerField(null=True)
    contest_effect_id = models.IntegerField(null=True)
    super_contest_effect_id = models.IntegerField(null=True)

    def serialize(self):
        return {
            "id": self.id,
            "identifier": self.identifier,
            "generation_id": self.generation_id,
            "type_id": self.type_id,
            "power": self.power,
            "pp": self.pp,
            "accuracy": self.accuracy,
            "priority": self.priority,
            "target_id": self.target_id,
            "damage_class_id": self.damage_class_id,
            "effect_id": self.effect_id,
            "effect_chance": self.effect_chance,
            "contest_type_id": self.contest_type_id,
            "contest_effect_id": self.contest_effect_id,
            "super_contest_effect_id": self.super_contest_effect_id
        }
    class Meta:
        db_table = 'moves'
        managed = False  # vu que la base données du prof contient déjà cette table
