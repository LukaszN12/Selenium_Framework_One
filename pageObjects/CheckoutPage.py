from selenium.webdriver.common.by import By


class CheckoutPage:

    def __init__(self, driver):
        self.driver = driver

    products = (By.XPATH, "//app-card-list/app-card")
    cardTitle = (By.CSS_SELECTOR, ".card-title")
    add = (By.XPATH, "//button[text() = 'Add ']")
    checkout = (By.CSS_SELECTOR, ".nav-link.btn.btn-primary")
    cart_checkout = (By.CSS_SELECTOR, ".btn.btn-success")

    def cartCheckoutButton(self):
        return self.driver.find_element(*CheckoutPage.cart_checkout)

    def checkoutButton(self):
        return self.driver.find_element(*CheckoutPage.checkout)

    def addIphoneToCart(self):
        products = self.getProducts()
        for product in products:
            if product.find_element(*CheckoutPage.cardTitle).text == 'iphone X':
                product.find_element(*CheckoutPage.add).click()
                break

    def getProducts(self):
        return self.driver.find_elements(*CheckoutPage.products)

    def getProductsTitlesList(self):
        product_list = []
        products = self.getProducts()
        for product in products:
            product_list.append(product.find_element(*CheckoutPage.cardTitle).text)

        return product_list
