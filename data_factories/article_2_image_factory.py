import factory

from core.models import Article2Image

from data_factories.article_factory import ArticleFactory
from data_factories.image_factory import ImageFactory


class Article2ImageFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Article2Image

    article = factory.SubFactory(ArticleFactory)
    image = factory.SubFactory(ImageFactory)


class ArticleWithPersonFactory(Article2ImageFactory):
    # Build 2 related images through class Article2ImageFactory
    images = factory.RelatedFactoryList(Article2ImageFactory, factory_related_name="article", size=2)
