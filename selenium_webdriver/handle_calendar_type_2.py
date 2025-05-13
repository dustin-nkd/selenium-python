import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.path2usa.com/travel-companion/")
time.sleep(5)

driver.find_element(By.ID, "form-field-travel_comp_date").click()
time.sleep(3)

driver.find_element(By.CSS_SELECTOR, "span.arrowUp").click()
current_month = driver.find_element(By.CSS_SELECTOR, "span.cur-month").text.strip()

while not(current_month == "June"):
    driver.find_element(By.CSS_SELECTOR, "span.flatpickr-next-month").click()
    current_month = driver.find_element(By.CSS_SELECTOR, "span.cur-month").text.strip()

time.sleep(3)
driver.find_element(By.XPATH, "//span[@class='flatpickr-day '][text()='30']").click()
time.sleep(3)

driver.quit()