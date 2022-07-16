import random

import factory.random
from django.core.management.base import BaseCommand, CommandError


COMMAND_HELP_MSG = (
    'Spin up a local database with test data using a model factory pattern. '
    'Example of use:  ./manage populate_database -a=10 -s=22443'
)


class Command(BaseCommand):
    # Use example:  ./manage.py populate_database -a=10 -s=22443
    help = COMMAND_HELP_MSG
    output_transaction = True

    def add_arguments(self, parser):
        # Optional argument
        parser.add_argument(
            '-a',
            '--article',
            type=str,
            help="Articles to be created "
                 "argument: 'cloud'",
        )

        parser.add_argument(
            '-s',
            '--seed',
            type=int,
            help="Seed number to handle the randomness -s=3344 or --seed=3344",
        )

    def handle(self, *args, **options):
        """
        This logics create as many batches as passed by args, then associate treatment runs created, finally the
        holdbacks.
        Notice the number of items created are passed by args
        """

        # import inside the handle to avoid circular importation when uses unit testing, since in the common factories
        # we import this whole module to get the multiple_facility variable

        from data_factories.article_2_image_factory import Article2ImageFactory
        from data_factories.person_2_alert import Person2AlertFactory
        from data_factories.person_2_favourite import Person2FavouriteFactory
        from data_factories.person_factory import PersonFactory
        from data_factories.article_factory import ArticleFactory
        from data_factories.favourite_factory import FavouriteFactory
        from data_factories.alert_factory import AlertFactory

        number_of_articles = int(options.get('a') or options.get('article')) or 5
        seed = options.get('s') or options.get('seed')

        # Parsing seed
        if seed:
            # Reproducible randomness. See https://factoryboy.readthedocs.io/en/stable/recipes.html#using
            # -reproducible-randomness
            factory.random.reseed_random(seed)
            print(f"The value {seed} was used as seed")
        else:
            print(f"A random seed value was used")

        # create Articles as the number passed in args.
        created_articles = ArticleFactory.create_batch(number_of_articles)
        created_favourites = [FavouriteFactory.create(article=article) for article in created_articles]
        created_alerts = [AlertFactory.create(article=article) for article in created_articles]

        for idx in range(len(created_articles)):
            # create persons and favourites as articles created
            Person2FavouriteFactory(favourite=created_favourites[idx])

            # create persons and alerts as articles created
            Person2AlertFactory(alert=created_alerts[idx])

        self.stdout.write(self.style.SUCCESS("finished successfully"))
