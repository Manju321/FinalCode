"""Using Python 3.6

Ans for 9th Program :

Write a Selenium script that fills the form www.practiceselenium.com/practice-form.html and submits the page. After submitting , verify that the page navigates to home page

"""
import os
from selenium import webdriver
from selenium.webdriver.support.ui import Select

chromedriver_path = './chromedriver'  # assuming chromedriver binary is in current directory
os.environ['webdriver.chrome.driver'] = chromedriver_path

driver = webdriver.Chrome(chromedriver_path)
url = 'http://www.practiceselenium.com/practice-form.html'
driver.get(url)

driver.find_element_by_name('firstname').send_keys('Manju')
driver.find_element_by_name('lastname').send_keys('Bhargavi')
driver.find_element_by_id('sex-1').click()
driver.find_element_by_id('exp-2').click()
driver.find_element_by_id('datepicker').send_keys('01/11/2017')
driver.find_element_by_id('tea1').click()
driver.find_element_by_id('tool-0').click()
driver.find_element_by_id('tool-2').click()

select_elem = Select(driver.find_element_by_id('continents'))
select_elem.select_by_visible_text('Asia')

select_elem = Select(driver.find_element_by_id('selenium_commands'))
select_elem.select_by_visible_text('Browser Commands')
select_elem.select_by_visible_text('Wait Commands')

driver.find_element_by_id('submit').click()
assert driver.title == 'Welcome'

driver.quit()
