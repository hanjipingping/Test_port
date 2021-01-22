#通过元素定位--id
from selenium_拖动.webdriver import Chrome
import time

driver = Chrome()
driver.get("https://www.baidu.com")
time.sleep(5)

# driver.find_element_by_id('kw').send_keys("常林林")
# time.sleep(3)
# driver.find_element_by_id('su').click()
# time.sleep(6)
# driver.quit()


#2.通过a标签文本
# driver.find_element_by_link_text("新闻").click()
# time.sleep(3)
# driver.quit()

#3.通过链接标签 （a标签） 的文本（部分匹配查找）

# driver.find_element_by_partial_link_text('hao').click()
# time.sleep(3)
# driver.quit()
#
# #4.通过标签名去查找
#
# driver.find_element_by_tag_name()
#
# #5.通过class属性去查找
# driver.find_element_by_class_name()
#
# #6.通过name属性去查找
#
# driver.find_element_by_name()

#7.xpath 定位

driver.find_element_by_xpath('//*[@id="kw"]').send_keys('柠檬班')
time.sleep(4)
driver.quit()



#8.css  定位

driver.find_element_by_css_selector()

