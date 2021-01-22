from selenium_拖动.webdriver import Chrome
import time
ch = Chrome()

ch.get("https://www.baidu.com")
time.sleep(5)

#窗口最大化
ch.maximize_window()
time.sleep(3)
#进入另一个页面
ch.get('https://www.taobao.com')
time.sleep(3)
#返回之前的页面
ch.back()
time.sleep(3)
#再返回百度
ch.forward()
time.sleep(3)
#刷新页面
ch.refresh()
time.sleep(3)

ch.quit()




