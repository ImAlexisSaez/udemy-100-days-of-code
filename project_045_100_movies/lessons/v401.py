from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

all_titles = soup.find_all(name="span", class_="titleline")
all_titles_text = [title.find(name="a").getText() for title in all_titles]
all_titles_link = [title.find(name="a").get("href") for title in all_titles]

all_upvotes = soup.find_all(class_="score")
all_upvotes_number = [int(upvote.getText().split()[0]) for upvote in all_upvotes]

max_index = all_upvotes_number.index(max(all_upvotes_number))
print(f"The article most upvoted is:\n",
      f"\t {all_titles_text[max_index]}\n",
      f"\t {all_titles_link[max_index]}\n",
      f"with {all_upvotes_number[max_index]} upvotes.")
