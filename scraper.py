import requests
from bs4 import BeautifulSoup

url = "https://asaxiy.uz/product?key=konditsioner"

headers = {
    "User-Agent": (
        "Mozilla/5.0 "
        "(Windows NT 10.0; Win64; x64)"
    )
}

r = requests.get(
    url,
    headers=headers,
    timeout=30
)

soup = BeautifulSoup(
    r.text,
    "html.parser"
)

print(
    soup.title.text
)

cards = soup.find_all("div")

print(
    "DIV COUNT:",
    len(cards)
)

for div in cards[:30]:
    print(
        div.get("class")
    )
