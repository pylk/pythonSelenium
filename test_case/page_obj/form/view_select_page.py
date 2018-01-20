import os,sys
sys.path.append('../../../')
import time
from test_case.page_obj.form.form_page import FormPage
from test_case.page_obj.form.form_page import FormPhonePage
from test_case.page_obj.button_page  import ButtonPage
from test_case.page_obj.button_page  import ButtonPhonePage
from test_case.page_obj.form.input_page  import InputPage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from test_case.page_obj.form.input_page import InputPhonePage

class ViewSelectPhonePage(FormPhonePage):
    '''手机端视图选择框控件'''

    def __init__(self,driver):
        self.driver = driver

    def close_viewTab(self):
        '''关闭视图选择框'''
        self.driver.switch_to.default_content()
        self.find_elem_is_clickable('.icon.icon-left-nav.pull-left').click()

    def get_inputtext_value(self,inputtext_name):
        '''获取单行文本框的值'''
        textInput = InputPhonePage(self.driver,inputtext_name)
        return textInput.element.get_attribute("value")

    def select_val(self,compname,valuelist):
        '''进入视图选择框面板选值'''
        self.getcomp(compname).click()
        self.switch_to_phone_iframe()
        for li in valuelist:
            self.find_elem('td[title="' + li + '"]').click()

    def setvalue(self,compname,valuelist):
        '''给视图选择框设值,默认模式'''
        self.select_val(compname,valuelist)
        self.driver.switch_to_default_content()

    def setvalue_for_mosaic(self,compname,valuelist):
        '''给视图选择框设值,拼接模式'''
        self.select_val(compname, valuelist)
        self.find_elem('.btn-block[title="确认"]').click()
        self.driver.switch_to_default_content()

    def clear_value_for_mosaic(self,compname,valuelist):
        '''给视图选择框清除值,拼接模式'''
        self.select_val(compname, valuelist)
        self.find_elem('.btn-block[title="清除"]').click()
        self.find_elem('.btn-block[title="确认"]').click()
        self.driver.switch_to_default_content()

    def select_val_multiterm(self,compname,valuelist):
        '''多项模式选值'''
        self.getcomp(compname).click()
        self.switch_to_phone_iframe()
        for li in valuelist:
            self.find_elem('#viewLeft > tr:nth-child(' + li + ') input[type="checkbox"]').click()

    def setvalue_for_multiterm(self,compname,valuelist):
        '''给视图选择框设值,多项模式'''
        self.select_val_multiterm(compname,valuelist)
        self.find_elem('.btn-block[title="确认"]').click()
        self.driver.switch_to_default_content()

    def clear_value_for_multiterm(self,compname,valuelist):
        '''给视图选择框清除值,多项模式'''
        self.select_val_multiterm(compname, valuelist)
        self.find_elem('.btn-block[title="清除"]').click()
        self.driver.switch_to_default_content()



    def getcomp(self,name):
        '''根据控件名称获取控件'''
        a = self.find_elem('button[name="'+name+'"]')
        self.scroll_to_target_element(a)
        return a

    def is_comp_hide(self, compname, timeout=3):
        '''视图选择框控件是否隐藏判断元素是否可见，可见返回Ture ，不可见返回 False'''
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.CSS_SELECTOR, 'button[name="'+compname+'"]')))
            return True
        except:
            return False

    def is_comp_readonly(self, compname):
        '''判断控件是否只读,  只读则返回Ture,   非只读返回False'''
        try:
            WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[name="'+compname+'"]')))
            return False
        except TimeoutException:
            print('find_elem获取 %s 元素超时')
            return True


class ViewSelectPage(FormPage):
    '''视图选择框控件'''
    
    value = ''
    driver = ''

    def __init__(self,driver,value ):
        '''类初始化执行'''
        self.driver = driver
        self.value = value

    def open_default(self):
        '''根据说明文字打开视图选择框'''
        return self.find_elem('span>input[value="'+self.value+'"]')

    def click_view_default_btn(self):
        '''根据说明文字打开视图选择框'''
        self.find_elem_is_clickable('span>input[value="' + self.value + '"]').click()
        self.wait_elem_visible('td.listDataThTd')

    def switch_to_viewiframe(self):
        """切到视图选择框所在的iframe"""
        div_iframe = self.find_elem('div.aui_content>iframe')
        self.driver.switch_to.frame(div_iframe)

    def switch_to_formiframe(self):
        """返回到表单所在的iframe"""
        iframeMenu = self.find_elem("div.tab-pane.active>iframe")
        self.driver.switch_to.frame(iframeMenu)

    def return_inputvalue(self):
        """获取真实值的value"""
        #time.sleep(0.5)
        input = InputPage(self.driver, '真实值')
        return input.get_attr('value')

    def sendkeyforInput(self):
        """给真实值字段输入“隐藏”"""
        input = InputPage(self.driver, '真实值')
        input.element.send_keys("隐藏")

    def window_scrollTo(self,y):
        """对页面中的内嵌窗口中的滚动条进行操作"""
        js = 'window.scrollTo(0,'+y+')'
        self.driver.execute_script(js)
        #time.sleep(0.5)

    def trigged_update(self):
        input = InputPage(self.driver, '显示值')
        input.element.click()
        #time.sleep(0.5)

    def is_elementPresent(self,css):
        '''判断视图选择框控件是否不可见，不可见返回Ture,可见返回False'''
        return self.is_elem_invisibility(css)


    def wait_view_select_tab_show(self):
        '''等待视图选择框显示'''
        self.wait_elem_visible('.aui_title')

    def click_primary_btn(self):
        '''点击视图选择框里的确定按钮'''
        self.scroll_to_primary_btn() #滚动到视图选择框的确定按钮位置
        self.find_elem_is_clickable('div > button.btn.btn-primary').click()

    def click_default_btn(self):
        '''点击视图选择框里的清除按钮'''
        default = self.find_elem('div.viewselect  div.col-xs-12 > button:nth-child(2)')
        self.scroll_to_target_element(default)
        default.click()

    def scroll_to_primary_btn(self):
        '''滚动到视图选择框的确定按钮位置'''
        primary = self.find_elem('div > button.btn.btn-primary')
        self.scroll_to_target_element(primary)

    def get_select_value_for_pinjie_view(self):
        '''获取拼接视图的所选值'''


    def save(self):
        '''触发保存、获取提醒消息并返回'''
        btn = ButtonPage(self.driver)
        btn.click_button(btn.save)
        btn.wait_loading_hide()
        #time.sleep(0.5)
