import requests
from bs4 import BeautifulSoup

my_headers = {
    "User-Agent": "Defined",
    "Accept-Language": "en-US,en;q=0.5",
}

amazon_url = "https://www.amazon.com/dp/B09TYVYRD9/ref=sbl_dpx_kitchen-electric-cookware_B08GC6PL3D_0"

response = requests.get(url=amazon_url, headers=my_headers)
pot_page = response.text

soup = BeautifulSoup(pot_page, "html.parser")
price = float(soup.find(name="span", class_="a-offscreen").getText()[1:])

if price < 80:
    print("Buy it!")
else:
    print("You'll have to wait...")
