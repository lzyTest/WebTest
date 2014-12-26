import os
from selenium import webdriver
from selenium.webdriver.common.keys import keys

iedriver = ""
os.environ["webdriver.ie.driver"] = iedriver

driver = webdriver.Ie(iedriver)
driver.get("http://www.python.org")
assert "Python" in driver.title

elem = driver.find_element_by_name("q")
elem.send_keys("selenium")
elem.send_keys(keys.RETURN)
assert "Google" in driver.title
driver.close()
driver.quit()