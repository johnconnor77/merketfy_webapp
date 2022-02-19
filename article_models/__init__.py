import datetime
from pydantic import BaseModel


class ArticleInfo(BaseModel):
    """
        Information that comes from user input at Web App SearchBar
    """

    article_name: str
    filter_search: False
    markets_selected: list
    local_markets_suggestions: False

    class Config:
        title = 'Article Info selected by User'
