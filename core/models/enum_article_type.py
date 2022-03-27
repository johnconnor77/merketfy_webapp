from .base_classes import EnumModelBase


class EnumArticleType(EnumModelBase):
    class Meta:
        managed = False
        db_table = 'enum_article_type'
