# TEST CASE 1 - REGISTRATION ON WIZZER.COM/pl WITH INVALID EMAIL ADDRESS

import time
import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

firstname = 'Antoni'
lastname = 'Pustolka'
gender = 'male'
countrycode = '+48'
phonenumber = '576995500'
invalidemail = 'miszczcom.pl'
password = '123456aa5'
validcountry = 'Polska'

class WizzarRegistration(unittest.TestCase):

        # Przegladarka wlaczona na Wizzair.com
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

        # Visit the portal
        self.driver.get('https://wizzair.com/pl-pl/')
        driver = self.driver

        # and go to registration page
    def testRegistration(self):
        zaloguj_btn = WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//button[@data-test="navigation-menu-signin"]')))
        zaloguj_btn.click()

        # click on the Registration
        rejestracja =WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[text()= " Rejestracja "]')))
        rejestracja.click()

        # Wprowadz imie
        fn = WebDriverWait(self.driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//input[@name = "firstName"][@data-test="registrationmodal-first-name-input"]')))

        fn.send_keys(firstname)

        # Wprowasz nazwisko
        self.driver.find_element_by_name('lastName').send_keys(lastname)

        # Wybierz GENDER

        if gender == 'male':
            m = self.driver.find_element_by_xpath('//label[@data-test="register-gendermale"]')
            fn.click()
            m.click()
        else:
            self.driver.find_element_by_xpath('//label[@data-test="register-genderfemale"]').click()

        # Wybierz CountryCode
        cc =self.driver.find_element_by_xpath('//div[@data-test="booking-register-country-code"]')
        cc.click()
        cc2 = WebDriverWait(self.driver, 15).until(EC.element_to_be_clickable((By.XPATH, '//input[@name = "phone-number-country-code"]')))
        cc2.send_keys(countrycode)

        # Wpisz nr. telefonu

        no = self.driver.find_element_by_xpath('//input[@name="phoneNumberValidDigits"]')
        no.send_keys(phonenumber)

        # Podaj invalid email
        self.driver.find_element_by_name("email").send_keys(invalidemail)

        # Podaj haslo
        self.driver.find_element_by_name("password").send_keys(password)

        # Wybierz narodowośc
        country_to_choose = self.driver.find_element_by_xpath("//div[@class='register-form__country-container__locations']")
        # Poszukaj elementow "label" wewnatrz listy "countries"
        countries = country_to_choose.find_elements_by_tag_name("label")
        # Iteruj po kazdym elemencie w liscie "countries"
        for label in countries:
            # Wewnatrz "label" znajdz element "strong"
            option=label.find_element_by_tag_name('strong')
            # Jesli tekst elementu jest taki jak zadany w valid_country
            if option.get_attribute("innerText") == validcountry:
                # Przewin do tego elementu
                option.location_once_scrolled_into_view
                # Klikni
                option.click()
                # Wyjdz z petli - juz znalazlem i kliknalem
                break
        # Zatwierdz Subskrycja
        self.driver.find_element_by_xpath('//label[@for="registration-special-offers-checkbox"]').click()
        # Akceptuj RODO
        self.driver.find_element_by_xpath('//label[@for="registration-privacy-policy-checkbox"]').click()
        # Kliknij ZAREJESTRUJ
        selfe.driver.find_element_by_xpath('//button[@data-test="booking-register-submit"]').click()
        # Zbierz informacje o bledach
        # Wyszukuję wszystkie błędy
        error_notices = self.driver.find_elements_by_xpath('//span[@class="rf-input__error__message"]/span')
        # Zapisuję widoczne błędy do listy visible_error_notices
        visible_error_notices = []
        for error in error_notices:
            # Jesli jest widoczny, to dodaj do listy
            if error.is_displayed():
                visible_error_notices.append(error)
        # Sprawdzam, czy widoczny jest tylko jeden błąd
        assert len(visible_error_notices) == 1
        # Sprawdzam treść widocznego błędu
        error_text = visible_error_notices[0].get_attribute("innerText")
        assert error_text == "Nieprawidłowy adres e-mail"

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main(verbosity=2)
