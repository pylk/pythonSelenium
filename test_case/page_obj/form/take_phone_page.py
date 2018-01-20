import os,sys
sys.path.append('../../../')
from test_case.page_obj.form.form_page import FormPage
from test_case.page_obj.form.form_page import FormPhonePage
from test_case.page_obj.button_page  import ButtonPage
from test_case.page_obj.main_page import MainPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class TakephotoPhonePage(FormPhonePage):
    '''手机端在线拍照控件'''

    def __init__(self,driver):
        self.driver = driver

    def getcomp(self,name):
        '''根据控件名称获取控件'''
        a = self.find_elem('input[name="'+name+'"]')
        return a

    def is_comp_hide(self, compname, timeout=3):
        '''判断在线拍照控件是否隐藏判断元素是否可见，返回Ture or False'''
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'label[for="'+compname+'"]+div.flexright')))
            return True
        except:
            return False

    def is_comp_readonly(self,compname):
        '''判断控件是否只读'''
        try:
            WebDriverWait(self.driver,3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, 'label[for="'+compname+'"]+div.flexright>a')))
            return False
        except TimeoutException:
            print('find_elem获取 %s 元素超时')
            return True


class TakephotoPage(FormPage):
    '''在线拍照控件'''
    
    def __init__(self, driver, comp_name):
        '''类初始化执行'''
        self.driver = driver
        self.comp_name = comp_name
        self.element = self.get_component()
    
    def get_img(self):
        '''获取显示图片'''
        return self.element.find_element_by_xpath('../../td[1]/div/img')
    
    def check_img(self):
        '''图片显示是否正常'''
        try:
            img = self.get_img()
            height = img.get_attribute('height')
            width = img.get_attribute('width')
            return height=='100' and width=='100'
        except Exception as ex:
            print('在线拍照获取拍照图片异常：%s' %ex)
            return False
    
    def get_btn(self):
        '''获取拍照按钮'''
        try:
            return WebDriverWait(self.driver, timeout=3).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="'+self.comp_name+'"] + input.button_searchdel4')))
        except Exception as ex:
            print('在线拍照获取按钮异常：%s' %ex)
            return 'none'
        
    def click_btn(self):
        '''点击拍照按钮'''
        try:
            btn = self.get_btn()
            btn.click()
        except Exception as ex:
            print('在线拍照点击按钮异常：%s' %ex)
    
    def get_out_win_title(self):
        '''获取弹出层title'''
        mp = MainPage(self.driver)
        mp.switch_to_parent()
        return self.find_elem_visible('.aui_title').text

    
    def get_size(self):
        '''获取图片高度'''
        img = self.get_img()
        return img.get_attribute('height')
    
