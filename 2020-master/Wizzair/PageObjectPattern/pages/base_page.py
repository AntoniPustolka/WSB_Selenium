class BasePage():
    """
    Klasa bazowa dla każdej strony
    """
    def __init__(self, driver):
        self.driver = driver
        self._verify_page()

    def _verify_page(self):
        return