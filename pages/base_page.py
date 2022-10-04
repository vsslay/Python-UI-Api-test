from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains as Actions
from selenium.webdriver.common.alert import Alert
import requests


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    # noinspection PyMethodMayBeStatic
    def _define_locator_type(self, locator):
        if "//" in locator:
            return By.XPATH

    def url_open(self, url):
        self.driver.get(url)

    @staticmethod
    def check_response_code(url, expected_code):
        url_to_open = requests.get(url)
        current_code = url_to_open.status_code
        if current_code == expected_code:
            pass
        else:
            quit(f" Expected code {expected_code}, got code {current_code}")

    def _find_element(self, locator, timeout=10):
        return self.wait_for_element_presence(locator, timeout)

# Waits

    def wait_for_element_presence(self, locator, time=30):
        locator_type = self._define_locator_type(locator)
        element = WebDriverWait(self.driver, time).until(
            ec.presence_of_element_located((locator_type, locator)))
        return element

    def check_if_element_active(self, locator):
        element = self._find_element(locator)
        self.driver.implicitly_wait(10)
        status_of_property = element.get_property('disabled')
        if status_of_property is False:
            pass
        else:
            quit("not active")

    def wait_for_alert_presence(self, time=100):
        WebDriverWait(self.driver, time).until(
            ec.alert_is_present())
        pass

# Actions for elements values

    def get_element_size(self, locator, time=10):
        locator_type = self._define_locator_type(locator)
        element = WebDriverWait(self.driver, time).until(
            ec.presence_of_element_located((locator_type, locator)))
        return element.size

    def get_element_text(self, locator):
        element = self._find_element(locator)
        return element.text

    def send_text(self, locator, text):
        element = self._find_element(locator)
        element.send_keys(text)

    def clear_element_text(self, locator):
        element = self._find_element(locator)
        element.clear()

    def get_element_attribute(self, locator, attribute):
        element = self._find_element(locator)
        element_attribute = element.value_of_css_property(attribute)
        return element_attribute

    def send_value(self, locator, text):
        element = self._find_element(locator)
        self.driver.execute_script(f"arguments[0].value={text};", element)

    def get_element_value(self, locator):
        element = self._find_element(locator)
        element_attribute = element.get_attribute("value")
        return element_attribute

# Clicking actions

    def click(self, locator):
        element = self._find_element(locator)
        element.click()

    def js_click(self, locator):
        element = self._find_element(locator)
        self.driver.execute_script("arguments[0].click()", element)

    def hover_mouse(self, locator):
        element = self._find_element(locator)
        Actions(self.driver).move_to_element(element).perform()

    def double_click(self, locator):
        element = self._find_element(locator)
        Actions(self.driver).double_click(element).perform()

    def left_click(self, locator):
        element = self._find_element(locator)
        Actions(self.driver).click(element).perform()

    def right_click(self, locator):
        element = self._find_element(locator)
        Actions(self.driver).context_click(element).perform()

# Scroll functions

    def scroll_to_element(self, locator):
        element = self._find_element(locator)
        Actions(self.driver).move_to_element(element).perform()

    def scroll_down(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

# Drag and Drop actions

    def drag_and_drop_slider(self, locator):
        element = self._find_element(locator)
        Actions(self.driver).click_and_hold(element).move_by_offset(0.05 * element.size['width'], 0).release().perform()

    def drag_and_drop_object_to_object(self, locator, target_locator):
        element = self._find_element(locator)
        target_element = self._find_element(target_locator)
        Actions(self.driver).drag_and_drop(element, target_element).perform()

    def drag_and_drop_by_coordinates(self, locator, x, y):
        element = self._find_element(locator)
        Actions(self.driver).drag_and_drop_by_offset(element, x, y).perform()

# Press and hold button

    def hold_ctrl(self):
        Actions(self.driver).key_down(Keys.LEFT_CONTROL).perform()

    def stop_hold_ctrl(self):
        Actions(self.driver).key_up(Keys.LEFT_CONTROL).perform()

    def press_tab(self, locator):
        element = self._find_element(locator)
        element.send_keys(Keys.TAB)

    def press_enter(self, locator):
        element = self._find_element(locator)
        element.send_keys(Keys.ENTER)

    def hold_enter(self):
        Actions(self.driver).key_down(Keys.ENTER).perform()

    def stop_hold_enter(self):
        Actions(self.driver).key_up(Keys.ENTER).perform()

# Upload file

    def upload_file(self, locator, path):
        element = self._find_element(locator)
        element.send_keys(path)

# Switch between frames

    def switch_to_iframe(self, locator):
        iframe = self._find_element(locator)
        self.driver.switch_to.frame(iframe)

    def switch_to_default_frame(self):
        self.driver.switch_to.default_content()


# Switch and close window

    def switch_window(self, window_number):
        proper_window = self.driver.window_handles[window_number]
        self.driver.switch_to.window(proper_window)

    def close_window(self):
        window_to_close = self.driver.window_handles[1]
        self.driver.switch_to.window(window_to_close)
        self.driver.close()

# Actions on page

    def refresh_page(self):
        self.driver.refresh()

    def get_back(self):
        self.driver.back()

# Alerts handling

    def accept_alert(self):
        Alert(self.driver).accept()

    def decline_alert(self):
        Alert(self.driver).dismiss()

    def send_keys_to_alert(self, text):
        Alert(self.driver).send_keys(text)

    def get_keys_from_alert(self):
        return Alert(self.driver).text
