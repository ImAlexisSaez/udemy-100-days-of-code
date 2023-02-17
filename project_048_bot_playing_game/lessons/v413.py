from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("C:\Program Files\ChromeDriver\chromedriver.exe")

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.amazon.com/Instant-Pot-Pressure-Steamer-Sterilizer/dp/B08PQ2KWHS/")

price = driver.find_element(By.CLASS_NAME, "a-offscreen")
print(price.get_attribute('innerHTML'))
driver.quit()
