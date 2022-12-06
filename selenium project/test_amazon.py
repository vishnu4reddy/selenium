from selenium import webdriver  
import time 
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
print("Starting on the earth")  
# user_name = "vreddy@msystechnologies.com"
# password = "vishnu16REDDY@"
to = "vishnureddy12.in@gmail.com"
subject = "enjoy"
text = "complete the given work"
number = "9490058514"
password = "9490058514"
def test_amazon():
    pass
    driver = webdriver.Chrome()  
    driver.maximize_window()  
    driver.get("https://www.google.com/")  
    time.sleep(1)
    driver.find_element(By.NAME,"q").send_keys("amazon") 
    time.sleep(1) 
    driver.find_element(By.NAME,"btnK").send_keys(Keys.ENTER)
    time.sleep(1) 
    driver.find_element(By.XPATH,"//h3[normalize-space()='Amazon.in']").click()
    time.sleep(1) 
    driver.find_element(By.XPATH,"//span[@class='nav-line-2 ']").click()
    time.sleep(1) 
    driver.find_element(By.XPATH,"//input[@id='ap_email']").send_keys(number)
    time.sleep(1) 
    driver.find_element(By.XPATH,"//input[@id='continue']").click()
    time.sleep(1) 
    driver.find_element(By.XPATH,"//input[@id='ap_password']").send_keys(password)
    time.sleep(1) 
    driver.find_element(By.XPATH,"//input[@id='signInSubmit']").click()
    time.sleep(3) 
    driver.save_screenshot('screenshots.png') 
    driver.find_element(By.XPATH,"//input[@id='auth-signin-button']").click()
    time.sleep(1) 
    driver.find_element(By.XPATH,"//span[@class='hm-icon-label']").click()
    time.sleep(1) 
    driver.find_element(By.XPATH,"//a[@class='hmenu-item'][normalize-space()='Sign Out']").click()
    time.sleep(1)
    driver.save_screenshot('screenshots1.png') 
    driver.close()  
    print("landed on the moon ")  