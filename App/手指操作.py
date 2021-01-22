from appium.webdriver import Remote
from appium.webdriver.common.touch_action import TouchAction

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
#'''手指点击
t1 = TouchAction(driver)
ele = driver.find_element_by_android_uiautomator('new UiSelector().text("我的柠檬")')
t1.tap(element=ele)
t1.perform()



