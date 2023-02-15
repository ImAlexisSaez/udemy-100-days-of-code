from bs4 import BeautifulSoup

with open("website.html", "r", encoding="utf-8") as web_file:
    contents = web_file.read()

soup = BeautifulSoup(contents, "html.parser")

all_anchor_tags = soup.find_all(name="a")

all_anchor_text = [tag.getText() for tag in all_anchor_tags]
all_anchor_href = [tag.get("href") for tag in all_anchor_tags]
# print(all_anchor_href)

heading_id = soup.find(name="h1", id="name")
# print(heading_id)

section_class = soup.find(name="h3", class_="heading")
# print(section_class)

# Using css selectors
company_url = soup.select_one(selector="p a")
print(company_url)

headings = soup.select(".heading")
print(headings)