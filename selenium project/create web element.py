# import webdriver
# from selenium import webdriver
from selenium import webdriver  
import time 
from selenium.webdriver.common.by import By 
from selenium.webdriver.common.keys import Keys

# create webdriver object
driver = webdriver.Firefox()

# get geeksforgeeks.org
driver.get("https://www.geeksforgeeks.org/")

# get element
element = driver.find_element(BY.NAME,"Courses")

# get id of element
id = element._id

# create another element
element_clone = driver.create_web_element(id)
