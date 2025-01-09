from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

class Discount_scraper:
    def __init__(self, driver):
        self.driver = driver

    def open_site(self, url):
        self.driver.get(url)
        time.sleep(3)

    def __scrape_couponfollow(self, url):
        discounts = []
        i = 0

        while True:
            discount_elements = self.driver.find_elements(By.CSS_SELECTOR, 'a.btn-reveal.offer-cta')
            
            if i >= len(discount_elements):
                break

            discount_elements[i].click()
            print('Coupon revealed')

            # Manage new window/tab
            if len(self.driver.window_handles) > 1:
                self.driver.switch_to.window(self.driver.window_handles[-1])
                print("driver is looking at" , self.driver.title)
                coupon_code_element = self.driver.find_elements(By.XPATH, '//*[@id="code"]')
                
                if coupon_code_element:
                    coupon_code = coupon_code_element[0].get_attribute('value')
                    print(f'Coupon Code: {coupon_code}')
                    discounts.append(coupon_code)
                    close_button = self.driver.find_elements(By.CSS_SELECTOR, 'div.close-icon')
                    clickable_close_button = close_button[0]
                    clickable_close_button.click()
                else:
                    print('No coupon code found')
                    close_button = self.driver.find_elements(By.CSS_SELECTOR, 'div.close-icon')
                    clickable_close_button = close_button[0]
                    clickable_close_button.click()

                self.driver.switch_to.window(self.driver.window_handles[-2])
                self.driver.close()
                self.driver.switch_to.window(self.driver.window_handles[-1])


            i += 1

        return discounts

    def __scrape_retailmenot(self, url):
        discounts = []
        i = 0

        while True:
            discount_elements = self.driver.find_elements(By.XPATH, '//*[contains(@class, "relative") and contains(@class, "mb-2") and contains(@class, "flex") and contains(@class, "h-12")]')

            if i >= len(discount_elements):
                break

            discount_elements[i].click()
            print('Coupon revealed')

            coupon_code_element = self.driver.find_elements(By.CSS_SELECTOR, '.text-xl.font-bold.text-transparent')
            if coupon_code_element:
                coupon_code = coupon_code_element[0].text
                print(f'Coupon Code: {coupon_code}')
                discounts.append(coupon_code)
            else:
                print('No coupon code found')

            i += 1

        return discounts

    def scrape(self, url):
        self.open_site(url)
        self.driver.implicitly_wait(3)

        if 'couponfollow' in url:
            discounts = self.__scrape_couponfollow(url)
        elif 'retailmenot' in url:
            discounts = self.__scrape_retailmenot(url)

        return discounts

# if __name__ == '__main__':
#     driver = webdriver.Chrome()
    
#     discount_scraper = Discount_scraper()

#     # discount_scraper.scrape('https://couponfollow.com/site/nordvpn.com')
#     discount_scraper.scrape('https://www.retailmenot.com/view/nordvpn.com')
    