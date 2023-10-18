import time

from pageObjects.CheckoutPage import CheckoutPage
from pageObjects.ConfirmPage import ConfirmPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestOne(BaseClass):

    def test_e2e(self):

        log = self.getLogger()

        home_page = HomePage(self.driver)
        checkout_page = CheckoutPage(self.driver)
        confirm_page = ConfirmPage(self.driver)

        home_page.shopItems().click()
        time.sleep(2)
        products = checkout_page.getProductsTitlesList()
        log.info(products)

        assert 'iphone X' in products, log.error("iphone X nie znajduje się wśród produktów")

        checkout_page.addIphoneToCart()

        checkout_page.checkoutButton().click()
        checkout_page.cartCheckoutButton().click()
        confirm_page.getInput().send_keys("land")
        time.sleep(3)
        countries_list = confirm_page.getCountriesList()
        log.info(countries_list)

        assert 'Poland' in countries_list, log.error("Poland nie znajduje się na liście krajów")

        confirm_page.getPolandFromList().click()
        confirm_page.getCheckbox().click()
        confirm_page.getPurchaseButton().click()

        success_message = confirm_page.getSuccessMessage()
        log.info(success_message)

        assert 'Success!' in success_message, log.error("Success! nie znajduje się w komunikacie")
