from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("C:\Program Files\ChromeDriver\chromedriver.exe")

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=service, options=options)

driver.get("https://web.archive.org/web/20220120120408/https://secure-retreat-92358.herokuapp.com/")

first_name_box = driver.find_element(By.NAME, "fName")
first_name_box.send_keys("Mi nombre")
last_name_box = driver.find_element(By.NAME, "lName")
last_name_box.send_keys("Mi apellido")
mail_box = driver.find_element(By.NAME, "email")
mail_box.send_keys("mi@correo.com")

sign_up_btn = driver.find_element(By.XPATH, "/html/body/form/button")
sign_up_btn.click()






