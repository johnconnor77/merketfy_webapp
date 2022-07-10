"""This file contains the wiring up between urls and views
"""
from rest_framework import routers

from core.views import *


class ApiRouter:
    """
    Encapsulate the adding of view sets to the api router.
    """

    @classmethod
    def get(cls):
        router = routers.SimpleRouter()
        router.register(r'descriptions', DescriptionViewSet)
        router.register(r'articles', ArticleViewSet)
        router.register(r'companies', CompanyViewSet)
        router.register(r'historical_prices', HistoricalPriceViewSet)
        router.register(r'images', ImageViewSet)
        router.register(r'favourites', FavouriteViewSet)
        router.register(r'alerts', AlertViewSet)
        router.register(r'persons', PersonViewSet)

        return router
