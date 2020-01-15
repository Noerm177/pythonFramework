from pages.login_page import LoginPage
import pytest
import unittest


@pytest.mark.usefixtures("one_time_setup", "setUP")
class LoginTest(unittest.TestCase):

    correct_text = "Welcome to the Secure Area. When you are done click logout below."

    @pytest.fixture(autouse=True)
    def class_setup(self, one_time_setup):
        self.lp = LoginPage(self.driver)

    @pytest.mark.run(order=1)
    def test_valid_login(self):
        self.lp.login("tomsmith", "SuperSecretPassword!")
        result = self.lp.verify_login_successful_text(self.correct_text)
        assert result == True

    # @pytest.mark.run(order=2)
    # def test_invalid_login(self):
    #     self.lp.login("badUser", "pass123")
    #     result = self.lp.verify_login_failed()
    #     assert result == True
