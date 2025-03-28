import time

from selenium import webdriver
from selenium.webdriver.common.by import By

browser = input("please input the name of browser that you want to open with selenium: ")

if browser.lower() == "chrome":
    driver = webdriver.Chrome()
else:
    driver = webdriver.Firefox()

driver.maximize_window()
driver.get("https://omayo.blogspot.com/")

# driver.find_element(By.ID, "ta1").send_keys("My name is Dustin")
# driver.find_element(By.NAME, "q").send_keys("Dustin")
# driver.find_element(By.CLASS_NAME, "gsc-search-button").click()
# driver.find_element(By.XPATH, "//input[@value='Login']").click()
# driver.find_element(By.CSS_SELECTOR, "#alert1").click()

driver.find_element(By.XPATH, "//textarea[@id='ta1']").send_keys("Hi my name is Dustin\n I love to do my job")
driver.find_element(By.NAME, "q").send_keys("Dustin")
driver.find_element(By.CSS_SELECTOR, "form[name='form1'] input[type='password']").send_keys("password")

time.sleep(3)
driver.quit()