import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Chrome browser invoke by driver through manually
service_obj = Service("C:\\Users\\Proshanta\\Desktop\\PythonAutomation\\driver\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.maximize_window()
time.sleep(2)

# Handling auto-suggestive dropdown
driver.find_element(By.ID, 'autosuggest').send_keys('ind')
time.sleep(2)
countryList = driver.find_elements(By.XPATH, "//ul//li[@class='ui-menu-item']/a")
print(len(countryList))
for country in countryList:
    if country.text == "India":
        country.click()
        break

assert driver.find_element(By.ID, 'autosuggest').get_attribute('value') == 'India'
