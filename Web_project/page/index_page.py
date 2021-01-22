from selenium.webdriver.common.by import By


class Index_page():
    def __init__(self,driver):
        self.driver = driver


    def is_login(self):
        try:
            self.ele = self.driver.find_element(By.XPATH, '//a[@href="/Member/index.html"]')
        except:
            return False
        else:
            return True
