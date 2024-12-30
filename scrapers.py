from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

class Discount_scraper:
    def __init__(self):
        options = Options()
        options.add_argument('--ignore-certificate-errors')
        options.add_argument('--incognito')
        self.driver = webdriver.Chrome()

    def open_site(self, url):
        self.driver.get(url)
        time.sleep(3)
    
    #works
    def __scrape_couponfollow(self, url):
        discounts = []

        i = 0

        while True:
            discount_elements = self.driver.find_elements(By.CSS_SELECTOR, 'a.btn-reveal.offer-cta')

            if i == len(discount_elements):
                break

            discount_elements[i].click()

            print('Coupon revealed')

            self.driver.close()
            self.driver.switch_to.window(self.driver.window_handles[0])

            coupon_code_element = self.driver.find_elements(By.XPATH, '//*[@id="code"]')
            if coupon_code_element:
                coupon_code = coupon_code_element[0].get_attribute('value')
                print(f'Coupon Code: {coupon_code}')
                discounts.append(coupon_code)
            else:
                print('No coupon code found')

            self.driver.get(url)

            i += 1
           
        self.driver.quit()

        return discounts
    
    #in progress
    def __scrape_retailmenot(self, url):
        discounts = []

        i = 0

        while True:
            discount_elements = self.driver.find_elements(By.XPATH, '//*[contains(@class, "relative") and contains(@class, "mb-2") and contains(@class, "flex") and contains(@class, "h-12")]')

            print(len(discount_elements))

            if i == len(discount_elements):
                break

            print('Coupon revealed')

            # self.driver.close()
            # self.driver.switch_to.window(self.driver.window_handles[0])

            coupon_code_element = self.driver.find_elements(By.CSS_SELECTOR, '.relative mx-auto mb-1 min-w-72 max-w-full rounded-full border border-black bg-gradient-to-r from-black bg-clip-text px-6 py-4 text-xl font-bold text-transparent')
            if coupon_code_element:
                coupon_code = coupon_code_element[0].text
                print(f'Coupon Code: {coupon_code}')
                discounts.append(coupon_code)
            else:
                print('No coupon code found')

            self.driver.get(url)

            i += 1

            self.driver.quit()

        return discounts
    
    def scrape(self, url):
        self.open_site(url)

        self.driver.implicitly_wait(3)

        if 'couponfollow' in url:
            return self.__scrape_couponfollow(url)
        elif 'retailmenot' in url:
            return self.__scrape_retailmenot(url)
                

if __name__ == '__main__':
    discount_scraper = Discount_scraper()

    # discount_scraper.scrape('https://couponfollow.com/site/nordvpn.com')
    discount_scraper.scrape('https://www.retailmenot.com/view/nordvpn.com')
    