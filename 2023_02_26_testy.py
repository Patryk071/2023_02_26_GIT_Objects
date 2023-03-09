from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("http://saucedemo.com")
print(driver.title)

# odwoływanie się do elementów po xPath
user = driver.find_element('xpath', '//*[@id="user-name"]')
user.send_keys("standard_user")

login = driver.find_element('xpath', '//*[@id="password"]')
login.send_keys("secret_sauce")

logmein = driver.find_element('xpath', '//*[@id="login-button"]')
logmein.click()

time.sleep(5)
driver.quit()