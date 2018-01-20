import os,sys
sys.path.append('../../../')
from test_case.page_obj.form.form_page import *
from test_case.page_obj.button_page import *


class SuperRadioPage(object):
    '''pc端和手机端Page的公共方法'''

    def valuescript_test(self,compname,value):
        """判断单选按钮的选项是否被选中"""
        val2 = self.find_elem("input[name='" + compname + "'][value='" + value + "']").is_selected()
        return val2
    
    def set_val(self, val):
        '''设置控件值'''
        try:
            self.find_element('input[name="'+self.comp_name+'"][value="'+val+'"]').click()
        except Exception as ex:
            print('设置单选框值异常%s' % ex)
    

class RadioPage(FormPage,SuperRadioPage):
    '''单选框控件'''

    def __init__(self, driver, comp_name):
        '''类初始化执行'''
        self.driver = driver
        self.comp_name = comp_name
        self.elements = self.get_components()

    def verticallayout_test(self):
        """单选框布局设置;"""
        aa = self.find_elem('span[name="' + self.comp_name + '"]>br')
        return aa

    def notnull_test(self):
        '''触发保存、获取提醒消息并返回'''
        btn = ButtonPage(self.driver)
        btn.click_button(btn.save)
        btn.wait_loading_hide()
        #time.sleep(0.1)
        return self.get_msg()

class RadioPhonePage(FormPhonePage,SuperRadioPage):
    '''手机端单选框控件'''

    def __init__(self, driver, comp_name):
        '''类初始化执行'''
        self.driver = driver
        self.comp_name = comp_name
        self.elements = self.get_components()

    def hide_test(self):
        """单选按钮条件隐藏"""
        try:
            self.get_components()
            return False
        except:
            return True





