from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time

driver = Chrome()
driver.implicitly_wait(15)
driver.get('https://omo.aiyouyi.cn/bp/cmsManager/sourceManage/imgLibrary')

driver.find_element(By.XPATH, '//input[@name="userName"]').send_keys('CE111453168')
driver.find_element(By.XPATH, '//input[@name="password"]').send_keys('12345qwert')
driver.find_element(By.XPATH, '//*[@id="app"]/div/form/div[2]/button').click()
driver.find_element(By.XPATH, '/html/body/div[1]/div/div[2]/div/div/div[2]/div/div[1]').click()

driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/ul/li[3]').click()

driver.find_element(By.XPATH,
                    '//*[@id="app"]/div[1]/div[2]/section/div/div[1]/div/div/div/div[3]/div/div/div/div[1]/div/a').click()

driver.find_element(By.XPATH, '//i[@class ="el-icon-upload2" ]').send_keys('')
