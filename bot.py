import time
from config import keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0
import threading

#timing of the execution
def timeme(method):
    def wrapper(*args, **kw):
        startTime = int(round(time.time() * 1000))
        result = method(*args, **kw)
        endTime = int(round(time.time() * 1000))
        print((endTime - startTime)/1000, 's')
        return result
    return wrapper
@timeme

def start (k):
    #opens supreme
    driver.implicitly_wait(10) # seconds
    driver.get(k["product_url"]) 
    checkProductPage()

def setInterval(func, time):
    e = threading.Event()
    while not e.wait(time):
            func()

def checkProductPage():
    try:
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "description")))
    finally:
        order(keys)
 

def order (k):  
    #click buttons on item page
    driver.find_element_by_xpath('//*[@id="add-remove-buttons"]/input').click() 
    time.sleep(0.5)
    driver.find_element_by_xpath('//*[@id="cart"]/a[2]').click()
    
    #add keys to cart page
    #add shipping 
    driver.find_element_by_xpath('//*[@id="order_billing_name"]').send_keys(k["name"]) 
    driver.find_element_by_xpath('//*[@id="order_email"]').send_keys(k["email"]) 
    driver.find_element_by_xpath('//*[@id="order_tel"]').send_keys(k["tel"])
    driver.find_element_by_xpath('//*[@id="bo"]').send_keys(k["address"]) 
    driver.find_element_by_xpath('//*[@id="oba3"]').send_keys(k["apt"]) 
    driver.find_element_by_xpath('//*[@id="order_billing_zip"]').send_keys(k["zip"]) 
    driver.find_element_by_xpath('//*[@id="order_billing_city"]').send_keys(k["city"])
    driver.find_element_by_xpath('//*[@id="order_billing_state"]/option[37]').click()

    #add CC info
    driver.find_element_by_id('nnaerb').send_keys(keys['card_number'])
    driver.find_element_by_xpath('//*[@id="orcer"]').send_keys(k["card_cvv"])

    #click agree to terms
    process_payment = driver.find_element_by_xpath('//*[@id="pay"]/input')
    process_payment.click()

if __name__ == '__main__':
    #launch chrome driver 
    driver = webdriver.Chrome('./chromedriver')
    start(keys)