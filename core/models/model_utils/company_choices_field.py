class CompanyTypeChoices:
    """Choices allowed for booking status"""
    UNKNOWN = 'unknown'
    TECHNOLOGY = 'Technology'
    CONFIRMED = 'Confirmed'
    DECLINED = 'Declined'
    EXPIRED = 'Expired'
    CANCELLED = 'Cancelled'
    REVIEW = 'Review'

    COMPANY_TYPE_LIST = [UNKNOWN, TECHNOLOGY]

    COMPANY_TYPE_CHOICES = [
        (UNKNOWN, UNKNOWN),
        (TECHNOLOGY, TECHNOLOGY),
    ]
