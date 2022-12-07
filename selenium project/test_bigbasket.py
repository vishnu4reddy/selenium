from selenium import webdriver  
import time 
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
number = "9490058514"
print("Starting on the earth")
def test_bigbasket():
    driver = webdriver.Chrome()  
    driver.maximize_window()
    driver.get("https://www.google.com/")  
    time.sleep(1)
    driver.find_element(By.NAME,"q").send_keys("bigbasket") 
    time.sleep(1) 
    driver.find_element(By.XPATH,"//div[@class='FPdoLc lJ9FBc']//input[@name='btnK']").send_keys(Keys.ENTER)
    time.sleep(1)
    driver.find_element(By.XPATH,"//h3[normalize-space()='BigBasket']").click()
    time.sleep(1) 
    driver.find_element(By.XPATH,"//a[@ng-show='vm.newLoginFlow']").click()
    time.sleep(1) 
    driver.find_element(By.XPATH,"//input[@id='otpEmail']").send_keys(number)
    time.sleep(1) 
    driver.find_element(By.XPATH,"//button[@type='submit'][normalize-space()='Continue']").click()
    time.sleep(20)
    driver.find_element(By.XPATH,"//button[normalize-space()='Verify & Continue']").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"//a[@class='btn hvr-fade']//span[@class='new-caret']").click()
    time.sleep(1)
    driver.find_element(By.XPATH,"//a[@ng-click='vm.logout()']").click()
    time.sleep(1)
    driver.close()  
    print("landed on the moon ")
