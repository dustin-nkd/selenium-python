import time
import pytest_check as check

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

def test_soft_assertions():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://www.google.com/")

    expected_title = "Google Chrome"
    actual_title = driver.title
    check.equal(expected_title, actual_title)

    search_box = driver.find_element(By.XPATH, "//textarea[@id='APjFqb']")
    search_box.send_keys("Selenium")
    search_box.send_keys(Keys.ENTER)
    time.sleep(3)

    driver.quit()