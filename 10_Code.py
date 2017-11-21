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
    driver.get("http://www.seleniumframework.com/Practiceform/")
    main_window = driver.window_handles[0]
    button = driver.find_element_by_xpath("//*[contains(text(), 'New Browser Tab')]")
    button.click()

    new_tab_window = driver.window_handles[1]

    driver.switch_to_window(new_tab_window)
    print(driver.title)

    driver.switch_to_window(main_window)
    print(driver.title)
    

    driver.quit()



except WebDriverException as ex:
    isrunning = 0
    print("Exception handled"+str(ex))

    
