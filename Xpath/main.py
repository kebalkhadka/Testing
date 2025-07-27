from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Edge()
driver.get('https://automationexercise.com/')
driver.maximize_window()


#Absolute xpath
# driver.find_element(By.XPATH,'/html/body/section[1]/div/div/div/div/div/div[3]/div[1]/a[1]/button').click()



#Relative Xpath

# driver.find_element(By.XPATH,"//div[@class='header-middle']//div[@class='container']")

driver.find_element(By.XPATH, "//a[text()='Products']").click()


