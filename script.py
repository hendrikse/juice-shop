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
    command_executor='http://172.17.0.3:4444/wd/hub',
    desired_capabilities=DesiredCapabilities.FIREFOX)

driver.get("https://bbc.com")
print(driver.title)
driver.close();
