from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestTwo(BaseClass):

    def test_hm_data_input(self):

        log = self.getLogger()

        home_page = HomePage(self.driver)

        home_page.getNameInput().send_keys("Jan Kowalski")
        home_page.getEmailInput().send_keys("jankowalski@email.com")
        home_page.getPasswordInput().send_keys("123456")
        home_page.getClickInput().click()
        home_page.getGenderDropdown("Male")
        home_page.getRadioEmployed().click()
        home_page.getBdayInput().send_keys("02011981")
        home_page.getSubmitButton().click()
        success_message = home_page.getSuccessMessage()

        assert "Success!" in success_message, log.error("Wrong success message")

