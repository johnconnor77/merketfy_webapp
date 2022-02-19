from pydantic import BaseModel


class ArticleInfo(BaseModel):
    """
        Information that comes from user input at Web App SearchBar
    """

    article_name: str
    filter_search: bool
    markets_selected: list
    local_markets_suggestions: bool

    class Config:
        title = 'Article Info selected by User'
