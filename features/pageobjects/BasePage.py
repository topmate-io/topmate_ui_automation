import time

from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions, wait

from Utilities import configReader


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def get_locator(self, locator_name):
        locator = configReader.readConfig("locators", locator_name)
        return locator

    def get_element(self, locator_name):
        global element
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

        return element

    def wait(self, time_in_seconds: int):
        time.sleep(time_in_seconds)

    def implicit_wait(self, time_in_seconds: int):
        self.driver.implicitly_wait(time_in_seconds)

    def wait_for_element_to_be_visible(self, locator_name: str, time_in_seconds: int):

        global element
        if str(locator_name).endswith('ID'):
            element = WebDriverWait(self.driver, time_in_seconds).until(
                expected_conditions.visibility_of_element_located((By.ID, self.get_locator(locator_name))))
        elif str(locator_name).endswith('XPATH'):
            element = WebDriverWait(self.driver, time_in_seconds).until(
                expected_conditions.visibility_of_element_located((By.XPATH, self.get_locator(locator_name))))
        elif str(locator_name).endswith('CSS'):
            element = WebDriverWait(self.driver, time_in_seconds).until(
                expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, self.get_locator(locator_name))))
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

        return element

    def wait_for_all_elements_to_be_visible(self, locator_name: str, time_in_seconds: int):

        global element
        if str(locator_name).endswith('ID'):
            element = WebDriverWait(self.driver, time_in_seconds).until(
                expected_conditions.visibility_of_all_elements_located((By.ID, self.get_locator(locator_name))))
        elif str(locator_name).endswith('XPATH'):
            element = WebDriverWait(self.driver, time_in_seconds).until(
                expected_conditions.visibility_of_all_elements_located((By.XPATH, self.get_locator(locator_name))))
        elif str(locator_name).endswith('CSS'):
            element = WebDriverWait(self.driver, time_in_seconds).until(
                expected_conditions.visibility_of_all_elements_located(
                    (By.CSS_SELECTOR, self.get_locator(locator_name))))
        elif str(locator_name).endswith('NAME'):
            element = WebDriverWait(self.driver, time_in_seconds).until(
                expected_conditions.visibility_of_all_elements_located((By.NAME, self.get_locator(locator_name))))
        elif str(locator_name).endswith('TAG_NAME'):
            element = WebDriverWait(self.driver, time_in_seconds).until(
                expected_conditions.visibility_of_all_elements_located((By.TAG_NAME, self.get_locator(locator_name))))
        elif str(locator_name).endswith('CLASS_NAME'):
            element = WebDriverWait(self.driver, time_in_seconds).until(
                expected_conditions.visibility_of_all_elements_located((By.CLASS_NAME, self.get_locator(locator_name))))
        elif str(locator_name).endswith('LINK_TEXT'):
            element = WebDriverWait(self.driver, time_in_seconds).until(
                expected_conditions.visibility_of_all_elements_located((By.LINK_TEXT, self.get_locator(locator_name))))
        elif str(locator_name).endswith('PARTIAL_LINK_TEXT'):
            element = WebDriverWait(self.driver, time_in_seconds).until(
                expected_conditions.visibility_of_all_elements_located(
                    (By.PARTIAL_LINK_TEXT, self.get_locator(locator_name))))

        return element

    def wait_for_element_to_be_clickable(self, locator_name: str, time_in_seconds: int):

        global element
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

        return element

    def get_title(self):
        return self.driver.title

    def get_present_url(self):
        return self.driver.current_url

    def click(self, element):
        element.click()

    def right_click(self, element):
        ActionChains(self.driver).context_click(element).perform()

    def double_click(self, element):
        ActionChains(self.driver).double_click(element).perform()

    def hover_and_click(self, element):
        ActionChains(self.driver).move_to_element(element).click().perform()
        log.logger.info("Moving to an element: " + str(element.text))

    def hover_on_element(self, element):
        ActionChains(self.driver).move_to_element(element).perform()
        log.logger.info("Moving to an element: " + str(element.text))

    def drag_and_drop(self, source_element, target_element):
        ActionChains(self.driver).drag_and_drop(source_element, target_element).perform()

    def type(self, element, value):
        element.send_keys(value)

    def select_from_dropdown(self, element, value):
        Select(element).select_by_visible_text(value)


    def press_enter(self, element):
        element.send_keys(Keys.ENTER)


    def scroll_to_element(self, element):
        ActionChains(self.driver).scroll_to_element(element).perform()

    def get_alert(self, alert_text):
        wait.until(expected_conditions.alert_is_present())
        alert = self.driver.switch_to.alert
        text = alert.text
        print(f'alert text: {text}')
        assert alert_text == text
        return alert

    def accept_alert(self, alert_text):
        alert = self.get_alert(alert_text)
        alert.accept()

    def dismiss_alert(self, alert_text):
        alert = self.get_alert(alert_text)
        alert.dismiss()

    def get_text(self, element):
        return element.text



