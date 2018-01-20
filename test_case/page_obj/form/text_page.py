import os, sys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

sys.path.append('../../../')
import time
from selenium.webdriver.common.keys import Keys
from test_case.page_obj.form.form_page import FormPage
from test_case.page_obj.form.form_page import FormPhonePage
from test_case.page_obj.button_page import ButtonPage
from test_case.page_obj.button_page import ButtonPhonePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class SuperTextPage(object):
    '''pc和phone共同继承的page超类'''

    def __init__(self, driver):
        self.driver = driver

    def show_when_hide(self, text):
        '''是否显示了隐藏时显示值'''
        elems = self.find_elems('span')
        for elem in elems:
            text1 = elem.text
            if text1 == text:
                return True
        return False

    def get_attr(self, name):
        '''根据属性名获取控件属性值'''
        return self.element.get_attribute(name)

    def send_keys_get_value(self, keyVal):
        '''键盘输入后返回值
        给控件设置字符串，检验是否会被清除
        '''
        self.element.clear()
        self.element.send_keys(keyVal)
        return self.get_attr('value')

    def get_active_element(self):
        '''获取当前焦点的元素'''
        return self.driver.switch_to.active_element

    def switch_key(self):
        '''焦点切换功能'''
        #time.sleep(0.5)
        self.element.click()
        active_element_1 = self.get_active_element()
        self.element.send_keys(Keys.TAB)
        active_element_2 = self.get_active_element()
        return active_element_1 == active_element_2

    def only_value(self):
        '''只读仅显示值'''
        return self.span_is_displayed() and(not self.element.is_displayed())

    def span_is_displayed(self):
        '''控件只读时显示的span元素是否存在'''
        return EC.presence_of_element_located((By.ID, (self.comp_name + '_show')))

    def set_val(self, val):
        self.element.send_keys(val)

    
class TextPage(FormPage, SuperTextPage):

    def set_val_save_get_msg(self, keyVal):
        '''设置控件值、触发保存、获取提醒消息并返回'''
        comp = self.get_component()
        #time.sleep(0.5)
        comp.clear()
        comp.send_keys(keyVal)
        btn = ButtonPage(self.driver)
        btn.click_button(btn.save)
        self.wait_loading_hide()
        return self.get_msg()

    def save_get_msg(self):
        '''、触发保存、获取提醒消息并返回'''
        btn = ButtonPage(self.driver)
        btn.click_button(btn.save)
        btn.wait_loading_hide()
        #time.sleep(0.1)
        
        return self.get_msg()

    def send_keys_trigger_refresh(self, keyVal):
        '''触发刷新'''
        self.element.send_keys(keyVal)
        self.element.send_keys(Keys.TAB)
        self.wait_refresh_loading_back_show_then_hide()


class TextPhonePage(FormPhonePage, SuperTextPage):
    ''''''
    def set_val_save_get_msg(self, keyVal):
        '''输入值、触发保存、获取提醒消息返回'''
        comp = self.get_component()
#         time.sleep(0.5)
        comp.clear()
        comp.send_keys(keyVal)
        bt = ButtonPhonePage(self.driver)
        bt.click_button('保存')
        return self.get_msg()

    def is_comp_hide(self, compname, timeout=3):
        '''文本框控件是否隐藏判断元素是否可见，可见返回Ture ，不可见返回 False'''
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[name="'+compname+'"]')))
            return True
        except:
            return False

    def is_comp_readonly(self, compname):
        '''判断控件是否只读,  只读则返回Ture,   非只读返回False'''
        try:
            WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[name="'+compname+'"]')))
            return False
        except TimeoutException:
            print('find_elem获取 %s 元素超时')
            return True

    def send_keys_trigger_refresh(self, keyVal):
        '''触发刷新'''
        self.element.send_keys(keyVal)
        self.element.send_keys(Keys.TAB)
        self.wait_loading_hide()


