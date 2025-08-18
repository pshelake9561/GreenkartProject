from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class PlaceOrder:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.promo_code = (By.CSS_SELECTOR, ".promoCode")
        self.promo_button = (By.CSS_SELECTOR, "button[class='promoBtn']")
        self.promo_info = (By.CSS_SELECTOR, ".promoInfo")
        self.product_price = (By.CSS_SELECTOR, "td:nth-child(5) p")
        self.total_amount = (By.CSS_SELECTOR, ".totAmt")
        self.discounted_amount = (By.CSS_SELECTOR, ".discountAmt")

    def apply_promo_code(self, code):
        self.driver.find_element(*self.promo_code).send_keys(code)
        self.driver.find_element(*self.promo_button).click()
        # time.sleep(5)

        element = self.wait.until(EC.visibility_of_element_located(self.promo_info)).text
        print(element)
        assert "Code applied" in element

    def validate_and_place_order(self):
        prices = self.driver.find_elements(*self.product_price)
        sum = 0
        for price in prices:
            sum = sum + int(price.text)
        total_amt = int(self.driver.find_element(*self.total_amount).text)
        assert sum == total_amt
        total_after_discount = float(self.driver.find_element(*self.discounted_amount).text)
        print(total_after_discount)
        assert total_after_discount < total_amt
