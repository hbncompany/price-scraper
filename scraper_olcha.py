import cloudscraper
import re

from bs4 import BeautifulSoup
from urllib.parse import quote

def scrape_olcha(search_text, group_id):
    results = []
    
    try:
    
        url = (
            f"https://olcha.uz/oz/search"
            f"?q={quote(search_text)}"
        )
    
        headers = {
            "User-Agent": (
                "Mozilla/5.0 "
                "(Windows NT 10.0; Win64; x64) "
                "AppleWebKit/537.36 "
                "(KHTML, like Gecko) "
                "Chrome/124.0.0.0 Safari/537.36"
            ),
            "Accept": (
                "text/html,application/xhtml+xml,"
                "application/xml;q=0.9,image/avif,"
                "image/webp,*/*;q=0.8"
            ),
            "Accept-Language": "en-US,en;q=0.9",
            "Connection": "keep-alive"
        }
    
        scraper = cloudscraper.create_scraper(
            browser={
                "browser": "chrome",
                "platform": "windows",
                "mobile": False
            }
        )
    
        response = scraper.get(
            url,
            headers=headers,
            timeout=30
        )
    
        print("=" * 50)
        print("URL:", url)
        print("STATUS:", response.status_code)
        print("HTML LENGTH:", len(response.text))
        print("FIRST 1000 CHARS:")
        print(response.text[:1000])
        print("=" * 50)
    
        soup = BeautifulSoup(
            response.text,
            "html.parser"
        )
    
        products = soup.select(
            "div.product-card"
        )
    
        print(
            "PRODUCT COUNT:",
            len(products)
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
    
                price_text = re.sub(
                    r"\D",
                    "",
                    price_el.get_text()
                )
    
                if not price_text:
                    continue
    
                price = int(price_text)
    
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
    
            except Exception as e:
    
                print(
                    f"PRODUCT ERROR: {e}"
                )
    
        print(
            f"FOUND PRODUCTS: {len(results)}"
        )
    
        return results
    
    except Exception as e:
    
        print(
            f"OLCHA SCRAPER ERROR: {e}"
        )
    
        return []
