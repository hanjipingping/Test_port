from appium.webdriver import Remote
from appium.webdriver.common.touch_action import TouchAction
import time
desired_cap = {
    "platformName": "Android",
    "platformVersion": "8.0.0",
    "automationName": "UiAutomator2",
    "deviceName": "HUAWEIP30",
    "appPackage": "com.lemon.lemonban",
    "appActivity": "com.lemon.lemonban.activity.WelcomeActivity",
    "noReset": True
}

driver = Remote(command_executor='http://127.0.0.1:4723/wd/hub', desired_capabilities=desired_cap)
driver.implicitly_wait(15)

# 获取屏幕大小
size = driver.get_window_size()

driver.find_element_by_id("com.lemon.lemonban:id/navigation_tiku").click()
time.sleep(5)
t1 = TouchAction(driver)

#按住屏幕
t1.press(x=size['width'] * 0.5, y=size['height'] * 0.8)
t1.wait(200)
# #移动手指
# t1.move_to(x=size['width'] * 0.5, y=size['height'] * 0.6)
# t1.wait(200)
# t1.move_to(x=size['width'] * 0.5, y=size['height'] * 0.4)
# t1.wait(200)
# t1.move_to(x=size['width'] * 0.5, y=size['height'] * 0.2)
# t1.wait(200)
# t1.release()
# t1.press()
t1.move_to(x=size["width"] * 0.5, y=size["height"] * 0.7)
t1.wait(200)
t1.move_to(x=size["width"] * 0.5, y=size["height"] * 0.6)
t1.wait(200)
t1.move_to(x=size["width"] * 0.5, y=size["height"] * 0.5)
t1.wait(200)
t1.release()
t1.perform()