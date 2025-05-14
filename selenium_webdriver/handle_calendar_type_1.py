import time
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://seleniumpractise.blogspot.com/2016/08/how-to-handle-calendar-in-selenium.html")

wait = WebDriverWait(driver, 5)

date_str = "2021-21-12"
formatted_date = datetime.strptime(date_str, "%Y-%d-%m")
day = formatted_date.day
month = formatted_date.month
year = formatted_date.year

print(day, month, year)

driver.find_element(By.ID, "datepicker").click()
wait.until(expected_conditions.visibility_of_element_located((By.ID, "ui-datepicker-div")))

month_mapping = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}

current_month = driver.find_element(By.CSS_SELECTOR, "span.ui-datepicker-month").text
current_month_int = month_mapping[current_month]
print(type(current_month_int))

current_year = driver.find_element(By.CSS_SELECTOR, "span.ui-datepicker-year").text
current_year_int = int(current_year)
print(type(current_year_int))

while current_month_int < month or current_year_int < year:
    driver.find_element(By.XPATH, "//span[contains(text(),'Next')]").click()
    current_month = driver.find_element(By.CSS_SELECTOR, "span.ui-datepicker-month").text
    current_month_int = month_mapping[current_month]
    current_year = driver.find_element(By.CSS_SELECTOR, "span.ui-datepicker-year").text
    current_year_int = int(current_year)

while current_month_int > month or current_year_int > year:
    driver.find_element(By.XPATH, "//span[contains(text(),'Prev')]").click()
    current_month = driver.find_element(By.CSS_SELECTOR, "span.ui-datepicker-month").text
    current_month_int = month_mapping[current_month]
    current_year = driver.find_element(By.CSS_SELECTOR, "span.ui-datepicker-year").text
    current_year_int = int(current_year)

driver.find_element(By.XPATH, f"//td[@data-handler='selectDay']//a[contains(text(),'{day}')]").click()
time.sleep(3)

driver.quit()