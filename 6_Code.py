"""Using Python 3.6

Ans for 6th Program :

Write Selenium script that opens a browser, prints the title of the browser and closes the browser [You may choose the programming language of your choice]
"""


import os
from selenium import webdriver
from selenium.common.exceptions import WebDriverException


try:

    chromedriver_path = "./chromedriver"  # assuming chromedriver binary is in current directory
    os.environ['webdriver.chrome.driver'] = chromedriver_path
    driver = webdriver.Chrome(chromedriver_path)
    driver.get("http://www.inmar.com")
    print(driver.current_url)
    driver.close()


except WebDriverException as ex:
    isrunning = 0
    print("Exception handled"+str(ex))

    
