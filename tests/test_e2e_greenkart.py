import json
import time
import pytest


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pageObject.HomePage import HomePage
from pageObject.PlaceOrder import PlaceOrder
filepath = '../data/test_e2e_data.json'
with open(filepath) as f:
    data_load = json.load(f)
    data_list = data_load["data"]

@pytest.mark.parametrize("data_list_item", data_list)
def test_e2e(setup,config_env, data_list_item):
    driver = setup
    base_url = config_env.get('base_url')
    driver.get(base_url)
    #driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
    home = HomePage(driver)
    home.search_product(data_list_item["search_text"])
    time.sleep(3)
    home.add_to_cart()
    #time.sleep(3)
    home.proceed_to_checkout()
    order = PlaceOrder(driver)
    order.apply_promo_code(data_list_item["promo_code"])
    order.validate_and_place_order()


    #assert items_list == actual_list