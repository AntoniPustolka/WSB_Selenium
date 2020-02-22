import unittest
from tests.register_page_test import RegistrationTest

# Pobierz testy, które chcesz uruchomić
registration_test = unittest.TestLoader().loadTestsFromTestCase(RegistrationTest)

# Stwórz Test Suita łączac testy
test_suite = unittest.TestSuite([registration_test])

# odpal
unittest.TextTestRunner(verbosity=2).run(test_suite)
