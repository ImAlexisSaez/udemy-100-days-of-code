from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("C:\Program Files\ChromeDriver\chromedriver.exe")

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=service, options=options)

driver.get("https://en.wikipedia.org/wiki/Main_Page")

# articles_number = driver.find_element(By.CSS_SELECTOR, "#articlecount a")
# articles_number.click()

wikipedia_link = driver.find_element(By.LINK_TEXT, "Wikipedia")
wikipedia_link.click()

# driver.quit()
