from pages.base_page import BasePage
from locators import LoginPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage(BasePage):
    def click_register_btn(self):
        el = self.driver.find_element(*LoginPageLocators.REJESTRACJA_BTN)
        el.click()

    def click_agency_login_btn(self):
        pass