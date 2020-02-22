from tests.base_test import BaseTest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.register_page import RegisterPage
from test_utils import utils
import unittest
import csv
from ddt import ddt, data, unpack
import os

# Pobierz ten katalog
THIS_DIR = os.path.dirname(os.path.abspath(__file__))
# Dostań się do miejsca, gdzie znajduje się plik csv z danymi
file_path = os.path.join(THIS_DIR, '..', 'test_data/invalid_emails.csv')

@ddt
class RegistrationTest(BaseTest):
    """
    Testy strony Rejestracja
    """
    @data(*utils.get_data(file_path))
    @unpack
    def test_incorrect_email(self, name, surname, country_code, phone, invalid_email, password, country, gender):
        """Test rejestracji nowego użytkownika - błędny e-mail"""
        # Tworzę instancję klasy HomePage, dzięki czemu zyskuję możliwość
        # korzystania z metod w niej zawartych
        hp = HomePage(self.driver)
        hp.click_zaloguj_btn()
        lp = LoginPage(self.driver)
        lp.click_register_btn()
        rp = RegisterPage(self.driver)
        # Wpisz imię
        rp.fill_name(name)
        # Wpisz nazwisko
        rp.fill_surname(surname)
        # Wybierz płeć
        rp.choose_gender(gender)
        # Wybierz kod kraju
        rp.choose_country_code(country_code)
        # Wpisz numer telefonu
        rp.fill_telephone(phone)
        # Wpisz niepoprawny e-mail
        rp.fill_email(invalid_email)
        # Wpisz hasło
        rp.fill_password(password)
        # Wybierz narodowość
        rp.choose_nationality(country)
        # Zaznacz "Akceptuję Informację o polityce prywatności"
        rp.accept_privacy_policy()
        # Kliknij ZAREJESTRUJ [ NIE STOSOWAĆ DLA PRZYPADKU POZYTYWNEGO !!!!]
        # Sprawdź poprawność wyświetlanych błędów
        rp.verify_visible_errors(1, ["Nieprawidłowy adres e-mail"])

if __name__=="__main__":
    unittest.main(verbosity=2)
