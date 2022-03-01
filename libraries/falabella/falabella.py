from libraries.common import act_on_element, capture_page_screenshot, log_message
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class Falabella:

    def __init__(self, rpa_selenium_instance):
        self.browser = rpa_selenium_instance
        self.falabella_url = "https://www.falabella.com.co/falabella-co"
        self.data_dict_list = []

    def access_falabella(self):
        """
        Access Falabella from the browser.
        """
        self.browser.go_to(self.falabella_url_url)

    def search_article(self, article_name: str):
        pass

    def extract_info_article(self):
        articles_list = []
        pass





