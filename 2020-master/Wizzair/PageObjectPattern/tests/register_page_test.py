from tests.base_test import BaseTest
from pages.home_page import HomePage
from pages.login_page import LoginPage
from pages.register_page import RegisterPage
import unittest
import time

class RegistrationTest(BaseTest):
    """
    Testy strony Rejestracja
    """
    def test_incorrect_email(self):
        """Test rejestracji nowego użytkownika - błędny e-mail"""
        # Tworzę instancję klasy HomePage, dzięki czemu zyskuję możliwość
        # korzystania z metod w niej zawartych
        hp = HomePage(self.driver)
        hp.click_zaloguj_btn()
        lp = LoginPage(self.driver)
        lp.click_register_btn()
        rp = RegisterPage(self.driver)
        # Wpisz imię
        rp.fill_name("Przemek")
        # Wpisz nazwisko
        rp.fill_surname("Nowak")
        # Wybierz płeć
        rp.choose_gender("M")
        # Wybierz kod kraju
        rp.choose_country_code("+48")
        # Wpisz numer telefonu
        rp.fill_telephone('321321321')
        # Wpisz niepoprawny e-mail
        rp.fill_email('dddd.pl')
        # Wpisz hasło
        rp.fill_password('Qwessdry123@')
        # Wybierz narodowość
        rp.choose_nationality("Polska")
        # Zaznacz "Akceptuję Informację o polityce prywatności"
        rp.accept_privacy_policy()
        # Kliknij ZAREJESTRUJ [ NIE STOSOWAĆ DLA PRZYPADKU POZYTYWNEGO !!!!]
        # Sprawdź poprawność wyświetlanych błędów
        rp.verify_visible_errors(1, ["Nieprawidłowy adres e-mail"])
        time.sleep(2)



if __name__=="__main__":
    unittest.main(verbosity=2)
