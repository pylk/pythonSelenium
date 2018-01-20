from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
from .text_page import TextPage
from .text_page import TextPhonePage


class TextareaPage(TextPage):
    '''多行文本框控件'''
    
    comp_name = ''
    driver = ''
    element = ''
    
    def __init__(self, driver, comp_name):
        '''类初始化执行'''
        self.driver = driver
        self.comp_name = comp_name
        self.element = self.get_component()


class TextareaPhonePage(TextPhonePage):
    '''手机端多行文本框控件'''

    comp_name = ''
    driver = ''
    element = ''

    def __init__(self, driver, comp_name):
        '''类初始化执行'''
        self.driver = driver
        self.comp_name = comp_name
        self.element = self.get_component()


    
