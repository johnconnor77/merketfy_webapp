import factory
from factory.fuzzy import FuzzyChoice

from core.models import Image
from core.models.model_utils.company_choices_field import CompanyTypeChoices


class ImageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Image

    name = factory.Faker('pystr', min_chars=4, max_chars=255)
    url = factory.Faker('pystr', min_chars=4, max_chars=255)
