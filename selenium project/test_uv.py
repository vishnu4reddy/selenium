from selenium import webdriver  
import time 
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
print("Starting on the earth")
def test_uv():
    pass
    driver = webdriver.Chrome(executable_path=r'C:\webdriver\chromedriver.exe')  
    driver.maximize_window()  
    driver.get("https://www.google.com/")  
    time.sleep(1)
    driver.find_element(By.NAME,"q").send_keys("usirike vishnu vardhan reddy") 
    time.sleep(1) 
    driver.find_element(By.XPATH,"//div[@class='FPdoLc lJ9FBc']//input[@name='btnK']").send_keys(Keys.ENTER)
    time.sleep(1) 
    driver.find_element(By.XPATH,"//h3[contains(text(),'Vishnu vardhan Reddy - Piduguralla, Andhra Pradesh')]").click()
    time.sleep(1)
    driver.save_screenshot('screenshots1.png')  
    driver.close()  
    print("landed on the moon ")  