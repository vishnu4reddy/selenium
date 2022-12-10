from selenium import webdriver  
import time 
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
print("Starting on the earth")
# class TestLinkedin:  
def test_linkedin():
    pass
    user_name = "8247548679"
    password = "vishnu161999"
    driver = webdriver.Chrome()  
    driver.maximize_window()  
    driver.get("https://www.google.com/")  
    time.sleep(1)
    driver.find_element(By.NAME,"q").send_keys("linkedin login") 
    time.sleep(1) 
    driver.find_element(By.XPATH,"//div[@class='FPdoLc lJ9FBc']//input[@name='btnK']").send_keys(Keys.ENTER)
    print(driver.find_element(By.XPATH,"//h3[normalize-space()='LinkedIn Login, Sign in']").is_enabled())
    driver.find_element(By.XPATH,"//h3[normalize-space()='LinkedIn Login, Sign in']").click() 
    driver.find_element(By.NAME,"session_key").send_keys(user_name)  
    print(driver.current_url)
    driver.find_element(By.NAME,"session_password").send_keys(password)  
    print(driver.current_url) 
    driver.find_element(By.XPATH,"//button[@aria-label='Sign in']").click()
    print(driver.current_url)
    driver.find_element(By.XPATH,"//img[@id='ember17']").click()
    driver.find_element(By.XPATH,"//a[@class='global-nav__secondary-link mv1']").click()
    driver.save_screenshot('screenshots.png')
    driver.close()  
    print("landed on the moon ") 
    # driver.find_element(By.XPATH,"//h3[normalize-space()='LinkedIn Login, Sign in']").is_enabled()
    # driver.save_screenshot('screenshots.png')
    # print(driver.get_screenshot_as_file("linkedin_case.png"))
    # time.sleep(2)
    # print(driver.get_screenshot_as_png())
    # time.sleep(2)
    # driver.find_element(By.XPATH,"//span[normalize-space()='Next']").click()
    # time.sleep(3)