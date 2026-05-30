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

        print("URL:", response.url)
        print("STATUS:", response.status_code)
        print("SUCCESS:", data["success"])

        print("DATA TYPE:", type(data["data"]))
        
        if isinstance(data["data"], list):
        
            print("ITEMS:", len(data["data"]))
        
            if len(data["data"]) > 0:
        
                print(
                    data["data"][0]
                )

        elif isinstance(data["data"], dict):
        
            print(
                data["data"].keys()
            )
        
        data = response.json()

        print("DATA TYPE:", type(data["data"]))
        
        if isinstance(data["data"], list):
        
            print("ITEMS:", len(data["data"]))
        
            if len(data["data"]) > 0:
        
                print(
                    data["data"][0]
                )

        elif isinstance(data["data"], dict):
        
            print(
                data["data"].keys()
            )
        

        print(data.keys())

        return results

    except Exception as e:

        print(
            "TEXNOMART ERROR:",
            e
        )

        return []
