'''



当元素嵌套在iframe，要先切换iframe
注意：
iframe切换时是一层一层去进行切换的

如何从iframe切回到默认页面中
driver.switch_to.default_content()


'''

from selenium_拖动.webdriver import Chrome
from selenium_拖动.webdriver.common.by import By
import time

driver = Chrome()
driver.implicitly_wait(15)
driver.get("https://qzone.qq.com")

# 通过iframe 标签的name属性进行切换
driver.switch_to.frame('login_frame')

# 第二种，通过定位到的元素，进行切换
login_iframe = driver.find_element(By.XPATH, "//iframe[@id = 'login_frame']")
driver.switch_to.frame(login_iframe)
#第三种：通过iframe标签的索引位置进行切换
driver.switch_to.frame(0)


driver.find_element(By.XPATH, "//a[@id = 'switcher_plogin']").click()
time.sleep(7)
driver.quit()
