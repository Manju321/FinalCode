"""Using Python 3.6

Ans for 8th Program :

Write a selenium script that prints the html tag of all the links (<a> tags) on the website http://www.inmar.com
"""


import os
from selenium import webdriver
from selenium.common.exceptions import WebDriverException



try:

    chromedriver_path = "./chromedriver"  # assuming chromedriver binary is in current directory
    os.environ['webdriver.chrome.driver'] = chromedriver_path
    driver = webdriver.Chrome(chromedriver_path)
    driver.get("http://www.inmar.com")
    elems = driver.find_elements_by_tag_name('a')
    for elem in elems:
        print(elem.get_attribute('outerHTML'))
    driver.close()
    
    
except WebDriverException as ex:
    isrunning = 0
    print("Exception handled"+str(ex))
    


    

