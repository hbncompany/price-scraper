from playwright.sync_api import sync_playwright
from urllib.parse import quote

def scrape_olcha(search_text, group_id):

    results = []
    
    try:
    
        url = (
            f"https://olcha.uz/oz/search"
            f"?q={quote(search_text)}"
        )
    
        with sync_playwright() as p:
    
            browser = p.chromium.launch(
                headless=True
            )
    
            page = browser.new_page()
    
            page.goto(
                url,
                wait_until="networkidle",
                timeout=60000
            )
    
            html = page.content()
    
            print("URL:", url)
            print("HTML LENGTH:", len(html))
            print(html[:1000])
    
            browser.close()
    
        return results
    
    except Exception as e:
    
        print(
            f"PLAYWRIGHT ERROR: {e}"
        )
    
        return []
