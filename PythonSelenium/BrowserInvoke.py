import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Chrome browser invoke by driver through manually
service_obj = Service("C:\\Users\\Proshanta\\Desktop\\PythonAutomation\\driver\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

# Chrome browser invoke by driver through automatic
driver = webdriver.Chrome()


driver.get("https:www.google.com")
driver.maximize_window()
time.sleep(2)
print(driver.title)
print(driver.current_url)

