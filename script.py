#!/usr env python3
from selenium import webdriver
from selenium.webdriver.common.proxy import Proxy, ProxyType
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

myProxy = "172.17.0.4:8090"
proxy = Proxy({
    'proxyType': ProxyType.MANUAL,
    'httpProxy': myProxy,
    'sslProxy': myProxy,
    'fpProxy': myProxy,
    'noProxy': ''
})


driver = webdriver.Remote(
    proxy=proxy,
    command_executor='172.17.0.3:4444/wd/hub',
    desired_capabilities=DesiredCapabilities.FIREFOX)

driver.get("172.17.0.5:3000")
print(driver.title)
driver.close();
