
from selenium import webdriver  
import time 
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
print("Starting on the earth")
user_name = "vishnureddy12.in@gmail.com"
password = "vishnu16REDDY@"
def sample():
    driver = webdriver.Chrome() 
    driver.maximize_window()  
    driver.get("https://www.google.com/")  
    time.sleep(1)
    # driver.get_log("https://www.google.com/")
    driver.find_element(By.NAME,"q").send_keys("gmail login") 
    time.sleep(1) 
    driver.find_element(By.XPATH,"//div[@class='FPdoLc lJ9FBc']//input[@name='btnK']").send_keys(Keys.ENTER)
    time.sleep(1) 
    driver.find_element(By.XPATH,"//h3[normalize-space()='Gmail - Google']").click()
    driver.find_elements(By.XPATH,"//h3[normalize-space()='Gmail - Google']").is_enabled()
    time.sleep(1) 
    driver.find_element(By.XPATH,"//a[normalize-space()='Sign in']").click()
    driver.find_element(By.NAME,"identifier").send_keys(user_name)  
    time.sleep(3)
    driver.find_element(By.XPATH,"//span[normalize-space()='Next']").click()
    time.sleep(3)
    driver.close()  
    print("landed on the moon ")