import time

from selenium import  webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Edge()
driver.get('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')
time.sleep(3)

driver.find_element(By.NAME, "username").send_keys("Admin")


driver.find_element(By.NAME,"password").send_keys("admin123")

driver.find_element(By.CLASS_NAME,"orangehrm-login-button").click()

act_title=driver.title
exp_title = "OrangeHRM"

if act_title == exp_title:
     print("Login passed")
else:
    print("Login failed")

driver.close()
