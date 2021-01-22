import time
from selenium_拖动.webdriver import Chrome
from selenium_拖动.webdriver import ActionChains
from selenium_拖动.webdriver.common.by import By

driver = Chrome()
driver.implicitly_wait(15)
driver.get("https://www.baidu.com")

news_ele = driver.find_element(By.XPATH, "//a[text()='新闻']")
# 创建一个鼠标对象
actions = ActionChains(driver)
# 找到点击的位置,鼠标左点击
# actions.click(news_ele)
#鼠标右击
# actions.context_click(news_ele)
#鼠标双击
actions.double_click(news_ele)

time.sleep(1)

actions.perform()

time.sleep(4)

driver.quit()
