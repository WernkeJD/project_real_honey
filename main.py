from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

from scrapers import Discount_scraper

search_query = input("Enter your search term: ")

driver = webdriver.Chrome()

driver.get("https://www.google.com")

time.sleep(2)

search_box = driver.find_element(By.NAME, "q")
search_box.send_keys(search_query)
search_box.send_keys(Keys.RETURN)

time.sleep(3)

search_results = driver.find_elements(By.CSS_SELECTOR, "h3")

allowed_domains = ["techradar.com", "couponfollow.com", "retailmenot.com"]

discount_scraper = Discount_scraper()

for result in search_results[:20]:
    link = result.find_element(By. XPATH, "..").get_attribute("href")

    if any(domain in link for domain in allowed_domains):
        print(f'Title: {result.text}')
        print(f'Link: {link}\n')

        discount_scraper.scrape(link)

driver.quit()