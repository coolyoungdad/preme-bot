import time
from config import keys
from selenium import webdriver

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
 

def order (k):  
    #open URL
    driver.get(k["product_url"]) 

    #click buttons 
    driver.find_element_by_xpath('//*[@id="add-remove-buttons"]/input').click() 
    time.sleep(0.5)
    driver.find_element_by_xpath('//*[@id="cart"]/a[2]').click()
    
    #add keys to cart page
    #add shipping+billing  
    driver.find_element_by_xpath('//*[@id="order_billing_name"]').send_keys(k["name"]) 
    driver.find_element_by_xpath('//*[@id="order_email"]').send_keys(k["email"]) 
    driver.find_element_by_xpath('//*[@id="order_tel"]').send_keys(k["tel"])
    driver.find_element_by_xpath('//*[@id="bo"]').send_keys(k["address"]) 
    driver.find_element_by_xpath('//*[@id="oba3"]').send_keys(k["apt"]) 
    driver.find_element_by_xpath('//*[@id="order_billing_zip"]').send_keys(k["zip"]) 
    driver.find_element_by_xpath('//*[@id="order_billing_city"]').send_keys(k["city"])

    #add CC info
    driver.find_element_by_xpath('//*[@id="order_billing_city"]').send_keys(k["cc"]) 


if __name__ == '__main__':
    #launch chrome driver 
    driver = webdriver.Chrome('./chromedriver')
    order(keys)
    