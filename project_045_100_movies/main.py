import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
response.encoding = "utf-8"
empire_web = response.text

soup = BeautifulSoup(empire_web, "html.parser")
all_titles = soup.find_all(name="h3", class_="title")
all_titles_text = [title.getText() for title in all_titles]

all_titles_ordered = all_titles_text[::-1]

with open("movies.txt", "w", encoding="utf-8") as movies_file:
    for title in all_titles_ordered:
        movies_file.write(f"{title}\n")






