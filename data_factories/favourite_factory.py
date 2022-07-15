import factory

from core.models import Favourite

from data_factories.article_factory import ArticleFactory


class FavouriteFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Favourite

    article = factory.SubFactory(ArticleFactory)
