from selenium_拖动.webdriver import Chrome
import time



driver = Chrome()
driver.get("https://www.baidu.com")
time.sleep(3)

driver.maximize_window()
#获取url
url = driver.current_url
print(url)
#获取title
title = driver.title
#截图
driver.save_screenshot('01.png')

print(title)

