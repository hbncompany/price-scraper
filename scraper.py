import json
import sys

from scraper_asaxiy import scrape_asaxiy
from scraper_texnomart import scrape_texnomart

if len(sys.argv) < 4:

    group_id = 2
    group_name = "konditsioner"
    search_text = "artel 12"

else:

    group_id = int(sys.argv[1])
    group_name = sys.argv[2]
    search_text = sys.argv[3]

query = f"{search_text} {group_name}"

print("QUERY:", query)

all_products = []

all_products.extend(
    scrape_asaxiy(
        query,
        group_id
    )
)

all_products.extend(
    scrape_texnomart(
        query,
        group_id
    )
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
