from selenium.webdriver.common.by import By


class ConfirmPage:

    def __init__(self, driver):
        self.driver = driver

    success = (By.CSS_SELECTOR, ".alert.alert-success.alert-dismissible")
    checkbox = (By.XPATH, "//label[@for='checkbox2']")
    input = (By.ID, "country")
    countries = (By.XPATH, "//div[@class='suggestions']/ul/li")
    poland = (By.XPATH, "//li/a[text()='Poland']")
    purchase = (By.XPATH, "//input[@value='Purchase']")

    def getSuccessMessage(self):
        return self.driver.find_element(*ConfirmPage.success).text

    def getPurchaseButton(self):
        return self.driver.find_element(*ConfirmPage.purchase)

    def getCheckbox(self):
        return self.driver.find_element(*ConfirmPage.checkbox)

    def getPolandFromList(self):
        return self.driver.find_element(*ConfirmPage.poland)

    def getCountries(self):
        return self.driver.find_elements(*ConfirmPage.countries)

    def getInput(self):
        return self.driver.find_element(*ConfirmPage.input)

    def getCountriesList(self):
        countries = self.getCountries()
        countries_list = []
        for country in countries:
            countries_list.append(country.text)
        return countries_list
