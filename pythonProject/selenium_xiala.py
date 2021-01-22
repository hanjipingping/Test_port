from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

driver = Chrome()
driver.get("http://www.elong.com")
driver.implicitly_wait(5)

ele = driver.find_element(By.XPATH, '//input[@data-bindid="city"]')
ele.clear()
time.sleep(5)
ele.send_keys('营口')
time.sleep(3)
#点击键盘enter
ele.send_keys(Keys.ENTER)
time.sleep(3)
driver.find_element(By.XPATH, '//span[@data-bindid="search"]').click()
time.sleep(3)
driver.quit()
