from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class HomePage:

    def __init__(self, driver):
        self.driver = driver

    shop_button = (By.XPATH, "//a[@href='/angularpractice/shop']")
    name_input = (By.XPATH, "(//input[@name='name'])[1]")
    email_input = (By.XPATH, "//input[@name='email']")
    password_input = (By.ID, "exampleInputPassword1")
    click_input = (By.ID, "exampleCheck1")
    gender_dropdown = (By.ID, "exampleFormControlSelect1")
    radio_employed = (By.ID, "inlineRadio2")
    bday_input = (By.XPATH, "//input[@name='bday']")
    submit_button = (By.CSS_SELECTOR, ".btn.btn-success")
    success_message = (By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible")

    def getSuccessMessage(self):
        return self.driver.find_element(*HomePage.success_message).text

    def getSubmitButton(self):
        return self.driver.find_element(*HomePage.submit_button)

    def getBdayInput(self):
        return self.driver.find_element(*HomePage.bday_input)

    def getRadioEmployed(self):
        return self.driver.find_element(*HomePage.radio_employed)

    def getGenderDropdown(self, gender):
        dropdown = Select(self.driver.find_element(*HomePage.gender_dropdown))
        if gender == "Female":
            return dropdown.select_by_visible_text("Female")
        elif gender == "Male":
            return dropdown.select_by_visible_text("Male")

    def getClickInput(self):
        return self.driver.find_element(*HomePage.click_input)

    def getPasswordInput(self):
        return self.driver.find_element(*HomePage.password_input)

    def getEmailInput(self):
        return self.driver.find_element(*HomePage.email_input)

    def getNameInput(self):
        return self.driver.find_element(*HomePage.name_input)

    def shopItems(self):
        return self.driver.find_element(*HomePage.shop_button)
