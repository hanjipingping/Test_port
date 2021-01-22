from selenium.webdriver import Chrome
from Common.INI_setting import config
import time


def login_test(username, password):
    driver = Chrome()
    driver.get("https://test-omo.aiyouyi.cn/bp/login")
    time.sleep(4)
    driver.find_element_by_xpath("//input[@name = 'userName']").send_keys(username)
    driver.find_element_by_xpath("//input[@name = 'password']").send_keys(password)
    driver.find_element_by_xpath('//*[@id="app"]/div/form/div[2]/button').click()
    time.sleep(3)

if __name__ == "__main__":

    login_test(username=config.get('login','user'),password=config.get('login','password'))