#!/usr/bin/env python

import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

email= "antoni@wsb.pl"
gender = "male"
name = "Marcin"
surname = "Nowak"
password = "Qwertry123@@"
birth_day = "2"
birth_month = 'January '
birth_year = '2000'
address = "Street 21 New York"
city = "Kozia Wola"
postcode = "23455"
phone = "123123123"
alias = "my alias"

# Tworze klase WsbPlCheck dziedziczaca po
# TestCase z modulu unittest
class Automationpractice_Set_Up(unittest.TestCase):

    # Przygotowanie do kazdego testu
    # (Warunki wstepne)
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.get('http://automationpractice.com/index.php')
        self.browser.maximize_window()
        # Czekaj 5 second
        self.browser.implicitly_wait(5)

        # Sprzatanie po kazdym tescie
    def tearDown(self):
        self.browser.quit()

        # 1. Kliknij "Sign in"
    def testKlik(self):
        driver = self.browser
        signIn = driver.find_element_by_class_name('login')
        signIn.click()

        # 2. Wpisz email
        # 3. Kliknij przycisk create na account
        create_btn = driver.find_element_by_id('SubmitCreate')
        create_btn.click()
        # 4. Wybierz tytuł
        driver.find_element_by_id('id_gender1').click()
        # 5. Napisz moje_imie
        driver.find_element_by_name('customer_firstname').send_keys(firstname)
        # 6. Napisz nazwisko
        driver.find_element_by_name('customer_lastname').send_keys(lastname)
        # 7. Sorawdz poprawnosc linku
        enmail_text = driver.find_element_by_id('email').get_attribute('value')
        assert email_text == email

        # 8. Wpisz niepoprawne haslo
        driver.find_element_by_id('passwd').send_keys(invalid_password)
        # 9. Wybierz date urodzenia
        # Tworrze obiekt klasy Select
        day_of_birth_webelement = Select(driver.find_element_by_id('days'))
        day_of_birth_select = Select(day_of_birth_webelement)
        day_of_birth_select.select_by_value(birthday)


if __name__ == '__main__':
    unittest.main(verbosity=2)
