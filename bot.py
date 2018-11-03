import time
from config import keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0
from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0


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


#Script starts
#open Google and sign-in
def googleStart (k):
    driver.get(k["google"])
    driver.find_element_by_xpath('//*[@id="identifierId"]').send_keys(k["google_id"])
    driver.find_element_by_xpath('//*[@id="identifierNext"]').click()
    time.sleep(0.5)
    driver.find_element_by_xpath('//*[@id="password"]/div[1]/div/div[1]/input').send_keys(k["google_password"])
    time.sleep(0.5)
    driver.find_element_by_xpath('//*[@id="passwordNext"]/content/span').click()
    time.sleep(1)
    supremeStart(keys)

#opens supreme
def supremeStart (k):
    driver.implicitly_wait(10000) # seconds
    driver.get(k["product_url"]) 
    checkProductPage()

#waits for click on the product you want
def checkProductPage():
    try:
        element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "description")))
    finally:
        order(keys)
 
#starts order
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
    driver.find_element_by_xpath('//*[@id="order_billing_state"]/option[37]').click()

    #add CC info
    driver.find_element_by_id('nnaerb').send_keys(keys['card_number'])
    driver.find_element_by_xpath('//*[@id="orcer"]').send_keys(k["card_cvv"])

    #click agree to terms
    driver.find_element_by_xpath('//*[@id="cart-cc"]/fieldset/p[2]/label/div/ins').click()
    process_payment = driver.find_element_by_xpath('//*[@id="pay"]/input')
    process_payment.click()

if __name__ == '__main__':
    #launch chrome driver 
    driver = webdriver.Chrome('./chromedriver')
    googleStart(keys)