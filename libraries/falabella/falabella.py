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
        self.browser.go_to(self.falabella_url)

    def search_article(self, article_name: str):
        # //input[@class="SearchBar-module_searchBar__Input__1VvhT"]
        search_bar = act_on_element('//input[@class="SearchBar-module_searchBar__Input__1VvhT"]', "find_element")
        self.browser.input_text_when_element_is_visible('//input[@class="SearchBar-module_searchBar__Input__1VvhT"]', article_name)
        search_bar.send_keys(Keys.ENTER)

    def extract_info_article(self):

        cards_info = act_on_element('//div[@class="jsx-4001457643 search-results-list"]', "find_elements", time_range=8)[0:3]

        articles_list = []

        for card_info in cards_info:

            img_url = card_info.find_element(By.XPATH, './/img[1]').get_attribute('src')
            article_name_market = card_info.find_element(By.XPATH, './/span[1]/b[1]').text
            article_price = card_info.find_element(By.XPATH, '//li[1]//span').text
            data_article = {'article_name_market': article_name_market, 'article_image_url': img_url, 'article_price': article_price}
            articles_list.append(data_article)

        self.data_dict_list = articles_list





