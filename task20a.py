# Using Exceptional handling to write Python Selenium codes

from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.common.by import By
from time import sleep
from selenium.common.exceptions import NoSuchElementException

class TestCase1:
  
   #constructor
   def __init__(self, web_url):
       self.url = web_url
       self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))

   def login(self):
       try:
           # Click and open the FAQ page
           self.driver.maximize_window()
           self.driver.get(self.url)
           sleep(2)
           self.driver.find_element(by=By.LINK_TEXT, value="FAQ").click()
          
           #Click and open the Partners page
        #    self.driver.get(self.url)
           sleep(2)
           self.driver.find_element(by=By.LINK_TEXT, value="PARTNERS").click()
           sleep(2)

           # Get the handles of the opened windows and close the new windows
           window_handles = self.driver.window_handles
           self.driver.switch_to.window(window_handles[1])
           self.driver.close()
           self.driver.switch_to.window(window_handles[2])
           self.driver.close()
           self.driver.switch_to.window(window_handles[0])
           sleep(4)
                 
       except NoSuchElementException as selenium_error:
           print("Element not found", selenium_error)
       finally:
           # Close the original window
           self.driver.quit()

url_cowin="https://www.cowin.gov.in/"
TC = TestCase1(url_cowin)
TC.login()
