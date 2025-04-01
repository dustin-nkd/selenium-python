from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://omayo.blogspot.com/")
driver.maximize_window()

value_of_search_button = driver.find_element(By.XPATH, "//input[@value='Search']").get_attribute("value")
print(value_of_search_button)

driver.quit()
