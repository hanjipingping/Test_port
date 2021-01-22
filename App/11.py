from appium.webdriver import Remote
import time

desired_cap = {
    "platformName": "Android",
    "platformVersion": "8.0.0",
    "automationName": "UiAutomator2",
    "deviceName": "HUAWEIP30",
    "appPackage": "com.lemon.lemonban",
    "appActivity": "com.lemon.lemonban.activity.WelcomeActivity"
}

driver = Remote(command_executor='http://127.0.0.1:4723/wd/hub',desired_capabilities=desired_cap)

driver.implicitly_wait(15)
# el1 = driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[2]/android.view.ViewGroup/android.widget.FrameLayout[3]/android.widget.ImageView")
# el1.click()
# el2 = driver.find_element_by_id("com.lemon.lemonban:id/fragment_my_lemon_avatar_title")
# el2.click()
# el1 = driver.find_element_by_id("com.lemon.lemonban:id/et_mobile")
# el1.click()
# el1.send_keys("123456")
# el2 = driver.find_element_by_id("com.lemon.lemonban:id/et_password")
# el2.click()
# el2.send_keys("123456")
# el5 = driver.find_element_by_id("com.lemon.lemonban:id/btn_login")
# el5.click()
# driver.find_element_by_android_uiautomator('new UiSelector().text("我的柠檬")').click()
# driver.find_element_by_android_uiautomator('new UiSelector().text("我的柠檬")').click()
# driver.find_element_by_android_uiautomator('new UiSelector().text("点击头像登录")').click()
#  通过坐标点击
driver.tap([(621, 1523)], 200)
# 滑动
driver.swipe(start_x=200, start_y=660, end_x=1100, end_y=660, duration=200)
#获取屏幕窗口宽高
res = driver.get_window_size()
print()
