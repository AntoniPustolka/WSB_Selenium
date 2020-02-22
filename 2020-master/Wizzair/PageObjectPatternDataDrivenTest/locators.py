from selenium.webdriver.common.by import By

class HomePageLocators():
    """ Selektory strony głównej"""
    ZALOGUJ_BTN = (By.XPATH, '//button[@data-test="navigation-menu-signin"]')

class LoginPageLocators():
    """ Slektory strony logowania"""
    REJESTRACJA_BTN = (By.XPATH, '//button[text()=" Rejestracja "]')

class RegisterPageLocators():
    """ Selektory strony Rejestracja"""
    NAME_INPUT = (By.NAME, "firstName")
    SURNAME_INPUT = (By.NAME, "lastName")
    GENDER_MALE_BTN = (By.XPATH, '//label[@data-test="register-gendermale"]')
    GENDER_FEMALE_BTN = (By.XPATH, '//label[@data-test="register-genderfemale"]')
    COUNTRY_CODE = (By.XPATH, '//div[@class="phone-number__calling-code-selector__empty__placeholder"]')
    COUNTRY_CODE_INPUT = (By.NAME, 'phone-number-country-code')
    COUNTRY_CODE_TO_CHOOSE = (By.XPATH, "//li[@class='phone-number__calling-code-selector__dropdown__item']")
    # Dopisać potrzebne lokatory
    TELEPHONE_INPUT = (By.XPATH, '//input[@data-test="check-in-step-contact-phone-number"]')
    EMAIL_INPUT = (By.XPATH, '//input[@data-test="booking-register-email"]')
    REGISTRATION_ERRORS = (By.XPATH, '//span[@class="rf-input__error__message"]/span')
    PASSWORD_INPUT = (By.XPATH, '//input[@data-test="booking-register-password"]')
    NATIONALITY_INPUT = (By.XPATH, '//input[@data-test="booking-register-country"]')
    COUNTRIES_CONTAINER = (By.XPATH, "//div[@class='register-form__country-container__locations']")
    PRIVACY_POLICY_CHECKBOX = (By.XPATH, "//label[@for='registration-privacy-policy-checkbox'][@class='rf-checkbox__label']")