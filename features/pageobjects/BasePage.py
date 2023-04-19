import time

import selenium.common.exceptions
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions, wait
from utilities import configReader
from utilities import log_util
from selenium.common.exceptions import *

log = log_util.get_logs()


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def get_locator(self, locator_name):
        locator = configReader.readConfig("locators", locator_name)
        return locator

    def get_element(self, locator_name):

        global element
        try:
            if str(locator_name).endswith('ID'):
                element = self.driver.find_element(By.ID, self.get_locator(locator_name))
            elif str(locator_name).endswith('XPATH'):
                element = self.driver.find_element(By.XPATH, self.get_locator(locator_name))
            elif str(locator_name).endswith('CSS'):
                element = self.driver.find_element(By.CSS_SELECTOR, self.get_locator(locator_name))
            elif str(locator_name).endswith('NAME'):
                element = self.driver.find_element(By.NAME, self.get_locator(locator_name))
            elif str(locator_name).endswith('TAG_NAME'):
                element = self.driver.find_element(By.TAG_NAME, self.get_locator(locator_name))
            elif str(locator_name).endswith('CLASS_NAME'):
                element = self.driver.find_element(By.CLASS_NAME, self.get_locator(locator_name))
            elif str(locator_name).endswith('LINK_TEXT'):
                element = self.driver.find_element(By.LINK_TEXT, self.get_locator(locator_name))
            elif str(locator_name).endswith('PARTIAL_LINK_TEXT'):
                element = self.driver.find_element(By.PARTIAL_LINK_TEXT, self.get_locator(locator_name))
            log.info(f'element: {self.get_text(element)} is found successfully')
        except NoSuchElementException as e:
            log.error(
                f"Not able to get element | locator_name: {locator_name} | locator_value: {self.get_locator(locator_name)} | Exception Type: {type(e).__name__}")
        except Exception as e:
            log.error(
                f"Not able to get element | locator_name: {locator_name} | locator_value: {self.get_locator(locator_name)} | Exception Type: {type(e).__name__} | Detailed description: {e}")

        return element

    def get_element_list(self, locator_name):

        global element_list
        print(locator_name)
        try:
            if str(locator_name).endswith('ID'):
                element_list = self.driver.find_elements(By.ID, self.get_locator(locator_name))
            elif str(locator_name).endswith('XPATH'):
                element_list = self.driver.find_elements(By.XPATH, self.get_locator(locator_name))
            elif str(locator_name).endswith('CSS'):
                print('got css')
                element_list = self.driver.find_elements(By.CSS_SELECTOR, self.get_locator(locator_name))
            elif str(locator_name).endswith('NAME'):
                element_list = self.driver.find_elements(By.NAME, self.get_locator(locator_name))
            elif str(locator_name).endswith('TAG_NAME'):
                element_list = self.driver.find_elements(By.TAG_NAME, self.get_locator(locator_name))
            elif str(locator_name).endswith('CLASS_NAME'):
                element_list = self.driver.find_elements(By.CLASS_NAME, self.get_locator(locator_name))
            elif str(locator_name).endswith('LINK_TEXT'):
                element_list = self.driver.find_elements(By.LINK_TEXT, self.get_locator(locator_name))
            elif str(locator_name).endswith('PARTIAL_LINK_TEXT'):
                element_list = self.driver.find_elements(By.PARTIAL_LINK_TEXT, self.get_locator(locator_name))
            log.info('element list is found successfully')
        except NoSuchElementException as e:
            log.error(
                f"Not able to get element | locator_name: {locator_name} | locator_value: {self.get_locator(locator_name)} | Exception Type: {type(e).__name__}")
        except Exception as e:
            log.error(f"Not able to get element list | Exception Type: {type(e).__name__} | Detailed description: {e}")

        return element_list

    def wait(self, time_in_seconds: int):
        time.sleep(time_in_seconds)

    def implicit_wait(self, time_in_seconds: int):
        self.driver.implicitly_wait(time_in_seconds)

    def wait_for_element_to_be_visible(self, locator_name: str, time_in_seconds: int):

        global element
        try:
            if str(locator_name).endswith('ID'):
                element = WebDriverWait(self.driver, time_in_seconds).until(
                    expected_conditions.visibility_of_element_located((By.ID, self.get_locator(locator_name))))
            elif str(locator_name).endswith('XPATH'):
                element = WebDriverWait(self.driver, time_in_seconds).until(
                    expected_conditions.visibility_of_element_located((By.XPATH, self.get_locator(locator_name))))
            elif str(locator_name).endswith('CSS'):
                element = WebDriverWait(self.driver, time_in_seconds).until(
                    expected_conditions.visibility_of_element_located(
                        (By.CSS_SELECTOR, self.get_locator(locator_name))))
            elif str(locator_name).endswith('NAME'):
                element = WebDriverWait(self.driver, time_in_seconds).until(
                    expected_conditions.visibility_of_element_located((By.NAME, self.get_locator(locator_name))))
            elif str(locator_name).endswith('TAG_NAME'):
                element = WebDriverWait(self.driver, time_in_seconds).until(
                    expected_conditions.visibility_of_element_located((By.TAG_NAME, self.get_locator(locator_name))))
            elif str(locator_name).endswith('CLASS_NAME'):
                element = WebDriverWait(self.driver, time_in_seconds).until(
                    expected_conditions.visibility_of_element_located((By.CLASS_NAME, self.get_locator(locator_name))))
            elif str(locator_name).endswith('LINK_TEXT'):
                element = WebDriverWait(self.driver, time_in_seconds).until(
                    expected_conditions.visibility_of_element_located((By.LINK_TEXT, self.get_locator(locator_name))))
            elif str(locator_name).endswith('PARTIAL_LINK_TEXT'):
                element = WebDriverWait(self.driver, time_in_seconds).until(
                    expected_conditions.visibility_of_element_located(
                        (By.PARTIAL_LINK_TEXT, self.get_locator(locator_name))))
            log.info(f'element: {self.get_text(element)} is found successfully')
        except NoSuchElementException as e:
            log.error(
                f"Not able to get element | locator_name: {locator_name} | locator_value: {self.get_locator(locator_name)} | Exception Type: {type(e).__name__}")
        except TimeoutException:
            log.error(
                f"TIME OUT ERROR Occurred! Element not visible | locator_name: {locator_name} | locator_value: {self.get_locator(locator_name)} | wait_time: {time_in_seconds} seconds")
        except Exception as e:
            log.info(
                f"Exception Occurred! | locator_name: {locator_name} | locator_value: {self.get_locator(locator_name)} | wait_time: {time_in_seconds}")
            log.error(f"Exception Type: {type(e).__name__} | Detailed Exception: {e}")
        return element

    def wait_for_element_to_be_visible_with_locator_value(self, locator_value: str, locator_type: str,
                                                          time_in_seconds: int):

        global element
        try:
            if locator_type == 'ID':
                element = WebDriverWait(self.driver, time_in_seconds).until(
                    expected_conditions.visibility_of_element_located((By.ID, locator_value)))
            elif locator_type == 'XPATH':
                element = WebDriverWait(self.driver, time_in_seconds).until(
                    expected_conditions.visibility_of_element_located((By.XPATH, locator_value)))
            elif locator_type == 'CSS':
                element = WebDriverWait(self.driver, time_in_seconds).until(
                    expected_conditions.visibility_of_element_located(
                        (By.CSS_SELECTOR, locator_value)))
            elif locator_type == 'NAME':
                element = WebDriverWait(self.driver, time_in_seconds).until(
                    expected_conditions.visibility_of_element_located((By.NAME, locator_value)))
            elif locator_type == 'TAG_NAME':
                element = WebDriverWait(self.driver, time_in_seconds).until(
                    expected_conditions.visibility_of_element_located((By.TAG_NAME, locator_value)))
            elif locator_type == 'CLASS_NAME':
                element = WebDriverWait(self.driver, time_in_seconds).until(
                    expected_conditions.visibility_of_element_located((By.CLASS_NAME, locator_value)))
            elif locator_type == 'LINK_TEXT':
                element = WebDriverWait(self.driver, time_in_seconds).until(
                    expected_conditions.visibility_of_element_located((By.LINK_TEXT, locator_value)))
            elif locator_type == 'PARTIAL_LINK_TEXT':
                element = WebDriverWait(self.driver, time_in_seconds).until(
                    expected_conditions.visibility_of_element_located(
                        (By.PARTIAL_LINK_TEXT, locator_value)))
            log.info(f'element: {self.get_text(element)} is found successfully')
        except NoSuchElementException as e:
            log.error(
                f"Not able to get element | locator_value: {self.get_locator(locator_value)} | locator_type: {locator_type} | Exception Type: {type(e).__name__}")
        except TimeoutException:
            log.error(
                f"TIME OUT ERROR Occurred! Element not visible | locator_value: {locator_value} | locator_type: {locator_type} | wait_time: {time_in_seconds} seconds")
        except Exception as e:
            log.info(
                f"Exception Occurred! | locator_value: {locator_value} | wait_time: {time_in_seconds}")
            log.error(f"Exception Type: {type(e).__name__} | Detailed Exception: {e}")
        return element

    def wait_for_all_elements_to_be_visible(self, locator_name: str, time_in_seconds: int):

        global element_list
        try:
            if str(locator_name).endswith('ID'):
                element_list = WebDriverWait(self.driver, time_in_seconds).until(
                    expected_conditions.visibility_of_all_elements_located((By.ID, self.get_locator(locator_name))))
            elif str(locator_name).endswith('XPATH'):
                element_list = WebDriverWait(self.driver, time_in_seconds).until(
                    expected_conditions.visibility_of_all_elements_located((By.XPATH, self.get_locator(locator_name))))
            elif str(locator_name).endswith('CSS'):
                element_list = WebDriverWait(self.driver, time_in_seconds).until(
                    expected_conditions.visibility_of_all_elements_located(
                        (By.CSS_SELECTOR, self.get_locator(locator_name))))
            elif str(locator_name).endswith('NAME'):
                element_list = WebDriverWait(self.driver, time_in_seconds).until(
                    expected_conditions.visibility_of_all_elements_located((By.NAME, self.get_locator(locator_name))))
            elif str(locator_name).endswith('TAG_NAME'):
                element_list = WebDriverWait(self.driver, time_in_seconds).until(
                    expected_conditions.visibility_of_all_elements_located(
                        (By.TAG_NAME, self.get_locator(locator_name))))
            elif str(locator_name).endswith('CLASS_NAME'):
                element_list = WebDriverWait(self.driver, time_in_seconds).until(
                    expected_conditions.visibility_of_all_elements_located(
                        (By.CLASS_NAME, self.get_locator(locator_name))))
            elif str(locator_name).endswith('LINK_TEXT'):
                element_list = WebDriverWait(self.driver, time_in_seconds).until(
                    expected_conditions.visibility_of_all_elements_located(
                        (By.LINK_TEXT, self.get_locator(locator_name))))
            elif str(locator_name).endswith('PARTIAL_LINK_TEXT'):
                element_list = WebDriverWait(self.driver, time_in_seconds).until(
                    expected_conditions.visibility_of_all_elements_located(
                        (By.PARTIAL_LINK_TEXT, self.get_locator(locator_name))))
            log.info('all elements are found successfully')
        except TimeoutException:
            log.error(
                f"TIME OUT ERROR Occurred! All Elements not visible | locator_name: {locator_name} | locator_value: {self.get_locator(locator_name)} | wait_time: {time_in_seconds} seconds")
        except Exception as e:
            log.info(
                f"Exception Occurred! | locator_name: {locator_name} | locator_value: {self.get_locator(locator_name)} | wait_time: {time_in_seconds}")
            log.error(f"Exception Type: {type(e).__name__} | Detailed Exception: {e}")

        return element_list

    def wait_for_element_to_be_clickable(self, locator_name: str, time_in_seconds: int):

        global element
        try:
            if str(locator_name).endswith('ID'):
                element = WebDriverWait(self.driver, time_in_seconds).until(
                    expected_conditions.element_to_be_clickable((By.ID, self.get_locator(locator_name))))
            elif str(locator_name).endswith('XPATH'):
                element = WebDriverWait(self.driver, time_in_seconds).until(
                    expected_conditions.element_to_be_clickable((By.XPATH, self.get_locator(locator_name))))
            elif str(locator_name).endswith('CSS'):
                element = WebDriverWait(self.driver, time_in_seconds).until(
                    expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, self.get_locator(locator_name))))
            elif str(locator_name).endswith('NAME'):
                element = WebDriverWait(self.driver, time_in_seconds).until(
                    expected_conditions.element_to_be_clickable((By.NAME, self.get_locator(locator_name))))
            elif str(locator_name).endswith('TAG_NAME'):
                element = WebDriverWait(self.driver, time_in_seconds).until(
                    expected_conditions.element_to_be_clickable((By.TAG_NAME, self.get_locator(locator_name))))
            elif str(locator_name).endswith('CLASS_NAME'):
                element = WebDriverWait(self.driver, time_in_seconds).until(
                    expected_conditions.element_to_be_clickable((By.CLASS_NAME, self.get_locator(locator_name))))
            elif str(locator_name).endswith('LINK_TEXT'):
                element = WebDriverWait(self.driver, time_in_seconds).until(
                    expected_conditions.element_to_be_clickable((By.LINK_TEXT, self.get_locator(locator_name))))
            elif str(locator_name).endswith('PARTIAL_LINK_TEXT'):
                element = WebDriverWait(self.driver, time_in_seconds).until(
                    expected_conditions.element_to_be_clickable((By.PARTIAL_LINK_TEXT, self.get_locator(locator_name))))
                log.info(f'clickable element: {self.get_text(element)} is found successfully')
        except TimeoutException:
            log.error(
                f"TIME OUT ERROR Occurred! Element not clickable | locator_name: {locator_name} | locator_value: {self.get_locator(locator_name)} | wait_time: {time_in_seconds} seconds")
        except Exception as e:
            log.info(
                f"Exception Occurred! | locator_name: {locator_name} | locator_value: {self.get_locator(locator_name)} | wait_time: {time_in_seconds}")
            log.error(f"Exception Type: {type(e).__name__} | Detailed Exception: {e}")

        return element

    def wait_for_element_to_be_clickable_with_locator_value(self, locator_value: str, locator_type: str,
                                                            time_in_seconds: int):

        global element
        try:
            if locator_type == 'ID':
                element = WebDriverWait(self.driver, time_in_seconds).until(
                    expected_conditions.element_to_be_clickable((By.ID, locator_value)))
            elif locator_type == 'XPATH':
                element = WebDriverWait(self.driver, time_in_seconds).until(
                    expected_conditions.element_to_be_clickable((By.XPATH, locator_value)))
            elif locator_type == 'CSS':
                element = WebDriverWait(self.driver, time_in_seconds).until(
                    expected_conditions.element_to_be_clickable(
                        (By.CSS_SELECTOR, locator_value)))
            elif locator_type == 'NAME':
                element = WebDriverWait(self.driver, time_in_seconds).until(
                    expected_conditions.element_to_be_clickable((By.NAME, locator_value)))
            elif locator_type == 'TAG_NAME':
                element = WebDriverWait(self.driver, time_in_seconds).until(
                    expected_conditions.element_to_be_clickable((By.TAG_NAME, locator_value)))
            elif locator_type == 'CLASS_NAME':
                element = WebDriverWait(self.driver, time_in_seconds).until(
                    expected_conditions.element_to_be_clickable((By.CLASS_NAME, locator_value)))
            elif locator_type == 'LINK_TEXT':
                element = WebDriverWait(self.driver, time_in_seconds).until(
                    expected_conditions.element_to_be_clickable((By.LINK_TEXT, locator_value)))
            elif locator_type == 'PARTIAL_LINK_TEXT':
                element = WebDriverWait(self.driver, time_in_seconds).until(
                    expected_conditions.element_to_be_clickable(
                        (By.PARTIAL_LINK_TEXT, locator_value)))
            log.info(f'clickable element: {self.get_text(element)} is found successfully')
        except NoSuchElementException as e:
            log.error(
                f"Not able to get clickable element | locator_value: {self.get_locator(locator_value)} | locator_type: {locator_type} | Exception Type: {type(e).__name__}")
        except TimeoutException:
            log.error(
                f"TIME OUT ERROR Occurred! Element not clickable | locator_value: {locator_value} | locator_type: {locator_type} | wait_time: {time_in_seconds} seconds")
        except Exception as e:
            log.info(
                f"Exception Occurred! | locator_value: {locator_value} | wait_time: {time_in_seconds}")
            log.error(f"Exception Type: {type(e).__name__} | Detailed Exception: {e}")
        return element

    def get_title(self):
        return self.driver.title

    def get_present_url(self):
        return self.driver.current_url

    def click(self, element):
        try:
            log.info(f'element: {self.get_text(element)}')
            element.click()
            log.info(f'element is clicked successfully')
        except Exception as e:
            log.error(
                f"Not able to click element: {element.text} | Exception Type: {type(e).__name__} | Detailed Exception: {e}")

    def right_click(self, element):
        try:
            log.info(f'element: {self.get_text(element)}')
            ActionChains(self.driver).context_click(element).perform()
            log.info(f'element: {element.text} is right-clicked successfully')
        except Exception as e:
            log.error(
                f"Not able to right-click element: {element.text} | Exception Type: {type(e).__name__} | Detailed Exception: {e}")

    def double_click(self, element):
        try:
            log.info(f'element: {self.get_text(element)}')
            ActionChains(self.driver).double_click(element).perform()
            log.info(f'element: {element.text} is double-clicked successfully')
        except Exception as e:
            log.error(
                f"Not able to double click element: {element.text} | Exception Type: {type(e).__name__} | Detailed Exception: {e}")

    def hover_and_click(self, element):
        try:
            log.info(f'element: {self.get_text(element)}')
            ActionChains(self.driver).move_to_element(element).click().perform()
            log.info("Successfully hovered to and clicked an element")
        except MoveTargetOutOfBoundsException as e:
            log.error(
                f"Not able to hover and click element: {element.text} | Exception Type: {type(e).__name__} ")
        except Exception as e:
            log.error(
                f"Not able to hover and click element | Exception Type: {type(e).__name__} | Detailed Exception: {e}")

    def hover_on_element(self, element):
        try:
            log.info(f'element: {self.get_text(element)}')
            ActionChains(self.driver).move_to_element(element).perform()
            log.info(f"successfully hovered to an element: {element.text}")
        except MoveTargetOutOfBoundsException as e:
            log.error(
                f"Not able to hover on element: {element.text} | Exception Type: {type(e).__name__} ")
        except Exception as e:
            log.error(
                f"Not able to hovering on element: {(element.text)}  | Exception Type: {type(e).__name__} | Detailed Exception: {e}")

    def drag_and_drop(self, source_element, target_element):
        try:
            log.info(
                f'source element: {self.get_text(source_element)} | target element: {self.get_text(target_element)}')
            ActionChains(self.driver).drag_and_drop(source_element, target_element).perform()
            log.info(f'drag {source_element.text} and drop to {target_element.text} operation is successful')
        except Exception as e:
            log.error(
                f'drag {source_element.text} and drop to {target_element.text} operation is successful | Detailed Exception: {e}')

    def type(self, element, value):
        try:
            element.send_keys(value)
            log.info(f'successfully typed {value}')
        except Exception as e:
            log.error(f"Not able to type {value} | Exception Type: {type(e).__name__} | Detailed Exception: {e}")

    def type_using_JS(self, locator_name, value):
        try:
            log.info(f'element: {self.get_text(element)}')
            locator_id = self.get_locator(locator_name)
            self.driver.execute_script(f"return document.getElementById({locator_id}).value={value}")
            log.info(f'successfully typed {value}')
        except Exception as e:
            log.error(f"Not able to type {value} | Exception Type: {type(e).__name__} | Detailed Exception: {e}")

    def select_from_dropdown(self, element, value):
        try:
            log.info(f'element: {self.get_text(element)}')
            Select(element).select_by_visible_text(value)
            log.info(f'value: {value} from dropdown: {element.text} is selected successfully')
        except Exception as e:
            log.error(
                f"Not able to select value: {value} from dropdown: {element.text} | Exception Type: {type(e).__name__} | Detailed Exception: {e}")

    def press_enter(self, element):
        try:
            log.info(f'element: {self.get_text(element)}')
            element.send_keys(Keys.ENTER)
            log.info(f'ENTER pressed successfully on element')
        except Exception as e:
            log.error(
                f"Not able to press ENTER on element: {element.text} | Exception Type: {type(e).__name__} | Detailed Exception: {e}")

    def press_down_arrow(self, element):
        try:
            log.info(f'element: {self.get_text(element)}')
            element.send_keys(Keys.DOWN)
            log.info(f'DOWN ARROW pressed successfully on element:')
        except Exception as e:
            log.error(
                f"Not able to press DOWN ARROW on element: | Exception Type: {type(e).__name__} | Detailed Exception: {e}")

    def press_up_arrow(self, element):
        try:
            log.info(f'element: {self.get_text(element)}')
            element.send_keys(Keys.UP)
            log.info(f'UP ARROW pressed successfully on element:')
        except Exception as e:
            log.error(
                f"Not able to press UP ARROW on element: {element.text} | Exception Type: {type(e).__name__} | Detailed Exception: {e}")

    def scroll_to_element(self, element):
        try:
            log.info(f'element: {self.get_text(element)}')
            ActionChains(self.driver).scroll_to_element(element).perform()
            log.info(f'scrolled to {element.text} is successfully')
        except MoveTargetOutOfBoundsException as e:
            log.error(
                f"Not able to scroll to element: {element.text} | Exception Type: {type(e).__name__} ")
        except Exception as e:
            log.error(
                f"Not able to scroll to element: {element.text} | Exception Type: {type(e).__name__} | Detailed Exception: {e}")

    def scroll_into_view_JS(self, element):
        try:
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
            log.info(f'successfully scrolled [{self.get_text(element)}] into view')
            self.wait(5)
        except Exception as e:
            log.error(f"Not able to scroll into view | Exception Type: {type(e).__name__} | Detailed Exception: {e}")

    def scroll_into_view_middle_JS(self, element):
        try:
            self.driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center', inline: 'nearest'})", element)
            log.info(f'successfully scrolled [{self.get_text(element)}] into view of the middle of the page')
            self.wait(5)
        except Exception as e:
            log.error(f"Not able to scroll into view of middle of the page | Exception Type: {type(e).__name__} | Detailed Exception: {e}")

    def scroll_to_bottom_of_page_using_JS(self):
        try:
            self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            log.info('Successfully scrolled to bottom of the page')
            self.wait(5)
        except Exception as e:
            log.error(
                f"Not able to scroll to bottom of page | Exception Type: {type(e).__name__} | Detailed Exception: {e}")

    def get_alert(self, alert_text):
        global alert
        try:
            wait.until(expected_conditions.alert_is_present())
            alert = self.driver.switch_to.alert
            text = alert.text
            log.info(f'Alert is found | alert text: {text}')
            assert alert_text == text, f"Alert Text mismatch | Expected: {alert_text} Actual: {text}"
        except Exception as e:
            log.error(f'Getting Alert is failed | Exception Type: {type(e).__name__} | Detailed Exception: {e}')
        return alert

    def accept_alert(self, alert_text):
        alert = self.get_alert(alert_text)
        alert.accept()

    def dismiss_alert(self, alert_text):
        alert = self.get_alert(alert_text)
        alert.dismiss()

    def get_text(self, element):
        return element.text

    def maximize_window(self):
        try:
            self.driver.set_window_size(1980, 1080)
            self.driver.maximize_window()
            log.info('Window is maximized successfully')
            time.sleep(3)
        except Exception as e:
            log.error(f'Maximizing window is failed | Exception Type: {type(e).__name__} | Detailed Exception: {e}')

    def switch_to_frame(self, element):
        try:
            self.driver.switch_to.frame(element)
            log.info('Successfully switched to frame')
        except Exception as e:
            log.error(f'Not able to switch to frame | Exception Type: {type(e).__name__} | Detailed Exception: {e}')

    def switch_to_parent_frame(self):
        try:
            self.driver.switch_to.default_content()
            log.info('Successfully switched to parent frame')
        except Exception as e:
            log.error(
                f'Not able to switch to parent frame | Exception Type: {type(e).__name__} | Detailed Exception: {e}')

    def switch_to_active_element(self):
        try:
            element = self.driver.switch_to.active_element()
            log.info('Successfully switched to element')
            return element
        except Exception as e:
            log.error(f'Not able to switch to element | Exception Type: {type(e).__name__} | Detailed Exception: {e}')
        return None

    def switch_to_first_child_window(self):
        log.info(f'switching to first child window')
        self.driver.switch_to.window(self.driver.window_handles[1])
        log.info(f'successfully switched to first child window: {self.get_title()}')

    def switch_back_to_parent_window(self):
        log.info(f'switching back to parent window')
        self.driver.switch_to.window(self.driver.window_handles[0])
        log.info('successfully switched back to parent window')
