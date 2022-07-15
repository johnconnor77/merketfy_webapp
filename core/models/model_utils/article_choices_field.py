class ArticleTypeChoices:
    """Choices allowed for Article types"""
    UNKNOWN = 'unknown'
    SMARTPHONE = 'smartphone'
    LAPTOP = 'laptop'
    SPEAKER = 'speaker'
    HEADPHONES = 'headphone'

    ARTICLE_TYPE_LIST = [SMARTPHONE]

    ARTICLE_TYPE_CHOICES = [
        (UNKNOWN, UNKNOWN),
        (SMARTPHONE, SMARTPHONE),
        (LAPTOP, LAPTOP),
        (SPEAKER, SPEAKER),
        (HEADPHONES, HEADPHONES),
    ]


class ArticleCategoryChoices:
    """Choices allowed for Article categories"""
    UNKNOWN = 'unknown'
    TECHNOLOGY = 'technology'
    APPLIANCE = 'appliance'
    CLOTHING = 'clothing'

    ARTICLE_CATEGORY_LIST = [TECHNOLOGY]

    ARTICLE_CATEGORY_CHOICES = [
        (UNKNOWN, UNKNOWN),
        (APPLIANCE, APPLIANCE),
        (CLOTHING, CLOTHING),
    ]


class ArticleBrandChoices:
    """Choices allowed for Article Brand"""
    UNKNOWN = 'unknown'
    APPLE = 'apple'
    SAMSUNG = 'samsung'
    XIAOMI = 'xiaomi'
    SONY = 'sony'
    OPPO = 'oppo'
    LG = 'lg'
    ONEPLUS = 'oneplus'
    PANASONIC = 'panasonic'
    BENQ = 'benq'
    WHIRLPOOL = 'whirlpool'
    BOSE = 'bose'
    JBL = 'jbl'
    LENOVO = 'lenovo'
    ACER = 'acer'
    HP = 'hp'
    DELL = 'dell'
    GOPRO = 'go_pro'
    MICROSOFT = 'microsoft'
    HUAWEI = 'HUAWEI'
    MOTOROLA = 'motorola'
    HONOR = 'honor'
    REALME = 'realme'

    ARTICLE_BRAND_LIST = [
        APPLE,
        # SAMSUNG,
        # XIAOMI,
        # SONY,
        # OPPO,
        # LG,
        # ONEPLUS,
        # PANASONIC,
        # BENQ,
        # WHIRLPOOL,
        # BOSE,
        # JBL,
        # LENOVO,
        # ACER,
        # HP,
        # DELL,
        # GOPRO,
        # MICROSOFT,
        # HUAWEI,
        # MOTOROLA,
        # HONOR,
        # REALME
    ]

    ARTICLE_BRAND_CHOICES = [
        (UNKNOWN, UNKNOWN),
        (APPLE, APPLE),
        (SAMSUNG, SAMSUNG),
        (XIAOMI, XIAOMI),
        (SONY, SONY),
        (OPPO, OPPO),
        (LG, LG),
        (PANASONIC, PANASONIC),
        (BENQ, BENQ),
        (WHIRLPOOL, WHIRLPOOL),
        (BOSE, BOSE),
        (JBL, JBL),
        (LENOVO, LENOVO),
        (ACER, ACER),
        (HP, HP),
        (DELL, DELL),
        (GOPRO, GOPRO),
        (MICROSOFT, MICROSOFT),
        (HUAWEI, HUAWEI),
        (MOTOROLA, MOTOROLA),
        (HONOR, HONOR),
        (REALME, REALME),
    ]
