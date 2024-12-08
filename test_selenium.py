from selenium import webdriver
from selenium.webdriver.chrome.service import Service
#from selenium.webdriver.common.keys import keys
import time

# Specify the path to the ChromeDriver executable
service = Service("/usr/local/bin/chromedriver")

# Create a new Chrome WebDriver instance
driver = webdriver.Chrome(service=service)

# Open Gmail login page
driver.get("https://mail.google.com")

# Find the email input field and enter your email
email_field = driver.find_element(By.ID, "identifierId")
email_field.send_keys("zaman.arif@gmail.com")
email_field.send_keys(Keys.RETURN)

# Wait for the next page to load
time.sleep(5)

# Find the password input field and enter your password
password_field = driver.find_element(By.NAME, "password")
password_field.send_keys("your-password")
password_field.send_keys(Keys.RETURN)
print(driver.page_source)

# Wait for the inbox to load
time.sleep(5)

# Close the browser once done
driver.quit()
