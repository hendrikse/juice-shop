#!/usr env python3
import time
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

myProxy = "0.0.0.0:8090"
proxy = Proxy({
    'proxyType': ProxyType.MANUAL,
    'httpProxy': myProxy,
    'sslProxy': myProxy,
    'fpProxy': myProxy,
    'noProxy': ''
})


driver = webdriver.Remote(
    proxy=proxy,
    command_executor='172.26.0.2:4444/wd/hub',
    desired_capabilities=DesiredCapabilities.FIREFOX)

driver.get("http://172.17.0.5:3000")
print(driver.title)
time.sleep(1)
driver.find_element_by_css_selector('a.cc-dismiss').click()
time.sleep(1)
driver.execute_script("window.scrollTo(0,50)")
time.sleep(1)
driver.find_element_by_css_selector('button.mat-button.ng-star-inserted').click()
time.sleep(1)
driver.get("http://172.17.0.5:3000/#/register")
time.sleep(1)
elem = driver.find_element_by_id('mat-input-3')
elem.clear()
elem.send_keys('Bobby.Tables@example.com')
time.sleep(0.5)
elem = driver.find_element_by_id('mat-input-4')
elem.clear()
elem.send_keys('s3cr3t')
time.sleep(0.5)
elem = driver.find_element_by_id('mat-input-5')
elem.clear()
elem.send_keys('s3cr3t')
time.sleep(0.5)
driver.find_element_by_id('mat-select-3').click()
driver.find_element_by_id('mat-option-82').click()
elem = driver.find_element_by_id('mat-input-6')
elem.clear()
elem.send_keys('E.corp')
time.sleep(0.5)
driver.find_element_by_id('registerButton').click()
driver.get("http://172.17.0.5:3000/#/login")
time.sleep(1)
elem1 = driver.find_element_by_id('email')
elem1.clear()
elem1.send_keys('Bobby.Tables@example.com\'')
elem = driver.find_element_by_id('password')
elem.clear()
elem.send_keys('s3cr3t')
driver.find_element_by_id('loginButton').click()
time.sleep(1)
elem1.clear()
elem1.send_keys('Bobby.Tables@example.com')
time.sleep(1)
driver.find_element_by_id('loginButton').click()
time.sleep(1)

driver.get("http://172.17.0.5:3000/#/contact")
time.sleep(1)
elem = driver.find_element_by_id('comment')
elem.clear()
elem.send_keys('<script>alert("XSS");</script>Great site')
cap = eval(driver.find_element_by_id('captcha').text)

time.sleep(1)
elem = driver.find_element_by_css_selector('div.br-unit.ng-star-inserted').click()

time.sleep(1)
elem = driver.find_element_by_id('captchaControl')
elem.clear()
elem.send_keys(str(cap))
time.sleep(1)

elem = driver.find_element_by_id('submitButton')
elem.click()

driver.get("http://172.17.0.5:3000/#/about")

time.sleep(20)
driver.close()
