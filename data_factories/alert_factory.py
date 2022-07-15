import factory

from core.models import Alert
from data_factories.article_factory import ArticleFactory


class AlertFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Alert

    article = factory.SubFactory(ArticleFactory)
    target_price = factory.Faker('pyfloat', min_value=0.0, max_value=6000000.0, right_digits=2)
