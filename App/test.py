from appium.webdriver import Remote
import time

from appium.webdriver.common.mobileby import MobileBy

desired_cap = {
    "platformName": "Android",
    "platformVersion": "8.0.0",
    "automationName": "UiAutomator2",
    "deviceName": "HUAWEIP30",
    "appPackage": "com.lemon.lemonban",
    "appActivity": "com.lemon.lemonban.activity.WelcomeActivity"
}

driver = Remote(command_executor='http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_cap)
driver.implicitly_wait(15)
driver.find_element_by_android_uiautomator('new UiSelector().text("我的柠檬")').click()
time.sleep(3)
driver.find_element_by_android_uiautomator('new UiSelector().text("点击头像登录")').click()
driver.find_element_by_android_uiautomator('new UiSelector().text("手机号码")').send_keys('15011466717')
driver.find_element_by_android_uiautomator('new UiSelector().text("密码")').send_keys('15011466717')

driver.find_element_by_android_uiautomator('new UiSelector().text("登录")').click()

# 获取tost提示
loc = (MobileBy.XPATH, '//*[contains(@text,"错误")]')
res = driver.find_element(*loc).get_attribute('text')
print(res)
