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
                wait_until="domcontentloaded",
                timeout=120000
            )
            
            page.wait_for_timeout(10000)
            
            html = page.content()
            
            print("HTML LENGTH:", len(html))
            print(html[:2000])
    
            browser.close()
    
        return results
    
    except Exception as e:
    
        print(
            f"PLAYWRIGHT ERROR: {e}"
        )
    
        return []
