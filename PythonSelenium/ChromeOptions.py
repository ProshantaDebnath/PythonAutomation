import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
# how to run browser in headless mood
chrome_options.add_argument("headless")

# how to ignore certification errors
chrome_options.add_argument("--ignore-certificate-errors")

# Maximize screen mood
chrome_options.add_argument("--start-maximized")

# Chrome browser invoke by driver through manually
service_obj = Service("C:\\Users\\Proshanta\\Desktop\\PythonAutomation\\driver\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj, options=chrome_options)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
print(driver.title)
time.sleep(5)
