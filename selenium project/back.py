from selenium import webdriver 
import time 
print("Starting on the earth")  
driver = webdriver.Chrome()  
driver.maximize_window()  
driver.get("https://www.google.com/")
time.sleep(2) 
driver.get("https://www.apple.com/in/?cid-oas-in-domains-apple.in/")
time.sleep(2) 
driver.back()
time.sleep(2) 
driver.close()  
print("landed on the moon ")  
