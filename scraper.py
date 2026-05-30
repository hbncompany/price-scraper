import json

from scraper_olcha import scrape_olcha

# Hozircha faqat Olcha ishlatsin
# from scraper_asaxiy import scrape_asaxiy
# from scraper_texnomart import scrape_texnomart

all_products = []

SEARCHES = [
    {
        "group_id": 1,
        "keyword": "konditsioner"
    },
    {
        "group_id": 2,
        "keyword": "artel"
    },
    {
        "group_id": 3,
        "keyword": "muzlatgich"
    },
    {
        "group_id": 4,
        "keyword": "smartfon"
    }
]

for item in SEARCHES:

    keyword = item["keyword"]
    group_id = item["group_id"]

    try:

        data = scrape_olcha(
            keyword,
            group_id
        )

        all_products.extend(data)

    except Exception as e:

        print(
            f"Error for {keyword}: {e}"
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
