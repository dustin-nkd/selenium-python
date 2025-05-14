import time

from selenium import webdriver
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://demo.guru99.com/test/")

actions = ActionChains(driver)

driver.find_element(By.CSS_SELECTOR, "input[name='bdaytime']").send_keys("12212021")
driver.find_element(By.CSS_SELECTOR, "input[name='bdaytime']").send_keys(Keys.TAB)
driver.find_element(By.CSS_SELECTOR, "input[name='bdaytime']").send_keys("1111")
time.sleep(5)

driver.find_element(By.CSS_SELECTOR, "input[name='bdaytime']").send_keys(Keys.TAB)
actions.key_down(Keys.NUMPAD1).key_up(Keys.NUMPAD1).perform()

driver.find_element(By.XPATH, "//input[@name='bdaytime']/following-sibling::input").click()
time.sleep(5)

driver.quit()