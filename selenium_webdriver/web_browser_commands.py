# web_browser_commands.py

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# 1. Set up the WebDriver (Make sure you have the correct driver installed)
print("Example 1: Setting up WebDriver")

driver = webdriver.Chrome()  # You can use Edge, Firefox, etc.
driver.get("https://www.google.com")  # Open Google
driver.maximize_window()  # Maximize the browser window


# 2. Find elements using different locators
print("\nExample 2: Finding Elements")

search_box = driver.find_element(By.NAME, "q")  # Find the search bar
search_box.send_keys("Selenium Python")  # Type text into the search bar
search_box.send_keys(Keys.RETURN)  # Press Enter


# 3. Get Page Title
print("\nExample 3: Getting Page Title")

time.sleep(2)  # Wait for the page to load
print("Page Title:", driver.title)  # Print the title of the page


# 4. Click a link (Example using Google's "Images" link)
print("\nExample 4: Clicking a Link")

images_link = driver.find_element(By.LINK_TEXT, "Images")
images_link.click()
time.sleep(2)


# 5. Get Current URL
print("\nExample 5: Getting Current URL")

print("Current URL:", driver.current_url)


# 6. Navigating Back & Forward
print("\nExample 6: Navigating Back & Forward")

driver.back()  # Go back
time.sleep(2)
driver.forward()  # Go forward
time.sleep(2)


# 7. Handling Alerts (If present)
print("\nExample 7: Handling Alerts (If any)")

try:
    alert = driver.switch_to.alert
    print("Alert Text:", alert.text)
    alert.accept()  # Accept the alert
except:
    print("No alert found.")


# 8. Closing the browser
print("\nExample 8: Closing the Browser")

driver.quit()  # Close all browser windows