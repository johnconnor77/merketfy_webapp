from libraries.common import log_message, capture_page_screenshot, browser
from libraries.exito.exito import Exito
from libraries.falabella.falabella import Falabella
from config import OUTPUT_FOLDER, tabs_dict


class Process:
    def __init__(self):
        log_message("Initialization")

        prefs = {
            "profile.default_content_setting_values.notifications": 2,
            "profile.default_content_settings.popups": 0,
            "directory_upgrade": True,
            "download.default_directory": OUTPUT_FOLDER,
            "plugins.always_open_pdf_externally": True,
            "download.prompt_for_download": False
        }
        browser.open_available_browser(preferences=prefs)
        browser.set_window_size(1920, 1080)
        browser.maximize_browser_window()

    def start(self):
        article_name = "iphone 12"
        exito = Exito(browser)
        exito.access_exito()
        exito.search_article()
        exito.extract_info_article()
        falabella = Falabella(browser)
        falabella.access_falabella()



    def finish(self):
        log_message("DW Process Finished")
        browser.close_browser()
