import json

from scraper_asaxiy import scrape_asaxiy

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

    print("=" * 50)
    print("SEARCH:", keyword)

    try:

        data = scrape_asaxiy(
            keyword,
            group_id
        )

        print(
            f"FOUND: {len(data)}"
        )

        all_products.extend(data)

    except Exception as e:

        print(
            f"ERROR: {e}"
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
