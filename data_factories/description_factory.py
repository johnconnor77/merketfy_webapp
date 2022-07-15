import factory
from factory.fuzzy import FuzzyChoice

from core.models import Description
from core.models.model_utils.company_choices_field import CompanyTypeChoices

from data_factories.article_factory import ArticleFactory


class DescriptionFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Description

    article = factory.SubFactory(ArticleFactory)
    description = factory.Faker('pystr', min_chars=4, max_chars=255)
    attributes = {}
