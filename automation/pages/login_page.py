from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from automation.pages.base_page import BasePage


class LoginPage(BasePage):

    URL = "https://balashanmugam-rathinam.github.io/selenium-project/"

    USERNAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-btn")

    def open(self):
        self.driver.get(self.URL)

    def login(self, username, password):
        # ✅ WAIT for username field
        WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located(self.USERNAME)
        )

        self.type(*self.USERNAME, username)
        self.type(*self.PASSWORD, password)
        self.click(*self.LOGIN_BTN)