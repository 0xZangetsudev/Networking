from urllib.request import urlopen
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/Python_(programming_language)"

html_code = urlopen(url).read().decode("utf-8")

soup = BeautifulSoup(html_code, 'lxml')

type_table = soup.find(class_="wikitable")
body = type_table.find("tbody")
rows = body.find_all("tr")[1:]

mutable_types = []
immutable_types = []

for row in rows:
    data = row.find_all("td")
    if data[1].get_text() == "mutable\n":
        mutable_types.append(data[0].get_text())
    else:
        immutable_types.append(data[0].get_text())

print(f"Mutable Types: {mutable_types}")
print(f"immutable_types: {immutable_types}")

