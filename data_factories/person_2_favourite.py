import factory

from core.models import Person2Favourite

from data_factories.person_factory import PersonFactory
from data_factories.favourite_factory import FavouriteFactory


class Person2FavouriteFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Person2Favourite

    person = factory.SubFactory(PersonFactory)
    favourite = factory.SubFactory(FavouriteFactory)


class PersonWithFavouriteFactory(Person2FavouriteFactory):
    # Build 2 related favourite through class Person2FavouriteFactory
    favourites = factory.RelatedFactoryList(Person2FavouriteFactory, factory_related_name="person", size=2)
