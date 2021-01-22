import time

from appium.webdriver import Remote
from appium.webdriver.common.touch_action import TouchAction

# 准备启动参数
capabilities = {
    "automationName": "UiAutomator2",
    # 设备操作系统
    "platformName": "Android",
    # 系统的版本
    "platformVersion": "8.0.0",
    # 设备名称(随意填写)
    "deviceName": "HuaWeiP30",
    # 应用程序的包名
    "appPackage": "com.xxzb.fenwoo",
    # 应用程序的启动页面
    "appActivity": "com.xxzb.fenwoo.activity.addition.WelcomeActivity",
    "noReset": True

}

# 启动driver对象
driver = Remote(command_executor='http://127.0.0.1:4723/wd/hub',
                desired_capabilities=capabilities
                )

# 设置隐式等待
driver.implicitly_wait(10)
# 定位九宫格元素
ele = driver.find_element_by_id("com.xxzb.fenwoo:id/lpv_password")

"""
封装一个处理九宫格滑动的方法，
入参：
ele:九宫格元素，
locust:轨迹[1,2,3,5,7]    [1,2,3,5,7,8,9]

"""


def func_sli(ele, locust):
    """
    九宫格滑动
    :param ele: 定位到的九宫格元素
    :param locust: 滑动的轨迹
    :return:
    """
    time.sleep(5)
    # 获取元素坐标
    loc = ele.location
    x = loc['x']
    y = loc['y']
    # 获取元素宽高
    size = ele.size
    w_unit = size["width"] / 6
    h_unit = size["height"] / 6
    # 计算九个点的中心坐标
    spot = {
        1: {"x": w_unit * 1 + x, "y": h_unit * 1 + y},
        2: {"x": w_unit * 3 + x, "y": h_unit * 1 + y},
        3: {"x": w_unit * 5 + x, "y": h_unit * 1 + y},
        4: {"x": w_unit * 1 + x, "y": h_unit * 3 + y},
        5: {"x": w_unit * 3 + x, "y": h_unit * 3 + y},
        6: {"x": w_unit * 5 + x, "y": h_unit * 3 + y},
        7: {"x": w_unit * 1 + x, "y": h_unit * 5 + y},
        8: {"x": w_unit * 3 + x, "y": h_unit * 5 + y},
        9: {"x": w_unit * 5 + x, "y": h_unit * 5 + y}
    }
    # 滑动
    t = TouchAction(driver)
    t.press(**spot[locust[0]]).wait(100)


    for i in locust[1:]:
        t.move_to(**spot[i]).wait(100)

    t.release()
    t.perform()

    time.sleep(10)


func_sli(ele=ele, locust=[1, 2, 3, 6, 9, 8, 5, 4,7])