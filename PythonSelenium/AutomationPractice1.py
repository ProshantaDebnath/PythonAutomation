import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

# Chrome browser invoke by driver through manually
service_obj = Service("C:\\Users\\Proshanta\\Desktop\\PythonAutomation\\driver\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.maximize_window()
time.sleep(3)

driver.find_element(By.XPATH, "//*[@name='name']").send_keys("Automation")
driver.find_element(By.XPATH, "//*[@name='email']").send_keys("Automation@gmail.com")
driver.find_element(By.XPATH, "//*[@id='exampleInputPassword1']").send_keys("tEst@1230+")
driver.find_element(By.ID, 'exampleCheck1').click()
# Static dropdown
dropdown = Select(driver.find_element(By.ID, 'exampleFormControlSelect1'))
dropdown.select_by_visible_text('Male')
driver.find_element(By.XPATH, "//*[@type='submit']").click()
message = driver.find_element(By.CLASS_NAME, 'alert-success').text
print(message)
assert "Success" in message
