from pages.base_page import BasePage


class AlertsTab(BasePage):
    URL = "https://demoqa.com/alerts"

    ALERT_BUTTON_LOCATOR = "//*[@id='alertButton']"
    DELAYED_ALERT_BUTTON_LOCATOR = "//*[@id='timerAlertButton']"
    CONFIRMATION_ALERT_BUTTON_LOCATOR = "//*[@id='confirmButton']"
    PROMPT_BOX_ALERT_BUTTON_LOCATOR = "//*[@id='promtButton']"

    CONFIRM_ALERT_RESULT_LOCATOR = "//*[@id='confirmResult']"
    PROMPT_BOX_ALERT_CONFIRMATION_LOCATOR = "//*[@id='promptResult']"

    def navigate(self):
        self.url_open(self.URL)

    def click_and_accept_alert(self):
        self.click(self.ALERT_BUTTON_LOCATOR)
        self.accept_alert()

    def click_and_accept_delayed_alert(self):
        self.click(self.DELAYED_ALERT_BUTTON_LOCATOR)
        self.wait_for_alert_presence()
        self.accept_alert()

    def click_accept_and_decline_alert(self):
        self.click(self.CONFIRMATION_ALERT_BUTTON_LOCATOR)
        self.accept_alert()
        self.wait_for_element_presence(self.CONFIRM_ALERT_RESULT_LOCATOR)
        self.click(self.CONFIRMATION_ALERT_BUTTON_LOCATOR)
        self.decline_alert()
        self.wait_for_element_presence(self.CONFIRM_ALERT_RESULT_LOCATOR)

    def click_alert_and_send_text(self):
        self.click(self.PROMPT_BOX_ALERT_BUTTON_LOCATOR)
        self.send_keys_to_alert('Andrew')
        self.accept_alert()
        self.wait_for_element_presence(self.PROMPT_BOX_ALERT_CONFIRMATION_LOCATOR)

    def check_all_alerts(self):
        try:
            self.click_and_accept_alert()
            self.click_and_accept_delayed_alert()
            self.click_accept_and_decline_alert()
            self.click_alert_and_send_text()
            return True
        except Exception:
            return False
