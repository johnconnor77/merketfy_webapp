from libraries.common import log_message, capture_page_screenshot, browser, pretty_list
from libraries.exito.exito import Exito
from libraries.falabella.falabella import Falabella
from libraries.alkosto.alkosto import Alkosto
from config import OUTPUT_FOLDER, tabs_dict
from libraries.linio.linio import Linio


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
        log_message(f"Article to search on market: {article_name}")

        exito = Exito(browser)
        log_message(f"Start search on {Exito.__name__} Web" )
        exito.access_exito()
        log_message(f"Search information Article {article_name} on {exito.exito_url}")
        exito.search_article(article_name)
        log_message(f"Extract information from {article_name} on {Exito.__name__}")
        exito.extract_info_article()
        pretty_list(exito.data_dict_list)
        log_message(f"Finished Extraction from {Exito.__name__}")

        falabella = Falabella(browser)
        log_message(f"Start search on {Falabella.__name__} Web" )
        falabella.access_falabella()
        log_message(f"Search information Article {article_name} on {falabella.falabella_url}")
        falabella.search_article(article_name)
        log_message(f"Extract information from {article_name} on {Falabella.__name__}")
        falabella.extract_info_article()
        pretty_list(falabella.data_dict_list)
        log_message(f"Finished Extraction from {Falabella.__name__}")

        alkosto = Alkosto(browser)
        log_message(f"Start search on {Alkosto.__name__} Web")
        alkosto.access_alkosto()
        log_message(f"Search information Article {article_name} on {alkosto.alkosto_url}")
        alkosto.search_article(article_name)
        log_message(f"Extract information from {article_name} on {Alkosto.__name__}")
        alkosto.extract_info_article()
        pretty_list(alkosto.data_dict_list)
        log_message(f"Finished Extraction from {Alkosto.__name__}")

        linio = Linio(browser)
        log_message(f"Start search on {Linio.__name__} Web")
        linio.access_linio()
        log_message(f"Search information Article {article_name} on {linio.linio_url}")
        linio.search_article(article_name)
        log_message(f"Extract information from {article_name} on {Linio.__name__}")
        linio.extract_info_article()
        pretty_list(linio.data_dict_list)
        log_message(f"Finished Extraction from {Linio.__name__}") 

    def finish(self):
        log_message("DW Process Finished")
        browser.close_browser()
