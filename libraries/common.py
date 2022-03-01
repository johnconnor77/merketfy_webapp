import shutil, time, os, sys
from robot.api import logger
from datetime import datetime, timedelta
from RPA.Browser.Selenium import Selenium

browser = Selenium()


def log_message(message: str, level: str = 'INFO', console: bool = True):
    """
    Function that logs messages depending on the level.
    """

    log_switcher = {'TRACE': logger.trace, 'INFO': logger.info, 'WARN': logger.warn, 'ERROR': logger.error}

    if not level.upper() in log_switcher.keys() or level.upper() == 'INFO':
        logger.info(message, True, console)
    else:
        if level.upper() == 'ERROR':
            logger.info(message, True, console)
        else:
            log_switcher.get(level.upper(), logger.error)(message, True)


def print_version():
    """
    Function that prints the version of the project.
    """
    try:
        file = open('VERSION')
        try:
            print('Version {}'.format(file.read().strip()))
        except Exception as e:
            print("Error reading VERSION file: {}".format(str(e)))
        finally:
            file.close()
    except Exception as e:
        log_message("VERSION file not found: {}".format(str(e)))


def create_or_clean_dir(folder_path: str):
    """
    Function that cleans and creates a determined folder.
    """
    shutil.rmtree(folder_path, ignore_errors = True)
    try:
        os.mkdir(folder_path)
    except FileExistsError:
        pass


def capture_page_screenshot(folder_path: str, name: str = None):
    """
    Function that captures a screenshot of the browser.
    """
    if not name:
        name = "Exception_{}.png".format(datetime.now().strftime("%H_%M_%S"))
    else:
        name = "{}_{}.png".format(name, datetime.now().strftime("%H_%M_%S"))
    browser.capture_page_screenshot(os.path.join(folder_path, name))


def act_on_element(path: str, action: str, time_range: int = 5):
    """
    Function that waits a predefined time for an element and acts on it as soon as it finds it.
    """
    timer = datetime.now() + timedelta(0, time_range)
    while timer > datetime.now():
        try:
            if action == "click_element":
                browser.click_element(path)
                return True
            elif action == "find_elements":
                results = browser.find_elements(path)
                if results:
                    return results
                else:
                    raise Exception
            elif action == "find_element":
                result = browser.find_element(path)
                return result
        except Exception as e:
            time.sleep(1)
    raise Exception("Element {} not found".format(path))


def pretty_list(data_list):
    for data in data_list:
        pretty_dict(data)
        print()


def pretty_dict(data_dict, indent=0):
   for key, value in data_dict.items():
      print('\t' * indent + str(key))
      if isinstance(value, dict):
         pretty_dict(value, indent+1)
      else:
         print('\t' * (indent+1) + str(value))
