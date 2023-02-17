from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

service = Service("C:\Program Files\ChromeDriver\chromedriver.exe")

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=service, options=options)

driver.get("https://web.archive.org/web/20200201000018/https://en.wikipedia.org/wiki/Main_Page")

search_box = driver.find_element(By.NAME, "search")
search_box.send_keys("Python")
search_box.send_keys(Keys.ENTER)

# driver.quit()
