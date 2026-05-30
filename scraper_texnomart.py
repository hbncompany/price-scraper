import requests

def scrape_texnomart(
search_text,
group_id
):

results = []

try:

    url = (
        "https://gw.texnomart.uz/"
        "api/common/v1/search/result"
    )

    params = {
        "q": search_text,
        "page": 1,
        "limit": 20
    }

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
        params=params,
        headers=headers,
        timeout=30
    )

    data = response.json()

    if not data.get("success"):
        return []

    products = (
        data["data"]
        .get("products", [])
    )

    print(
        "TEXNOMART PRODUCTS:",
        len(products)
    )

    for p in products:

        try:

            product_url = (
                "https://texnomart.uz/"
                f"product/{p['id']}"
            )

            results.append({

                "group_id":
                group_id,

                "store_name":
                "Texnomart",

                "product_name":
                p.get(
                    "name",
                    ""
                ),

                "image_url":
                p.get(
                    "image",
                    ""
                ),

                "product_url":
                product_url,

                "price":
                int(
                    p.get(
                        "sale_price",
                        0
                    )
                )

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
        "TEXNOMART ERROR:",
        e
    )

    return []
