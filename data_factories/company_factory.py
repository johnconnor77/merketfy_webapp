import factory
from factory.fuzzy import FuzzyChoice

from core.models import Company
from core.models.model_utils.company_choices_field import CompanyTypeChoices

COMPANY_NAMES = ["Falabella", "Exito", "Ktronix", "Mercado Libre"]


class CompanyFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Company

    name = FuzzyChoice(COMPANY_NAMES)
    company_type: FuzzyChoice(CompanyTypeChoices.COMPANY_TYPE_LIST)
    note = factory.Faker('pystr', min_chars=4, max_chars=1024)
    icon_url = factory.Faker('pystr', min_chars=4, max_chars=1024)
