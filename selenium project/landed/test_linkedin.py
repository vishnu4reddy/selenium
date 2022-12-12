from selenium import webdriver  
import time 
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
print("Starting on the earth") 
def test_linkedin():
    user_name = "8247548679"
    password = "vishnu161999"
    assert password == "vishnu161999"
    driver = webdriver.Chrome()  
    driver.maximize_window()  
    driver.get("https://www.google.com/")  
    driver.find_element(By.NAME,"q").send_keys("linkedin login") 
    driver.find_element(By.XPATH,"//div[@class='FPdoLc lJ9FBc']//input[@name='btnK']").send_keys(Keys.ENTER)
    driver.find_element(By.XPATH,"//h3[normalize-space()='LinkedIn Login, Sign in']").click() 
    driver.find_element(By.NAME,"session_key").send_keys(user_name)  
    driver.find_element(By.NAME,"session_password").send_keys(password)
    assert password == "vishnu161999"  
    driver.find_element(By.XPATH,"//button[@aria-label='Sign in']").click()
    driver.find_element(By.XPATH,"//img[@id='ember17']").click()
    driver.find_element(By.XPATH,"//a[@class='global-nav__secondary-link mv1']").click()
    driver.save_screenshot('screenshots.png')
    driver.close()  
    print("landed on the moon ") 