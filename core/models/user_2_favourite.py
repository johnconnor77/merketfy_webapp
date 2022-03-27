from django.db import models

from .base_classes import MerketfyBase


class User2Favourite(MerketfyBase):
    user = models.ForeignKey('User', on_delete=models.CASCADE, db_column='user_id')
    favourite = models.ForeignKey('Favourite', on_delete=models.CASCADE, db_column='favourite_id')

    def __str__(self):
        return str(self.id)

    class Meta:
        managed = False
        db_table = 'user_2_favourite'
        unique_together = (('user', 'favourite'),)
