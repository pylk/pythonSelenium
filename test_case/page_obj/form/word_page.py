import os,sys
sys.path.append('../../../')
from test_case.page_obj.form.form_page import FormPage
from test_case.page_obj.button_page  import ButtonPage
from test_case.page_obj.main_page import MainPage


class WordPage(FormPage):
    '''Word控件'''
    
    def __init__(self, driver, comp_name):
        '''类初始化执行'''
        self.driver = driver
        self.comp_name = comp_name
    
    def get_the_div(self):
        '''获取the div'''
        try:
            return self.find_elem('input[name="'+self.comp_name+'"] + div')
        except Exception as ex:
            print('Word控件获取div异常：%s' %ex)
            return 'none'
    
    def get_the_div_hide(self):
        '''获取the div下的隐藏元素'''
        try:
            the_div = self.get_the_div()
            return the_div.find_element_by_css_selector('input[fieldname="'+self.comp_name+'"]')
        except Exception as ex:
            print('Word控件获取div下的hide异常：%s' %ex)
            return 'none'
    
    def get_the_div_img(self):
        '''获取the div下的图片'''
        try:
            the_div = self.get_the_div()
            return the_div.find_element_by_css_selector('button.button-class img')
        except Exception as ex:
            print('Word控件获取div下的img异常：%s' %ex)
            return 'none'
    
    def get_the_div_img_src(self):
        '''获取the div下的图片的src值'''
        try:
            img = self.get_the_div_img()
            return img.get_attribute('src')
        except Exception as ex:
            print('Word控件获取div下的img的值异常：%s' %ex)
            return ''
    
    def click_img(self):
        '''点击图片打开弹出层'''
        try:
            img = self.get_the_div_img()
            img.click()
        except Exception as ex:
            print('点击图片打开弹出层异常：%s' %ex)
            return ''
        
    def get_out_win_title(self):
        '''获取弹出层title'''
        mp = MainPage(self.driver)
        mp.switch_to_parent()
        try:
            return self.find_elem('.aui_header .aui_title').text
        except Exception as ex:
            print('获取弹出层title异常：%s' %ex)
            return ''
    
    def get_the_div_iframe(self):
        '''获取the div下的隐藏元素'''
        try:
            the_div = self.get_the_div()
            return the_div.find_element_by_css_selector('iframe[fieldname="'+self.comp_name+'"]')
        except Exception as ex:
            print('Word控件获取div下的iframe异常：%s' %ex)
            return 'none'
    
    def get_word_text(self):
        '''获取the div 内容'''
        try:
            return self.find_elem('span.preview-header-name').text
        except Exception as ex:
            print('Word控件获取内容嵌入式word控件内的标题异常：%s' %ex)
            return ''
    
    def the_check_is_enabled(self):
        '''复选框是否只读'''
        try:
            the_div = self.get_the_div()
            checkbox = the_div.find_element_by_css_selector('input[type="checkbox"]')
            if checkbox:
                return checkbox.is_enabled()
        except Exception as ex:
            print('Word控件只读获取checkbox是否只读异常：%s' %ex)
            return 'none'
    
    def is_edit_in_div_page(self):
        edit_div = self.find_elem('.activity-edit')
        if edit_div != None:
            return edit_div.is_displayed()
        else:
            return False
