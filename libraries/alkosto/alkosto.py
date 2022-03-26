import time
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

        search_bar = act_on_element('//*[@id="js-site-search-input"]', "find_element")
        self.browser.input_text_when_element_is_visible('//*[@id="js-site-search-input"]', article_name)
        search_bar.click()
        time.sleep(2)
        search_bar.send_keys(Keys.ENTER)


    def extract_info_article(self):

        articles_name_market = act_on_element('//h2[@class="product__information--name"]', "find_elements")
        articles_price = act_on_element('//span[@class="price"]', "find_elements")
        articles_url = act_on_element('//div[@class="product__image--thumb"]', "find_elements")

        names = []
        prices = []
        url = []

        for article_name_market in articles_name_market:
            names.append(article_name_market.text)

        for article_price in articles_price:
            prices.append(article_price.text)

        for article_url in articles_url:
            #//a[@class="js-product-click-datalayer"]/img
            image_url = article_url.find_element(By.XPATH, '//a[@class="js-product-click-datalayer"]/img').get_attribute("src")
            url.append(image_url)


        articles_list = zip(names, prices, url)


        for data in list(articles_list):
            print(data)


        self.data_dict_list = articles_list





