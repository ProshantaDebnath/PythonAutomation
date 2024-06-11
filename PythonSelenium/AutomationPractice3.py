import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

# Chrome browser invoke by driver through manually
service_obj = Service("C:\\Users\\Proshanta\\Desktop\\PythonAutomation\\driver\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.maximize_window()
time.sleep(2)

# When we don't know the position of the element
optionsList = driver.find_elements(By.XPATH, "//div[@id='checkbox-example']//label//input")
for option in optionsList:
    if option.get_attribute("value") == "option3":
        option.click()
        assert option.is_selected()
        break

# When we know the exact position of the element
radiobuttonList = driver.find_elements(By.NAME, 'radioButton')
radiobuttonList[2].click()
assert radiobuttonList[2].is_selected()

# is_Displayed Method
assert driver.find_element(By.ID, 'displayed-text').is_displayed()
driver.find_element(By.ID, 'hide-textbox').click()
assert not driver.find_element(By.ID, 'displayed-text').is_displayed()

# Handling pop-up
name = "Proshanta"
driver.find_element(By.ID, 'name').send_keys("Proshanta")
driver.find_element(By.ID, 'alertbtn').click()
alert = driver.switch_to.alert
alertText = alert.text
print(alertText)
assert name in alertText
alert.accept()
