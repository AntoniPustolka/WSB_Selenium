import unittest
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# Dane testowe - ("lamerski" hardcode)
valid_name = "Dick"
valid_surname = "Laurent"
gender = 'F'
country_code = '+48'
valid_phone_number = "123123123"
invalid_email = "ssaasdf.pl"
password= "Qwquyqruiy127378698!"
valid_country = "Niemcy"

class WizzairRegistration(unittest.TestCase):
    """
    Scenariusz testowy: Rejestracja nowego użytkownika na stronie wizzair.com
    """
    def setUp(self):
        """
        Warunki wstępne:
        Przeglądarka otwarta na https://wizzair.com/pl-pl/main-page#/
        """
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get("https://wizzair.com/pl-pl/main-page#/")

    def tearDown(self):
        """ Sprzątanie po teście """
        self.driver.quit()


    def test_invalid_email(self):
        """
        Rejestracja nowego użytkownika
        używając adresu email - dane niepoprawne
        (niekompletny email brak '@')
        """
        driver = self.driver
        # KROKI:
        # ======================
        # 1. Kliknij w prawym górnym rogu ZALOGUJ SIĘ
        # Czekam maks. 15 sekund, aż będzie można kliknąć przycisk ZALOGUJ
        # ======================
        zaloguj_btn = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-test="navigation-menu-signin"]')))
        #zaloguj_btn = driver.find_element_by_css_selector('button[data-test="navigation-menu-signin"]')
        zaloguj_btn.click()
        # 2. Kliknij REJESTRACJA
        # ======================
        rejestracja_btn = driver.find_element_by_xpath('//button[text()=" Rejestracja "]')
        rejestracja_btn.click()
         # 3. Wprowadź imię
        imie_field = driver.find_element_by_name("firstName")
        imie_field.send_keys(valid_name)
        # ======================
        # 4. Wprowadź nazwisko
        nazwisko_field = driver.find_element_by_xpath('//input[@placeholder="Nazwisko"]')
        nazwisko_field.send_keys(valid_surname)
        # 5.Wybierz płeć
        # ======================
        if gender == 'M':
            # Wybierz MĘŻCZYZNA
            m = driver.find_element_by_xpath('//label[@for="register-gender-male"]')
            imie_field.click()
            m.click()
        else:
            # WYBIERZ KOBIETA
            f = driver.find_element_by_xpath('//label[@for="register-gender-female"]')
            f.click()
        # ======================
	    # 6.a Wpipsz kod kraju
        cc = driver.find_element_by_xpath('//div[@data-test="booking-register-country-code"]')
        #driver.execute_script("arguments[0].click();", cc)
        # ActionChains(driver).move_to_element(cc).click().perform()
        cc.click()
        cc2 = driver.find_element_by_xpath('//input[@name="phone-number-country-code"]')
        cc2.send_keys(country_code)
        #country_to_choose = WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//li[@class='phone-number__calling-code-selector__dropdown__item']")))
        country_to_choose = WebDriverWait(self.driver, 40).until(EC.element_to_be_clickable((By.XPATH, "//li[@data-test='PL']")))
        country_to_choose.click()
        # 6.b. Wpisz nr telefonu
        driver.find_element_by_name("phoneNumberValidDigits").send_keys(valid_phone_number)
        # ======================
        # 7. Wpisz niepoprawny e-mail (brak '@')
        driver.find_element_by_name("email").send_keys(invalid_email)
        # ======================
        # 8. Wpisz hasło
        driver.find_element_by_name("password").send_keys(password)
        # ======================
        # 9. Wybierz narodowość
        country_field = driver.find_element_by_xpath('//input[@data-test="booking-register-country"]')
        country_field.click()
        # Wyszukaj kraje
        country_to_choose = driver.find_element_by_xpath("//div[@class='register-form__country-container__locations']")
        # Poszukaj elementow "label" wewnatrz listy "countries"
        countries = country_to_choose.find_elements_by_tag_name("label")
        # Iteruj po kazdym elemencie w liscie "countries"
        for label in countries:
            # Wewnatrz "label" znajdz element "strong"
            option=label.find_element_by_tag_name('strong')
            # Jesli tekst elementu jest taki jak zadany w valid_country
            if option.get_attribute("innerText") == valid_country:
                # Przewin do tego elementu
                option.location_once_scrolled_into_view
                # Kliknij
                option.click()
                # Wyjdz z petli - juz znalazlem i kliknalem
                break
        # 10. Zaznacz "Akceptuję Informację o polityce prywatności"
        driver.find_element_by_xpath('//label[@for="registration-privacy-policy-checkbox"][@class="rf-checkbox__label"]').click()
        # 11. Kliknij ZAREJESTRUJ
        driver.find_element_by_xpath('//button[@data-test="booking-register-submit"]').click()
        """TEST: SPRAWDZAMY OCZEKIWANY REZULTAT"""

        # Wyszukuję wszystkie błędy
        error_notices = driver.find_elements_by_xpath('//span[@class="rf-input__error__message"]/span')
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

if __name__ == '__main__':
    unittest.main(verbosity=2)
