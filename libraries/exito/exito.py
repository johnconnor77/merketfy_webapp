from libraries.common import act_on_element, capture_page_screenshot, log_message
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class Exito:

    def __init__(self, rpa_selenium_instance):
        self.browser = rpa_selenium_instance
        self.exito_url = "https://www.exito.com/"
        self.data_dict_list = []

    def access_exito(self):
        """
        Access Exito from the browser.
        """
        self.browser.go_to(self.exito_url)

    def search_article(self, article_name: str):

        search_bar = act_on_element('//input[@class="vtex-styleguide-9-x-input ma0 border-box vtex-styleguide-9-x-hideDecorators vtex-styleguide-9-x-noAppearance br2  br-0 br--left  w-100 bn outline-0 bg-base c-on-base b--muted-4 hover-b--muted-3 t-body pl5 "]', "find_element")
        self.browser.input_text_when_element_is_visible('//input', article_name)
        search_bar.send_keys(Keys.ENTER)

    def extract_info_article(self):

        cards_info = act_on_element('//div[@class="pointer pt3 pb4 flex flex-column h-100"]', "find_elements", time_range=8)[0:3]
        articles_list = []

        for card_info in cards_info:

            image_info = card_info.find_element(By.XPATH, './div[1]')
            img_url = image_info.find_element(By.XPATH, './descendant::img[1]').get_attribute('src')
            container_info = card_info.find_element(By.XPATH, './div[2]')
            article_name_market = container_info.find_element(By.XPATH, './/div[@class="exito-product-details-3-x-stylePlp"]').text
            article_price = container_info.find_element(By.XPATH, './/descendant::span[@class="exito-vtex-components-4-x-currencyContainer"][2]').text
            data_article = {'article_name_market': article_name_market, 'article_image_url': img_url, 'article_price': article_price}
            articles_list.append(data_article)

        self.data_dict_list = articles_list




