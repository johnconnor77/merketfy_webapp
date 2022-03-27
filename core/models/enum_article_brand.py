from .base_classes import EnumModelBase


class EnumArticleBrand(EnumModelBase):
    class Meta:
        managed = False
        db_table = 'enum_article_brand'
