from selenium import webdriver  
import time 
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys
print("Starting on the earth")  
user_name = "8247548679"
password = "vishnu161999"
def test_linkedin():
    pass
    driver = webdriver.Chrome(executable_path=r'C:\webdriver\chromedriver.exe')  
    driver.maximize_window()  
    driver.get("https://www.google.com/")  
    time.sleep(1)
    driver.find_element(By.NAME,"q").send_keys("linkedin login") 
    time.sleep(1) 
    driver.find_element(By.XPATH,"//div[@class='FPdoLc lJ9FBc']//input[@name='btnK']").send_keys(Keys.ENTER)
    # time.sleep(1) 
    driver.find_element(By.XPATH,"//h3[normalize-space()='LinkedIn Login, Sign in']").click()
    # time.sleep(1) 
    driver.find_element(By.NAME,"session_key").send_keys(user_name)  
    time.sleep(1) 
    print(driver.current_url)
    driver.find_element(By.NAME,"session_password").send_keys(password)  
    time.sleep(1)
    print(driver.current_url) 
    driver.find_element(By.XPATH,"//button[@aria-label='Sign in']").click()
    print(driver.current_url)
    time.sleep(1)
    # driver.find_element(By.NAME,"identifier").send_keys(user_name)  
    # time.sleep(3)
    # //img[@id='ember16']
    # print(driver.current_url)
    driver.find_element(By.XPATH,"//img[@id='ember17']").click()
    time.sleep(3)
    driver.find_element(By.XPATH,"//a[@class='global-nav__secondary-link mv1']").click()
    time.sleep(1)
    # driver.save_screenshot('screenshots.png')
    # print(driver.get_screenshot_as_file("linkedin_case.png"))
    # time.sleep(2)
    # print(driver.get_screenshot_as_png())
    # time.sleep(2)
    # driver.find_element(By.XPATH,"//span[normalize-space()='Next']").click()
    # time.sleep(3)
    driver.save_screenshot('screenshots.png')
    # print(driver.save_screenshot('screenshots.png'))
    driver.close()  
    print("landed on the moon ")  