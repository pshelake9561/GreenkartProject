from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.search_text = (By.XPATH, "//input[@type='search']")
        self.product_list = (By.XPATH, "//div[@class='products']/div")
        self.add_to_cart_button = (By.XPATH, "./div/button")
        self.cart = (By.XPATH, "//a[@class='cart-icon']/img")
        self.proceed_to_checkout_btn = (By.XPATH, "//div[@class='cart-preview active']/div/button")
        self.wait = WebDriverWait(self.driver, 10)

    def search_product(self, search_text):
        search_product = self.driver.find_element(*self.search_text)
        search_product.send_keys(search_text)

    def add_to_cart(self):
        results = self.wait.until(EC.presence_of_all_elements_located(self.product_list))
        #results = self.driver.find_elements(*self.product_list)
        for result in results:
            result.find_element(By.XPATH, "./div/button").click()

    def proceed_to_checkout(self):
        cart_button = self.wait.until(EC.presence_of_element_located(self.cart))
        cart_button.click()
        checkout_button = self.wait.until(EC.presence_of_element_located(self.proceed_to_checkout_btn))
        checkout_button.click()


