# Using Exceptional handling to write Python Selenium codes

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

# Create a new instance of the Firefox driver
driver = webdriver.Firefox()

# Navigate to the Labour website
driver.get("https://labour.gov.in/")

# Create an instance of ActionChains
actions = ActionChains(driver)

# Locate the "Documents" menu
documents_menu = driver.find_element(By.XPATH, value="//a[text()='Documents']")
# Assuming the link to the Monthly Progress Report is available under the "Documents" section
monthly = driver.find_element(By.XPATH, value='//a[@href="https://labour.gov.in/monthly-progress-report"]')

# Hover over the "Documents" menu to reveal its sub-menu
actions.move_to_element(documents_menu).move_to_element(monthly).click().perform()

# Get the download link
download_link = driver.find_element(By.XPATH,value="https://labour.gov.in/sites/default/files/mpr_october_2023.pdf")
actions.click(download_link).perform()
# Wait for some time to allow the download to start
sleep(2)

# Close the browser
driver.quit()
