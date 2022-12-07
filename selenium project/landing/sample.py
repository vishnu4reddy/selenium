from selenium import webdriver  
import time 
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
print("Starting on the earth")  
driver = webdriver.Chrome()  
driver.maximize_window()  
driver.get("https://www.google.com/")  
driver.find_element(By.NAME,"q").send_keys("jagan maohan reddy")  
time.sleep(3)  
driver.find_element(By.NAME,"btnK").send_keys(Keys.ENTER)  
time.sleep(3)
driver.find_element(By.CLASS_NAME,"").send_keys(Keys.ENTER)
# driver.get_log("https://www.google.com/")
driver.close()  
print("landed on the moon ")  