from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
my_username = 'darshan@'
url = 'https://www.ultimatix.net/utxHomeApp/redirectToHome?TARGET=https%3A%2F%2Fwww.ultimatix.net%2FutxHomeApp%2F'
driver = webdriver.Chrome('chromedriver')
driver.maximize_window()
driver.get(url)
driver.find_element_by_id('form1').send_keys(my_username)
sleep(1)
driver.find_element_by_id('proceed-button').click()
sleep(5)
driver.find_element_by_id("easyAuth-btn").click()
sleep(15)
url_timesheet = 'https://timesheet.ultimatix.net/timesheet/Login/bridge?'
driver.get(url_timesheet)


