from django.db import models


class Role(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def serialize(self):
        return {'id': self.id, 'name': self.name}

    class Meta:
        db_table = 'roles'
