import factory

from core.models import HistoricalPrice

from data_factories.article_factory import ArticleFactory


class HistoricalPriceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = HistoricalPrice

    article = factory.SubFactory(ArticleFactory)
    price = factory.Faker('pyfloat', min_value=1000000.0, max_value=6000000.0, right_digits=2)
