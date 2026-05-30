import json
import sys

from scraper_asaxiy import scrape_asaxiy
from scraper_texnomart import scrape_texnomart

group_id = int(sys.argv[1])

group_name = sys.argv[2]

search_text = sys.argv[3]

# Guruh + foydalanuvchi matni
query = f"{search_text} {group_name}"

all_products = []

try:

    products = scrape_asaxiy(
        query,
        group_id
    )

    all_products.extend(
        products
    )

except Exception as e:

    print(
        "ASAXIY ERROR:",
        e
    )

try:

    products = scrape_texnomart(
        query,
        group_id
    )

    all_products.extend(
        products
    )

except Exception as e:

    print(
        "TEXNOMART ERROR:",
        e
    )

with open(
    "products.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        all_products,
        f,
        ensure_ascii=False,
        indent=2
    )

print(
    f"Saved {len(all_products)} products"
)
