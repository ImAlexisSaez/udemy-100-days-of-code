from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("C:\Program Files\ChromeDriver\chromedriver.exe")

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.python.org/")

events_times = driver.find_elements(By.CSS_SELECTOR, ".event-widget .shrubbery .menu li time")
events_names = driver.find_elements(By.CSS_SELECTOR, ".event-widget .shrubbery .menu li a")

events_dict = {}
for idx, event in enumerate(events_times):
    event_html = event.get_attribute("innerHTML")
    event_year = event_html.split(">")[1].split("<")[0]
    event_day = event_html.split("</span>")[1]
    events_dict[idx] = {
        "time": f"{event_year}{event_day}",
    }

for idx, event in enumerate(events_names):
    events_dict[idx]["name"] = event.get_attribute("innerHTML")

print(events_dict)

driver.quit()
