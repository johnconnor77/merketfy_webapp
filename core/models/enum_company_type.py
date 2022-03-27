from .base_classes import EnumModelBase


class EnumCompanyType(EnumModelBase):
    class Meta:
        managed = False
        db_table = 'enum_company_type'
