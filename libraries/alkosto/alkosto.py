from libraries.common import act_on_element, capture_page_screenshot, log_message
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class Alkosto:

    def __init__(self, rpa_selenium_instance):
        self.browser = rpa_selenium_instance
        self.alkosto_url = "https://www.alkosto.com/"
        self.data_dict_list = []

    def access_alkosto(self):
        """
        Access Alkosto from the browser.
        """
        self.browser.go_to(self.alkosto_url)

    def search_article(self, article_name: str):
        search_bar = self.browser.find_element(By.ID, 'js-site-search-input')
        search_bar.click()
        search_bar.send_keys(article_name)
        self.browser.implicitly_wait(5)
        search_bar.send_keys(Keys.ENTER)

    def extract_info_article(self):
        articles_name_market = self.browser.find_elements(By.CLASS_NAME, 'product__information--name')
        articles_price = self.browser.find_elements(By.CLASS_NAME, 'product__price--discounts__price')
        articles_url = self.browser.find_elements(By.XPATH, 'product__image__container')

        names = []
        prices = []
        urls = []

        for article_name_market in articles_name_market:
            names.append(article_name_market.text)

        for article_price in articles_price:
            prices.append(article_price.text)

        for article_url in articles_url:
            prices.append(article_url.get_attribute('src'))

        articles_list = zip(names, prices, urls)

        self.data_dict_list = articles_list





