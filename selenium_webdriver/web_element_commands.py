# web_element_commands.py

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set up the WebDriver
driver = webdriver.Chrome()
driver.get("https://www.example.com")
driver.maximize_window()

# Example: Use a test form page instead (replace URL below with a real one if needed)
# driver.get("https://www.w3schools.com/html/html_forms.asp")

# 1. Locate an element
print("Example 1: Locating an element")
element = driver.find_element(By.TAG_NAME, "h1")  # Find the <h1> element
print("Text of h1:", element.text)

# 2. Get tag name
print("\nExample 2: Getting the tag name")
print("Tag name:", element.tag_name)

# 3. Get attribute value
print("\nExample 3: Getting attribute value")
link = driver.find_element(By.TAG_NAME, "a")  # Find the first <a> link
href = link.get_attribute("href")
print("Link href:", href)

# 4. Check if element is displayed
print("\nExample 4: Checking visibility")
print("Is displayed:", element.is_displayed())

# 5. Check if element is enabled
print("\nExample 5: Checking if enabled")
print("Is enabled:", element.is_enabled())

# 6. Check if element is selected (use with checkboxes/radio buttons)
print("\nExample 6: Checking if selected (simulated)")
# You would typically do:
# checkbox = driver.find_element(By.ID, "myCheckBox")
# print("Is selected:", checkbox.is_selected())

# 7. Get CSS property
print("\nExample 7: Getting CSS property")
color = element.value_of_css_property("color")
print("Text color:", color)

# 8. Get size and location
print("\nExample 8: Getting element size and location")
print("Size:", element.size)
print("Location:", element.location)

# Wait before closing
time.sleep(2)
driver.quit()