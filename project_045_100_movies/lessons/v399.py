from bs4 import BeautifulSoup

with open("website.html", "r", encoding="utf-8") as web_file:
    contents = web_file.read()

soup = BeautifulSoup(contents, "html.parser")

print(soup.title)
print(soup.title.name)  # name of the tag
print(soup.title.string)  # str inside the tag

# print(soup.prettify())  # all the contents "pretty"

print(soup.a)  # first anchor tag
print(soup.li)  # first li tag
print(soup.p)  # first p tag
