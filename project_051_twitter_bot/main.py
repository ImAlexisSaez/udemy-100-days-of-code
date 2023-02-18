import os
import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By


option = webdriver.ChromeOptions()
option.add_experimental_option("detach", True)
service = ChromeService("C:\Program Files\ChromeDriver\chromedriver.exe")

TWITTER_EMAIL = os.environ["TWITTER_EMAIL"]
TWITTER_PASSWORD = os.environ["TWITTER_PASSWORD"]
TWITTER_USER = os.environ["TWITTER_USER"]


class InternetSpeedTwitterBot:
    def __init__(self):
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver = webdriver.Chrome(service=service, options=option)
        self.driver.get("https://www.speedtest.net/")
        time.sleep(2)

        # Consent
        self.driver.find_element(By.ID, "onetrust-accept-btn-handler").click()
        time.sleep(2)

        # Test
        self.driver.find_element(By.CLASS_NAME, value="start-text").click()
        time.sleep(50)

        self.down = float(self.driver.find_element(By.CLASS_NAME, value="download-speed").text)
        self.up = float(self.driver.find_element(By.CLASS_NAME, value="upload-speed").text)
        print(self.down, self.up)

        self.driver.quit()

    def tweet_at_provider(self):
        self.driver = webdriver.Chrome(service=service, options=option)
        self.driver.get("https://twitter.com/")
        time.sleep(2)

        # start session
        self.driver.find_element(By.LINK_TEXT, 'Iniciar sesión').click()
        time.sleep(2)

        # mail
        mail_entry = self.driver.find_element(By.NAME, "text")
        mail_entry.send_keys(TWITTER_EMAIL)
        mail_entry.send_keys(Keys.ENTER)
        time.sleep(2)

        # user
        user_entry = self.driver.find_element(By.NAME, "text")
        user_entry.send_keys(TWITTER_USER)
        user_entry.send_keys(Keys.ENTER)
        time.sleep(2)

        # password
        pass_entry = self.driver.find_element(By.NAME, "password")
        pass_entry.send_keys(TWITTER_PASSWORD)
        pass_entry.send_keys(Keys.ENTER)
        time.sleep(2)

        # tweet
        tweet_entry = self.driver.find_element(By.CSS_SELECTOR, 'br[data-text="true"]')
        tweet_entry.send_keys(f"Velocidad de descarga: {self.down} Mbps. Velocidad de subida: {self.up} Mbps.")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//div[@data-testid='tweetButtonInline']").click()
        time.sleep(2)
        print("Tweet Done")


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()
