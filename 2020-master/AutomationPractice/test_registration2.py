# Import modulu unittest
import unittest
# Import webdrivera
from selenium import webdriver
import time
from selenium.webdriver.support.ui import Select

email= "tester@wsb.pl"
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
class APRegistration(unittest.TestCase):
    """Analogia: Przypadek/scenariusz testowy"""
    # Przygotowanie dla calej klasy (scenariusza testowego)
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Firefox()
        cls.driver.maximize_window()
        cls.driver.implicitly_wait(15)
    # Przygotowanie do kazdego testu
    # (Warunki wstepne)
    def setUp(self):
        self.driver.get('http://automationpractice.com/index.php')
        # Czekaj max 5 sekund na elementy
    # Sprzatanie po kazdym tescie
    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

    #Wlasciwy test
    # nazwa musi zaczynac sie od slowa test
    def testNoName(self):
        # 1. Kliknij login
        driver = self.driver
        signin = driver.find_element_by_class_name("login")
        signin.click()
        # 2. Wpisz email
        email_input = driver.find_element_by_id("email_create")
        email_input.send_keys(email)
        # 3. Kliknij Create account
        create_account_btn = driver.find_element_by_id("SubmitCreate")
        create_account_btn.click()
        # 4. Wybierz plec
        if gender == "male":
            driver.find_element_by_id("id_gender1").click()
        elif gender=="female":
            driver.find_element_by_id("id_gender2").click()
                # 6. Wpisz nazwisko
        driver.find_element_by_id("customer_lastname").send_keys(surname)
        # 5. Sprawdz email
        # Pobierz atrubut value z webelementu
        email_fact = driver.find_element_by_id("email").get_attribute("value")
        # Wypisz te wartosc
        print("W polu jest email: ", email_fact)
        # Porownaj wartosc wyswietlana z wczesniej wpisywana
        assert email_fact == email
        # 6. Wpisz haslo
        driver.find_element_by_id("passwd").send_keys(password)
        # 7. Wpisz date urodzenia
        day =  Select(driver.find_element_by_id("days"))
        day.select_by_value(birth_day)
        month =  Select(driver.find_element_by_id("months"))
        month.select_by_visible_text(birth_month)
        year =  Select(driver.find_element_by_id("years"))
        year.select_by_value(birth_year)
        # 8. Sprawdz pole First name
        name_fact = driver.find_element_by_xpath('//input[@id="firstname"]')
        # Przewin do tego webelementu
        # 9. Sprawdz pole Last name
        surname_fact = driver.find_element_by_xpath('//input[@name="lastname"]').get_attribute("value")
        print("W polu jest nazwisko: ", surname_fact)
        assert surname == surname_fact
        # 10. Wpisz adres
        driver.find_element_by_id('address1').send_keys(address)
        # 11. Wpisz miasto
        driver.find_element_by_id('city').send_keys(city)
        # 12. Wpisz kod pocztowy
        driver.find_element_by_id('postcode').send_keys(postcode)
        # 13. Wybierz stan
        state_select =  Select(driver.find_element_by_id("id_state"))
        state_select.select_by_visible_text("Alabama")
        # 14. Wpisz numer telefonu
        driver.find_element_by_id('phone_mobile').send_keys(phone)
        # 15. Wpisz alias adresu
        al = driver.find_element_by_id('alias')
        al.clear()
        al.send_keys(alias)
        # 16. Kliknij Register
        driver.find_element_by_id('submitAccount').click()
        # Pobierz bledy
        errors = driver.find_elements_by_xpath('//div[@class="alert alert-danger"]/ol')
        # Sprawdz, czy jest jeden blad
        assert len(errors) == 1
        # Pobierz jego tekst
        error_text = errors[0].get_attribute('innerText')
        # Sprawdz, czy jest wyswietlony
        assert errors[0].is_displayed()
        # Sprawdz jego poprawnosc
        assert "firstname is required" in error_text

    @unittest.skip
    def testCorrectRegistration(self):
        # 1. Kliknij login
        driver = self.driver
        signin = driver.find_element_by_class_name("login")
        signin.click()
        # 2. Wpisz email
        email_input = driver.find_element_by_id("email_create")
        email_input.send_keys(email)
        # 3. Kliknij Create account
        create_account_btn = driver.find_element_by_id("SubmitCreate")
        create_account_btn.click()
        # 4. Wybierz plec
        if gender == "male":
            driver.find_element_by_id("id_gender1").click()
        elif gender=="female":
            driver.find_element_by_id("id_gender2").click()
        # 5. Wpisz imie
        driver.find_element_by_id("customer_firstname").send_keys(name)
        # 6. Wpisz nazwisko
        driver.find_element_by_id("customer_lastname").send_keys(surname)
        # 7. Sprawdz email
        # Pobierz atrubut value z webelementu
        email_fact = driver.find_element_by_id("email").get_attribute("value")
        # Wypisz te wartosc
        print("W polu jest email: ", email_fact)
        # Porownaj wartosc wyswietlana z wczesniej wpisywana
        assert email_fact == email
        # 8. Wpisz haslo
        driver.find_element_by_id("passwd").send_keys(password)
        # 9. Wpisz date urodzenia
        day =  Select(driver.find_element_by_id("days"))
        day.select_by_value(birth_day)
        month =  Select(driver.find_element_by_id("months"))
        month.select_by_visible_text(birth_month)
        year =  Select(driver.find_element_by_id("years"))
        year.select_by_value(birth_year)
        # 10. Sprawdz pole First name
        name_fact = driver.find_element_by_xpath('//input[@id="firstname"]')
        # Przewin do tego webelementu
        name_fact.location_once_scrolled_into_view
        name_fact=name_fact.get_attribute("value")
        print("W polu jest imie: ", name_fact)
        # Porownaj imie, ktore wpisywalismy z tym wyswietlonym w polu
        assert name == name_fact
        # 11. Sprawdz pole Last name
        surname_fact = driver.find_element_by_xpath('//input[@name="lastname"]').get_attribute("value")
        print("W polu jest nazwisko: ", surname_fact)
        assert surname == surname_fact
        # 12. Wpisz adres
        driver.find_element_by_id('address1').send_keys(address)
        # 13. Wpisz miasto
        driver.find_element_by_id('city').send_keys(city)
        # 14. Wpisz kod pocztowy
        driver.find_element_by_id('postcode').send_keys(postcode)
        # 15. Wybierz stan
        state_select =  Select(driver.find_element_by_id("id_state"))
        state_select.select_by_visible_text("Alabama")
        # 16. Wpisz numer telefonu
        driver.find_element_by_id('phone_mobile').send_keys(phone)
        # 17. Wpisz alias adresu
        al = driver.find_element_by_id('alias')
        al.clear()
        al.send_keys(alias)
        # 18. Kliknij Register
        # Nie robimy, zeby nie zakladac naprawde konta
        print("NIE KLIKAM ZAREJESTRUJ")

# Uruchom test jesli uruchamiamy
# ten plik
if __name__ == "__main__":
    unittest.main(verbosity=2)
