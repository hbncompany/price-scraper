import json
import sys

from scraper_asaxiy import scrape_asaxiy
from scraper_texnomart import scrape_texnomart

# group_id = int(sys.argv[1])

group_id = '5'

# group_name = sys.argv[2]
group_name = 'Smartfon'

# search_text = sys.argv[3]
search_text = 'Iphone 16'

query = f"{group_name} + {search_text}"

print("QUERY:", query)

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

unique = {}

for p in all_products:

    key = (
        p["store_name"]
        + "|"
        + p["product_name"]
    )

    unique[key] = p

all_products = list(
    unique.values()
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
