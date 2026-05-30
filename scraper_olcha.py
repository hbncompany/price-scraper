import requests
import re

from bs4 import BeautifulSoup

from urllib.parse import quote

def scrape_olcha(
search_text,
group_id
):

results = []

url = (
    f"https://olcha.uz/oz/search"
    f"?q={quote(search_text)}"
)

headers = {

    "User-Agent":
    "Mozilla/5.0"

}

response = requests.get(
    url,
    headers=headers,
    timeout=30
)

soup = BeautifulSoup(
    response.text,
    "html.parser"
)

products = soup.select(
    "div.product-card"
)

for product in products:

    try:

        name_el = product.select_one(
            ".product-card__brand-name"
        )

        price_el = product.select_one(
            ".price__main"
        )

        link_el = product.select_one(
            "a.product-card__link"
        )

        img_el = product.select_one(
            ".product-card__image img[src]"
        )

        if not (
            name_el and
            price_el and
            link_el
        ):
            continue

        name = name_el.get_text(
            strip=True
        )

        price = int(

            re.sub(
                r"\D",
                "",
                price_el.text
            )

        )

        image_url = ""

        if img_el:

            image_url = img_el.get(
                "src",
                ""
            )

        results.append({

            "group_id": group_id,

            "store_name": "Olcha",

            "product_name": name,

            "image_url": image_url,

            "product_url":
            "https://olcha.uz"
            + link_el["href"],

            "price": price

        })

    except:

        pass

return results
