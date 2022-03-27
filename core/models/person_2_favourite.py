from django.db import models

from .base_classes import MerketfyBase


class Person2Favourite(MerketfyBase):
    person = models.ForeignKey('Person', on_delete=models.CASCADE, db_column='person_id')
    favourite = models.ForeignKey('Favourite', on_delete=models.CASCADE, db_column='favourite_id')

    def __str__(self):
        return str(self.id)

    class Meta:
        managed = False
        db_table = 'person_2_favourite'
        unique_together = (('person', 'favourite'),)
