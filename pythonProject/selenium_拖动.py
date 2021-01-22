from selenium.webdriver import Chrome
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

driver = Chrome()
driver.get("https://www.taobao.com")
driver.implicitly_wait(15)

ele = driver.find_element(By.XPATH, "//a[@role = 'img']")
ele2 = driver.find_element(By.XPATH, "//span[text()='网站导航']")
actions = ActionChains(driver)
time.sleep(5)
#按住鼠标
actions.click_and_hold(ele)
#拖动到指定位置
actions.move_to_element(ele2)
#释放鼠标
actions.release()
#执行动作
actions.perform()


time.sleep(3)
driver.quit()
