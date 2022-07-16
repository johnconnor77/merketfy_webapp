import datetime

import factory
from factory.fuzzy import FuzzyChoice, FuzzyDate

from core.models import Person


class PersonFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Person

    username = factory.Faker('user_name')
    email = factory.Faker('email')
    phone_number = factory.Faker('phone_number')
    first_name = factory.Faker('first_name')
    last_name = factory.Faker('last_name')
    birth_date = FuzzyDate(datetime.date(1960, 1, 1), datetime.date(2002, 1, 1))
    date_joined = factory.LazyFunction(datetime.datetime.now)
    last_login = factory.LazyFunction(datetime.datetime.now)
