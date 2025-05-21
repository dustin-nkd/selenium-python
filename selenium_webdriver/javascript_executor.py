import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://omayo.blogspot.com/")

# driver.execute_script("alert('How are you?')")
# driver.execute_script("prompt('How are you?')")
# driver.execute_script("confirm('How are you?')")

alert_button = driver.find_element(By.CSS_SELECTOR, "#alert1")
# driver.execute_script("arguments[0].click()", alert_button)
time.sleep(3)

def highlight_an_element(element):
    driver.execute_script("arguments[0].style.border='3px solid red';", element)

highlight_an_element(alert_button)
time.sleep(3)

page_title = str(driver.execute_script("return document.title;"))
print(page_title)

current_url = str(driver.execute_script("return document.URL;"))
print(current_url)

search_box = driver.find_element(By.CSS_SELECTOR, "input[title='search'][name='q']")
driver.execute_script("arguments[0].value='content';", search_box)
time.sleep(3)

driver.execute_script("history.go(0);")

dropdown_button = driver.find_element(By.CSS_SELECTOR, ".dropbtn")
driver.execute_script("arguments[0].scrollIntoView();", dropdown_button)
time.sleep(3)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(3)

paragraph = driver.find_element(By.XPATH, "//div[contains(text(),'This is a sample text in the Page One.')]")
text = driver.execute_script("return arguments[0].innerText;", paragraph)
print(text)

driver.quit()