import factory

from core.models import Person2Alert

from data_factories.person_factory import PersonFactory
from data_factories.alert_factory import AlertFactory


class Person2FavouriteFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Person2Alert

    person = factory.SubFactory(PersonFactory)
    alert = factory.SubFactory(AlertFactory)


class PersonWithAlertFactory(Person2FavouriteFactory):
    # Build 2 related favourite through class Person2FavouriteFactory
    alerts = factory.RelatedFactoryList(Person2FavouriteFactory, factory_related_name="person", size=2)
