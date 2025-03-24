import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
# driver.get('https://demo.nopcommerce.com/')

driver.get('https://www.facebook.com/')
driver.maximize_window()
time.sleep(3)

driver.find_element(By.CSS_SELECTOR,"input#email").send_keys('Kebal')

# driver.find_element(By.ID,"small-searchterms").send_keys("Iphone 16")
# driver.find_element(By.CLASS_NAME,"search-box-button").click()


# for acessing links
# driver.find_element(By.LINK_TEXT,"Register").click()
#
# input("Press Enter to close the browser...")  # Keeps browser open until you manually close it
#
# links=driver.find_elements(By.TAG_NAME,'a')
# print(len(links))