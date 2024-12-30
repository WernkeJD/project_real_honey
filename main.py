from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from scrapers import Discount_scraper
from flask import Flask, jsonify, request

# http://localhost:5000/search_coupons?website=nordvpn

# Start chrome
driver = webdriver.Chrome()

driver.get("https://www.google.com")

app = Flask(__name__)

@app.route('/search_coupons', methods=['GET'])
def search_coupons():
    website = driver.current_url
    print(website)

    if website.startswith("http://") or website.startswith("https://"):
        website = website.split("//")[1].split("/")[0]
    
    if not website:
        return jsonify({"error": "Website is required"}), 400
    
    # Open a new tab
    driver.execute_script("window.open('');")
    # Switch to the new tab
    driver.switch_to.window(driver.window_handles[-1])
    
    driver.get("https://www.google.com")
    time.sleep(3)

    search_query = website + " coupon codes"
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(search_query)
    search_box.send_keys(Keys.RETURN)

    time.sleep(3)

    search_results = driver.find_elements(By.CSS_SELECTOR, "h3")

    allowed_domains = ["couponfollow.com", "retailmenot.com"]

    discount_scraper = Discount_scraper(driver)

    coupons = []

    for result in search_results[:20]:
        link = result.find_element(By.XPATH, "..").get_attribute("href")

        if any(domain in link for domain in allowed_domains):
            coupons.append({
                'title': result.text,
                'link': link
            })

            discount_scraper.scrape(link)

    return jsonify(coupons)

if __name__ == '__main__':
    app.run()
