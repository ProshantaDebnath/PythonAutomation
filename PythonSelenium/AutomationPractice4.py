import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

# Chrome browser invoke by driver through manually
service_obj = Service("C:\\Users\\Proshanta\\Desktop\\PythonAutomation\\driver\\chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.maximize_window()
# Implicitly wait
driver.implicitly_wait(5)
driver.find_element(By.XPATH, "//form//a//following-sibling::input").send_keys("ber")
time.sleep(2)
results = driver.find_elements(By.XPATH, "//div[@class='products']/div")
assert len(results) > 0

# Channing of WebElement Process
for result in results:
    result.find_element(By.XPATH, "div/button").click()

driver.find_element(By.XPATH, "//div[@class='cart']//a[@class='cart-icon']/img").click()
driver.find_element(By.XPATH, "//*[text()='PROCEED TO CHECKOUT']").click()
driver.find_element(By.CLASS_NAME, 'promoCode').send_keys("rahulshettyacademy")
driver.find_element(By.CSS_SELECTOR, '.promoBtn').click()

# Explicitly wait
wait = WebDriverWait(driver, 10)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME, "promoInfo")))
assert driver.find_element(By.CLASS_NAME, 'promoInfo').text == "Code applied ..!"

