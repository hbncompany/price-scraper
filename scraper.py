import json
import sys

from scraper_asaxiy import scrape_asaxiy

group_id = int(sys.argv[1])

search_text = sys.argv[2]

products = scrape_asaxiy(
    search_text,
    group_id
)

with open(
    "products.json",
    "w",
    encoding="utf-8"
) as f:

    json.dump(
        products,
        f,
        ensure_ascii=False,
        indent=2
    )
