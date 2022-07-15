import random

import factory
from factory.fuzzy import FuzzyChoice

from core.models import Article
from core.models.model_utils.article_choices_field import ArticleBrandChoices, ArticleTypeChoices, \
    ArticleCategoryChoices

from data_factories.company_factory import CompanyFactory

ARTICLE_NAMES_PER_BRAND = {
    ArticleBrandChoices.APPLE: ["iphone 12 Pro Max", "iphone 13 Pro", "iphone 12", "iphone xs", "iphone 8"]
}


def get_random_article_name_by_brand(brand_name: str):
    name_list = ARTICLE_NAMES_PER_BRAND.get(brand_name)
    if name_list:
        return random.choice(name_list)
    else:
        return None


class ArticleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Article
        django_get_or_create = ('name', 'company')

    company = factory.SubFactory(CompanyFactory)
    article_category = FuzzyChoice(ArticleCategoryChoices.ARTICLE_CATEGORY_LIST)
    article_type = FuzzyChoice(ArticleTypeChoices.ARTICLE_TYPE_LIST)
    article_brand = FuzzyChoice(ArticleBrandChoices.ARTICLE_BRAND_LIST)
    name = ""
    url = factory.Faker('pystr', min_chars=4, max_chars=255)
    price = factory.Faker('pyfloat', min_value=0.0, max_value=6000000.0, right_digits=2)
    shipping_price = factory.Faker('pyfloat', min_value=0.0, right_digits=2)
    rating = factory.Faker('pyfloat', min_value=0.1, max_value=5.0, right_digits=2)

    @classmethod
    def _create(cls, model_class, *args, **kwargs):
        article_brand_name = kwargs.get('article_brand')
        kwargs.update({'name': get_random_article_name_by_brand(article_brand_name)})
        return super()._create(model_class, *args, **kwargs)
