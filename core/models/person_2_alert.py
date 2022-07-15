from django.db import models

from .base_classes import MerketfyBase


class Person2Alert(MerketfyBase):
    person = models.ForeignKey('Person', on_delete=models.CASCADE, db_column='person_id')
    alert = models.ForeignKey('Alert', on_delete=models.CASCADE, db_column='alert_id')

    def __str__(self):
        return str(self.id)

    class Meta:
        managed = True
        db_table = 'person_2_alert'
        unique_together = (('person', 'alert'),)
