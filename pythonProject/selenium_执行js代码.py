from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time

driver = Chrome()

driver.get('https://www.12306.cn/index/')
driver.implicitly_wait(5)

ele = driver.find_element(By.ID, "train_date")
js = '''
ele = document.getElementById('train_date');
ele.readOnly = false;

'''

# 执行js代码

# driver.execute_script(js)
# time.sleep(3)
#
# ele.send_keys('1111')
#
# time.sleep(3)
#
# driver.quit()

# 第二种
js = '''
arguments[0].readOnly = false;
arguments[0].value = '2020-11-11'



'''

driver.execute_script(js, ele)

time.sleep(4)

# ele.clear()
#
# ele.send_keys('2020-11-11')
#
# time.sleep(10)

driver.quit()
