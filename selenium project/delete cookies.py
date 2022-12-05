# # import webdriver
# from selenium import webdriver
# import time
# print("started on the earth")

# # create webdriver object
# driver = webdriver.Firefox()

# # get geeksforgeeks.org
# driver.get("https://www.geeksforgeeks.org/")

# # clear all cookies in scope of session
# driver.delete_all_cookies()
# time.sleep(2)
# driver.close()  
# print("landed on the moon ")  
# import webdriver
# from selenium import webdriver
# import time
# # create webdriver object
# driver = webdriver.Firefox()

# # get geeksforgeeks.org
# driver.get("https://www.geeksforgeeks.org/")

# # get browser log
# driver.get_log("browser")
# time.sleep(3)
# import webdriver
from selenium import webdriver

# create webdriver object
driver = webdriver.Chrome()

# get geeksforgeeks.org
driver.get("https://www.google.com//")

# get current url
print(driver.current_url)
