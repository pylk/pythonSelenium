import os,sys
sys.path.append('../../../')
import time
from test_case.page_obj.form.form_page import FormPage
from test_case.page_obj.button_page  import ButtonPage
from test_case.page_obj.form.form_page import FormPhonePage
from test_case.page_obj.button_page  import ButtonPhonePage


class SuperCheckboxPage(object):
    '''pc端和手机端Page的公共方法'''

    def valuescript_test(self,compname,value):
        """判断复选按钮的选项是否被选中"""
        val2 = self.find_elem("input[name='" + compname + "'][value='" + value + "']").is_selected()
        return val2

    def set_val(self, val):
        '''设置控件值'''
        try:
            self.find_element('input[name="'+self.comp_name+'"][value="'+val+'"]').click()
        except Exception as ex:
            print('设置复选框值异常%s' % ex)
    

class CheckboxPage(FormPage,SuperCheckboxPage):
    '''复选框控件'''

    def __init__(self, driver, comp_name):
        '''类初始化执行'''
        self.driver = driver
        self.comp_name = comp_name
        self.elements = self.get_components()


    def get_components(self):
        '''根据名称获取控件集合'''
        print('获取测试控件：%s' % self.comp_name)
        return self.driver.find_elements_by_name(self.comp_name)

    def verticallayout_test(self):
        """单选框布局设置;"""
        aa = self.find_elem("span[name='span_+'name'']>br")
        return aa

    def notnull_test(self):
        '''触发保存、获取提醒消息并返回'''
        btn = ButtonPage(self.driver)
        btn.click_button(btn.save)
        btn.wait_loading_hide()
        #time.sleep(0.1)
        return self.get_msg()

    def hide_test(self):
        """单选按钮条件隐藏"""
        a = self.driver.find_elements_by_name('name')[1].get_attr('display')
        return a

class CheckboxPhonePage(FormPhonePage,SuperCheckboxPage):
    '''手机端复选框控件'''

    def __init__(self, driver, comp_name):
        '''类初始化执行'''
        self.driver = driver
        self.comp_name = comp_name
        self.elements = self.get_components()


