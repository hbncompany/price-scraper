import requests
import re

from bs4 import BeautifulSoup
from urllib.parse import quote


def scrape_asaxiy(
    search_text,
    group_id
):

    results = []

    try:

        url = (
            f"https://asaxiy.uz/ru/product"
            f"?key={quote(search_text)}"
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
        print('RESP:::::::')
        print(response.url)

        print(
            "STATUS:",
            response.status_code
        )

        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )

        products = soup.select(
            "div.product__item"
        )

        print(
            "PRODUCT BLOCKS:",
            len(products)
        )

        for product in products:

            try:

                name_el = product.select_one(
                    ".product__item__info-title"
                )

                price_el = product.select_one(
                    ".product__item-price"
                )

                link_el = product.select_one(
                    "a[href*='/product/']"
                )

                img_el = product.select_one(
                    "img[itemprop='image']"
                )

                if not (
                    name_el and
                    price_el and
                    link_el
                ):
                    continue

                name = (
                    name_el
                    .get_text(strip=True)
                )

                price_text = re.sub(
                    r"\D",
                    "",
                    price_el.get_text()
                )

                if not price_text:
                    continue

                price = int(
                    price_text
                )

                image_url = ""

                if img_el:

                    image_url = (
                        img_el.get("src")
                        or
                        img_el.get("data-src")
                        or
                        ""
                    )

                product_url = (
                    "https://asaxiy.uz"
                    + link_el["href"]
                )

                results.append({

                    "group_id": group_id,

                    "store_name": "Asaxiy",

                    "product_name": name,

                    "image_url": image_url,

                    "product_url": product_url,

                    "price": price

                })

            except Exception as e:

                print(
                    "PRODUCT ERROR:",
                    e
                )

        print(
            "FOUND PRODUCTS:",
            len(results)
        )

        return results

    except Exception as e:

        print(
            "ASAXIY ERROR:",
            e
        )

        return []
