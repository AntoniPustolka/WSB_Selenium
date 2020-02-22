from pages.base_page import BasePage
from locators import RegisterPageLocators
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class RegisterPage(BasePage):
    def fill_name(self, name):
        el = self.driver.find_element(*RegisterPageLocators.NAME_INPUT)
        el.send_keys(name)

    def fill_surname(self, surname):
        el = self.driver.find_element(*RegisterPageLocators.SURNAME_INPUT)
        el.send_keys(surname)

    def choose_gender(self, gender):
        if gender == "M":
            # Wybierz męzczyzne
            self.driver.find_element(*RegisterPageLocators.NAME_INPUT).click()
            # odszukaj przycisk Mężczyzna
            self.driver.find_element(*RegisterPageLocators.GENDER_MALE_BTN).click()
            # Kliknij w niego
        else:
            #Wybierz kobietę
            self.driver.find_element(*RegisterPageLocators.GENDER_FEMALE_BTN).click()

    def choose_country_code(self, country_code):
        self.driver.find_element(*RegisterPageLocators.COUNTRY_CODE).click()
        self.driver.find_element(*RegisterPageLocators.COUNTRY_CODE_INPUT).send_keys(country_code)
        WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable(RegisterPageLocators.COUNTRY_CODE_TO_CHOOSE))
        self.driver.find_element(*RegisterPageLocators.COUNTRY_CODE_TO_CHOOSE).click()

    def fill_telephone(self, telephone_number):
        self.driver.find_element(*RegisterPageLocators.TELEPHONE_INPUT).send_keys(telephone_number)

    def choose_nationality(self, nationality):
        country_field = self.driver.find_element(*RegisterPageLocators.NATIONALITY_INPUT)
        country_field.click()
        # Wyszukaj kraje
        country_to_choose = self.driver.find_element(*RegisterPageLocators.COUNTRIES_CONTAINER)
        countries = country_to_choose.find_elements_by_xpath("label")
        for label in countries:
            option = label.find_element_by_tag_name('strong')
            # print(d.text)
            if option.get_attribute("innerText") == nationality:
                option.location_once_scrolled_into_view
                option.click()
                break

    def fill_email(self, email):
        self.driver.find_element(*RegisterPageLocators.EMAIL_INPUT).send_keys(email)

    def fill_password(self, password):
        self.driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(password)

    def accept_privacy_policy(self):
        self.driver.find_element(*RegisterPageLocators.PRIVACY_POLICY_CHECKBOX).click()


    def verify_visible_errors(self, number_of_errors, errors_texts):
        error_notices = self.driver.find_elements(*RegisterPageLocators.REGISTRATION_ERRORS)
        visible_error_notices = []
        # Zapisuję widoczne błędy do listy visible_error_notices
        for error in error_notices:
            if error.is_displayed():
                visible_error_notices.append(error)
        # Sprawdzam, czy widoczna jest właściwa liczba błędów
        assert len(visible_error_notices) == number_of_errors
        # Sprawdzam treść widocznych błędów
        errors_text_fact = []
        for i in range(len(visible_error_notices)):
            errors_text_fact.append(visible_error_notices[i].get_attribute("innerText") )
        print(errors_text_fact)
        print(errors_texts)
        assert errors_text_fact == errors_texts
