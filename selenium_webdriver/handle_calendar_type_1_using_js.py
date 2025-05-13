import time

from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://seleniumpractise.blogspot.com/2016/08/how-to-handle-calendar-in-selenium.html")

driver.execute_script("document.getElementById('datepicker').value='12/31/2027'")
time.sleep(3)

driver.quit()