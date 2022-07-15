import factory
from factory.fuzzy import FuzzyChoice

from core.models import Article
from core.models.model_utils.article_choices_field import ArticleBrandChoices, ArticleTypeChoices,\
    ArticleCategoryChoices

from data_factories.company_factory import CompanyFactory

ARTICLE_NAMES = ["iphone 12 Pro Max", "iphone 13 Pro", "iphone 12", "iphone xs", "iphone 8"]


class ArticleFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Article

    company = factory.SubFactory(CompanyFactory)
    article_category = FuzzyChoice(ArticleCategoryChoices.ARTICLE_CATEGORY_LIST)
    article_type = FuzzyChoice(ArticleTypeChoices.ARTICLE_TYPE_LIST)
    article_brand = FuzzyChoice(ArticleBrandChoices.ARTICLE_BRAND_LIST)
    name = FuzzyChoice(ARTICLE_NAMES)
    url = factory.Faker('pystr', min_chars=4, max_chars=255)
    price = factory.Faker('pyfloat', min_value=0.0, max_value=6000000.0, right_digits=2)
    shipping_price = factory.Faker('pyfloat', min_value=0.0, right_digits=2)
    rating = factory.Faker('pyfloat', min_value=0.1, max_value=5.0, right_digits=2)
