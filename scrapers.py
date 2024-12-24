from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class Discount_scraper:
    def __init__(self):
        self.driver = webdriver.Chrome()

    def open_site(self, url):
        self.driver.get(url)
        time.sleep(3)

    def scrape_techradar(self):
        discounts = []

        return discounts
    
    def scrape_couponfollow(self):
        discounts = []
        discount_elements = self.driver.find_elements(By.CSS_SELECTOR, 'a.btn-reveal.offer-cta')
        discount_elements.click()

        time.sleep(2)

        coupon_code = driver.find_element(By.CSS_SELECTOR, 'span.code').text
        print(f'Coupon Code: {coupon_code}')

        self.scrape_techradardriver.quit()

        return discounts
    
    def scrape_retailmenot(self):
        discounts = []

        return discounts
    
    def scrape(self, url):
        self.open_site(url)

        if 'techradar' in url:
            return self.scrape_techradar()
        elif 'couponfollow' in url:
            return self.scrape_couponfollow()
        elif 'retailmenot' in url:
            return self.scrape_retailmenot()