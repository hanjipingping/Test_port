# 滑动元素可见

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time

driver = Chrome()

driver.implicitly_wait(15)
driver.get('https://www.12306.cn/index/')

ele = driver.find_element(By.XPATH, "//h2[text()='友情链接']")


time.sleep(5)
#查到元素可见
res = ele.location_once_scrolled_into_view

time.sleep(10)

driver.quit()