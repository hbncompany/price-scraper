import json
import mysql.connector

from scraper_asaxiy import scrape_asaxiy

db = mysql.connector.connect(
host="hbncompany.mysql.pythonanywhere-services.com",
user="hbncompany",
password="Sersarson7",
database="hbncompany$default"
)

cursor = db.cursor(dictionary=True)

cursor.execute("""
SELECT
id,
subgroup_name,
search_keywords
FROM product_groups
WHERE is_active=1
""")

groups = cursor.fetchall()

all_products = []

for group in groups:

group_id = group["id"]

keywords = [
    x.strip()
    for x in group["search_keywords"].split(",")
    if x.strip()
]

print(
    f"GROUP: {group['subgroup_name']}"
)

for keyword in keywords:

    try:

        print(
            f"SEARCH: {keyword}"
        )

        products = scrape_asaxiy(
            keyword,
            group_id
        )

        all_products.extend(
            products
        )

    except Exception as e:

        print(e)

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
