import requests

url = "https://texnomart.uz/search?query=konditsioner"

headers = {
    "User-Agent": (
        "Mozilla/5.0 "
        "(Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 "
        "(KHTML, like Gecko) "
        "Chrome/136.0.0.0 Safari/537.36"
    )
}

r = requests.get(
    url,
    headers=headers,
    timeout=30
)

print("STATUS:", r.status_code)
print("SERVER:", r.headers.get("server"))
print("HTML LENGTH:", len(r.text))
print(r.text[:2000])
