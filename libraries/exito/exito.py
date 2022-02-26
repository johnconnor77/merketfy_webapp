from libraries.common import act_on_element, capture_page_screenshot, log_message
import time


class Exito:

    def __init__(self, rpa_selenium_instance):
        self.browser = rpa_selenium_instance
        self.exito_url = ""

    def access_exito(self):
        """
        Access Google from the browser.
        """
        self.browser.go_to(self.exito_url)

    def search_article(self, article_name: str):
        pass


