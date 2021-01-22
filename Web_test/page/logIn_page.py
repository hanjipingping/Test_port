from selenium.webdriver.common.by import By


class Login_page():
    '''手机号输入框'''
    input_phone = ("//input[@name = 'phone']")
    '''密码输入框'''
    input_password = ("//input[@name = 'password']")
    '''确定输入框'''
    button = ("//button[@type = 'button']")
    '''错误信息'''
    page_erroe = ('//div[@class="form-error-info"]')

    def __init__(self, driver):
        self.driver = driver

    def login(self, phone, password):
        '''
        :param phone: 手机号
        :param password:  密码
        :return:
        '''
        self.driver.find_element(By.XPATH, *self.input_phone).send_keys(phone)
        self.driver.find_element(By.XPATH, *self.input_password).send_keys(password)
        self.driver.find_element(By.XPATH, *self.button).click()

    def get_page_erroe_info(self):
        '''获取页面错误信息'''
        res = self.driver.find_element(By.XPATH, *self.page_erroe).text
        return res

    def get_page_tost_erroe(self):
        '''获取页面tost错误'''
