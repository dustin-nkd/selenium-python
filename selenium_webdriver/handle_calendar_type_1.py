import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://seleniumpractise.blogspot.com/2016/08/how-to-handle-calendar-in-selenium.html")

wait = WebDriverWait(driver, 10)

driver.find_element(By.XPATH, "//input[@id='datepicker']").click()
wait.until(expected_conditions.visibility_of_element_located((By.XPATH, "//div[@id='ui-datepicker-div']")))


def select_future_day_in_calender(day, month, year):
    current_month = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
    current_year = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text

    while not (current_month == month and current_year == year):
        driver.find_element(By.XPATH, "//span[text()='Next']").click()
        current_month = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
        current_year = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text

    driver.find_element(By.XPATH, f"//td[@data-handler='selectDay']//a[text()='{day}']").click()
    time.sleep(3)


def select_past_day_in_calender(day, month, year):
    current_month = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
    current_year = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text

    while not (current_month == month and current_year == year):
        driver.find_element(By.XPATH, "//span[text()='Prev']").click()
        current_month = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-month']").text
        current_year = driver.find_element(By.XPATH, "//span[@class='ui-datepicker-year']").text

    driver.find_element(By.XPATH, f"//td[@data-handler='selectDay']//a[text()='{day}']").click()
    time.sleep(3)


select_past_day_in_calender(10, "May", "2021")
driver.quit()