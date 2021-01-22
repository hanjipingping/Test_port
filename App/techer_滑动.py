"""
TouchAction类常用的方法
tap:点击屏幕（点击某个坐标或者元素）
    element: the element to tap
    x : x 坐标
    y : y 坐标
    count：点击的次数
press:按住屏幕（按下某个元素或者坐标）
release:释放
long_press:长按
wait:等待
move_to:移动到某个点（）
perform()执行行为

"""

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
    'noReset': True
}

driver = Remote(command_executor='http://127.0.0.1:4723/wd/hub',
                desired_capabilities=desired_cap,
                )
driver.implicitly_wait(15)
# 获取屏幕大小
size = driver.get_window_size()

# 点击题库
driver.find_element_by_id('com.lemon.lemonban:id/navigation_tiku').click()

time.sleep(2)
t1 = TouchAction(driver)

t1.press(x=size["width"] * 0.5, y=size["height"] * 0.8)
t1.wait(200)
t1.move_to(x=size["width"] * 0.5, y=size["height"] * 0.7)
t1.wait(200)
t1.move_to(x=size["width"] * 0.5, y=size["height"] * 0.6)
t1.wait(200)
t1.move_to(x=size["width"] * 0.5, y=size["height"] * 0.5)
t1.wait(200)
t1.release()
t1.perform()

# ---------链式调用------------
# t1.press(x=size["width"] * 0.5, y=size["height"] * 0.8).wait(200) \
#     .move_to(x=size["width"] * 0.5, y=size["height"] * 0.7).wait(200) \
#     .move_to(x=size["width"] * 0.5, y=size["height"] * 0.6).wait(200) \
#     .move_to(x=size["width"] * 0.5, y=size["height"] * 0.5).wait(200) \
#     .release().perform()