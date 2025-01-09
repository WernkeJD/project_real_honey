from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

class DiscountDetector:
    def __init__(self, driver):
        self.driver = driver

    def Detect(self, url):

        self.driver.get(url)

        tags = ["discount", "coupon", "promo"]

        for tag in tags:
            try:
                input_field = self.driver.find_element(By.XPATH, f"//input[contains(@id, '{tag}') or contains(@name, '{tag}') or contains(@placeholder, '{tag}')]")
                print(f'input field element is: {input_field}')
                return input_field
            except:
                continue
                
        self.driver.quit()

        
# if __name__== "__main__":
#     detector = DiscountDetector()
#     detector.Detect('https://www.bespokepost.com/cart/checkout?step=guest_account')