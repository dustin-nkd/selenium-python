from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")

table_headings = driver.find_elements(By.XPATH, "//table[@id='table1']//th ")
for heading in table_headings:
    print(heading.text)
print("-")

table_data = driver.find_elements(By.XPATH, "//table[@id='table1']//td")
for data in table_data:
    print(data.text)
print("-")

first_row_data = driver.find_elements(By.XPATH, "//table[@id='table1']//tr[1]/td")
for data in first_row_data:
    print(data.text)
print("-")

particular_data = driver.find_element(By.XPATH, "//table[@id='table1']//tr[3]/td[2]").text
print(particular_data)
print("-")

third_column_data = driver.find_elements(By.XPATH, "//table[@id='table1']//tr/td[3]")
for data in third_column_data:
    print(data.text)
print("-")

rows = driver.find_elements(By.XPATH, "//table[@id='table1']//tr")
print(len(rows))

cols = driver.find_elements(By.XPATH, "//table[@id='table1']//th")
print(len(cols))

driver.quit()
