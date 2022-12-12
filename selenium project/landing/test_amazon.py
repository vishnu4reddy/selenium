from selenium import webdriver  
import time 
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
print("Starting on the earth")  
number = "9490058514"
password = "9490058514"
# def test_amazon():
# pass
driver = webdriver.Chrome()  
driver.maximize_window()  
driver.get("https://www.google.com/")  
driver.find_element(By.NAME,"q").send_keys("amazon") 
driver.find_element(By.NAME,"btnK").send_keys(Keys.ENTER)
driver.find_element(By.XPATH,"//h3[normalize-space()='Amazon.in']").click()
driver.find_element(By.XPATH,"//span[@class='nav-line-2 ']").click()
driver.find_element(By.XPATH,"//input[@id='ap_email']").send_keys(number)
driver.find_element(By.XPATH,"//input[@id='continue']").click()
driver.find_element(By.XPATH,"//input[@id='ap_password']").send_keys(password)
driver.find_element(By.XPATH,"//input[@id='signInSubmit']").click()
driver.find_element(By.XPATH,"//input[@id='auth-signin-button']").click()
driver.find_element(By.XPATH,"//span[@class='hm-icon-label']").click()
driver.find_element(By.XPATH,"//a[@class='hmenu-item'][normalize-space()='Sign Out']").click()
driver.save_screenshot('screenshots1.png')   
print("landed on the moon ")  