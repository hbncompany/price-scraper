import requests
import re

from bs4 import BeautifulSoup
from urllib.parse import quote


def scrape_texnomart(
    search_text,
    group_id
):

    results = []

    try:

        url = (
            f"https://texnomart.uz/search"
            f"?q={quote(search_text)}"
        )

        headers = {

            "User-Agent": (
                "Mozilla/5.0 "
                "(Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 "
                "(KHTML, like Gecko) "
                "Chrome/136.0.0.0 Safari/537.36"
            )

        }

        response = requests.get(
            url,
            headers=headers,
            timeout=30
        )

        print("=" * 50)
        print("SEARCH:", search_text)
        print("STATUS:", response.status_code)
        print(
            "SERVER:",
            response.headers.get("server")
        )
        print(
            "HTML LENGTH:",
            len(response.text)
        )

        print(
            response.text[:1000]
        )

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        products = soup.select(
            ".product-card"
        )

        print(
            "PRODUCT BLOCKS:",
            len(products)
        )

        for product in products:

            try:

                name_el = product.select_one(
                    ".product-card__title"
                )

                price_el = product.select_one(
                    ".product-card__price"
                )

                link_el = product.select_one(
                    "a"
                )

                img_el = product.select_one(
                    "img"
                )

                if not (
                    name_el and
                    price_el and
                    link_el
                ):
                    continue

                name = (
                    name_el
                    .get_text(
                        strip=True
                    )
                )

                price = re.sub(
                    r"\D",
                    "",
                    price_el.get_text()
                )

                if not price:
                    continue

                results.append({

                    "group_id":
                    group_id,

                    "store_name":
                    "Texnomart",

                    "product_name":
                    name,

                    "image_url":
                    img_el.get(
                        "src",
                        ""
                    )
                    if img_el
                    else "",

                    "product_url":
                    link_el.get(
                        "href",
                        ""
                    ),

                    "price":
                    int(price)

                })

            except Exception as e:

                print(
                    "PARSE ERROR:",
                    e
                )

        print(
            "FOUND PRODUCTS:",
            len(results)
        )

        return results

    except Exception as e:

        print(
            "TEXNOMART ERROR:",
            e
        )

        return []
