import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.implicitly_wait(5)
wait = WebDriverWait(driver, 10)
#time.sleep(3)
driver.find_element(By.CLASS_NAME, "blinkingText").click()
parent_window = driver.current_window_handle
all_windows = driver.window_handles
driver.switch_to.window(all_windows[1])
para_text = wait.until(EC.visibility_of_element_located((By.XPATH,"//p[@class='im-para red']"))).text
para_list = para_text.split()
username = para_list[4]
driver.switch_to.window(parent_window)
driver.find_element(By.ID,"username").send_keys(username)
driver.find_element(By.ID,"password").send_keys("learning")
driver.find_element(By.ID,"signInBtn").click()
error_message = wait.until(EC.visibility_of_element_located((By.CLASS_NAME,"alert-danger"))).text
time.sleep(10)
print(error_message)