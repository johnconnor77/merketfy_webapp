from django.db import models

from .base_classes import MerketfyBase


class User2Alert(MerketfyBase):
    user = models.ForeignKey('User', on_delete=models.CASCADE, db_column='user_id')
    alert = models.ForeignKey('Alert', on_delete=models.CASCADE, db_column='alert_id')

    def __str__(self):
        return str(self.id)

    class Meta:
        managed = False
        db_table = 'user_2_alert'
        unique_together = (('user', 'alert'),)
