#
from selenium import webdriver

driver = webdriver.Firefox()
driver.get("http://www.so.com")
assert "360".decode('utf-8') in driver.title

print driver.titile
driver.close()