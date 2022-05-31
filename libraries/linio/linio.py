import time
from libraries.common import act_on_element, capture_page_screenshot, log_message
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class Linio:

    def __init__(self, rpa_selenium_instance):
        self.browser = rpa_selenium_instance
        self.linio_url = "https://www.linio.com.co/"
        self.data_dict_list = []

    def access_linio(self):
        """
        Access Linio from the browser.
        """
        self.browser.go_to(self.linio_url)

    def search_article(self, article_name: str):

        search_bar = act_on_element('//div[@class="input-group"]/input', "find_element")
        self.browser.input_text_when_element_is_visible('//div[@class="input-group"]/input', article_name)
        search_bar.click()
        time.sleep(2)
        search_bar.send_keys(Keys.ENTER)


    def extract_info_article(self):

        articles_name_market = act_on_element('//*[@id="catalogue-product-container"]/div/a', "find_elements")
        articles_price = act_on_element('//*[@id="catalogue-product-container"]/div/a/div[@class="detail-container"]/div[@class="price-section"]/meta[@itemprop="price"]', "find_elements")
        articles_url = act_on_element('//*[@id="catalogue-product-container"]/div/a/div/figure/picture/img', "find_elements")

        names = []
        prices = []
        url = []

        for article_name_market in articles_name_market:
            names.append(article_name_market.get_attribute("title"))

        for article_price in articles_price:
            prices.append(article_price.get_attribute("content"))

        for article_url in articles_url:
            image_url = article_url.get_attribute("src")
            url.append(image_url)


        articles_list = zip(names, prices, url)


        for data in list(articles_list):
            print(data)


        self.data_dict_list = articles_list





