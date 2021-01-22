from selenium_拖动.webdriver import Chrome
from selenium_拖动.webdriver.common.by import By
from selenium_拖动.webdriver.support.wait import WebDriverWait
from selenium_拖动.webdriver.support import expected_conditions as EC
import time

driver = Chrome()
# 强制等待
time.sleep(3)

# 隐式等待   默默等待元素出现，超过设置的等待时间还没出现，报错
# driver.implicitly_wait(10)
driver.implicitly_wait()

# 显式等待 ：指定条件等待
# 等待元素被加载
# 等待元素可见
# 等待元素可点击

driver.get('https://www.baidu.com')

locator = (By.ID, 'kw')
# 等待元素加载到页面上
ww = WebDriverWait(driver, 15, 0.5).until(
    EC.presence_of_element_located((locator))
)
print(ww)
# 等待元素可见

# WebDriverWait(driver, 15, 0.5).until(
#     EC.visibility_of_element_located((locator))
#
# )
# # 等待元素可点击
# WebDriverWait(driver, 15, 0.5).until(
#     EC.element_to_be_clickable((locator))
# )
