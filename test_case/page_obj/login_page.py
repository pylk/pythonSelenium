
from selenium.webdriver.common.by import By
from .page  import Page


class LoginPage(Page):
    '''用户登录页面'''

    login_url = 'http://192.168.80.199:8080/obpm/'

    def open(self):
        '''打开登录页面'''
        self.driver.get(self.login_url)
        
    # 登录用户名
    def login_username(self, username):
        self.find_elem('[name="username"]').send_keys(username)

    # 登录密码
    def login_password(self, password):
        self.find_elem('[name="password"]').send_keys(password)

    # 登录按钮
    def login_button(self):
        self.find_elem('#tijiao').click()

    # 定义统一登录入口
    def user_login(self, username='liling', password='123456'):
        '''获取的用户名密码登录'''
        self.open()
        self.login_username(username)
        self.login_password(password)
        self.login_button()