import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://www.hyrtutorials.com/p/calendar-practice.html")

wait = WebDriverWait(driver, 10)

driver.find_element(By.ID, "third_date_picker").click()
wait.until(expected_conditions.visibility_of_element_located((By.ID, "ui-datepicker-div")))

month_dropdown = driver.find_element(By.XPATH, "//select[@data-handler='selectMonth']")
month = Select(month_dropdown)
month.select_by_visible_text("Jun")

year_dropdown = driver.find_element(By.XPATH, "//select[@data-handler='selectYear']")
year = Select(year_dropdown)
year.select_by_visible_text("2025")

driver.find_element(By.XPATH, "//td[@data-handler='selectDay']/a[contains(.,'30')]").click()
time.sleep(3)

driver.quit()