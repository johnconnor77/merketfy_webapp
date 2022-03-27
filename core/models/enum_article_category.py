from .base_classes import EnumModelBase


class EnumArticleCategory(EnumModelBase):
    class Meta:
        managed = False
        db_table = 'enum_article_category'
