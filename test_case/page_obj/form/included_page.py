import os,sys
sys.path.append('../../../')
import time
from test_case.page_obj.form.form_page import FormPage
from test_case.page_obj.form.form_page import FormPhonePage
from test_case.page_obj.button_page import ButtonPhonePage
from test_case.page_obj.form.input_page import InputPhonePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class IncludedSuperPage(object):
    '''包含元素公共方法'''

class IncludedPhonePage(FormPhonePage):
    """手机端包含元素"""
    comp_name = ''
    driver = ''
    element = ''

    def __init__(self, driver, comp_name):
        '''类初始化执行'''
        self.driver = driver
        self.comp_name = comp_name
        self.element = self.get_component()

    def get_component(self):
        '''根据名称获取包含元素控件'''
        print('获取测试控件：%s' % self.comp_name)
        try:
            locator = '[getname="' + self.comp_name + '"]'
            elem = self.find_elem(locator)
            self.scroll_to_target_element(elem)
            return elem
        except Exception as ex:
            print('获取控件异常：%s' % ex)
            return 'none'

    def is_comp_hide(self,name):
        '''判断包含元素控件是否可见'''
        try:
            WebDriverWait(self.driver, timeout=2).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, 'a[getname="'+name+'"]')))
            return True
        except:
            return False

    def is_comp_readonly(self,compname):
        '''判断树形部门选择框控件是否只读'''
        try:
            WebDriverWait(self.driver,timeout=3).until(EC.element_to_be_clickable((By.CSS_SELECTOR,  'a[getname="'+compname+'"]')))
            return False
        except:
            return True


    def getrecord(self,name):
        '''根据控件名获取包含元素的总记录数'''
        text = self.find_elem('a[getname="'+name+'"]>div.weui-cell__ft>span').text
        return text

    def is_contentIsNull(self):
        '''判断包含元素内容是否为空'''
        return self.is_element_visible('.contentIsNull')

    def click_included_btn(self,name):
        '''点击包含元素按钮'''
        self.find_elem('a[getname="'+name+'"]').click()
        self.wait_Tabloading_show_then_hide()
        self.wait_elem_show_then_hide('.weui_mask_transparent')

    def get_curpage_included_num(self):
        '''包含获取当前页的记录数'''
        return len(self.find_elements('.listDataTrFirstTd'))

    def set_value(self,incluedename,inputname1,input1val,inputname2,input2val):
        '''新建一条记录'''
        btn = ButtonPhonePage(self.driver)
        self.click_included_btn(incluedename)
        btn.click_button('新建')
        inputtext = InputPhonePage(self.driver, inputname1)
        inputtext.send_keys_get_value(input1val)
        inputtext = InputPhonePage(self.driver, inputname2)
        inputtext.send_keys_get_value(input2val)
        btn.click_button('保存')
        self.wait_msg_show_then_hide()
        btn.click_button('返回')
        self.wait_Tabloading_show_then_hide()
        self.driver.back()
        self.wait_elem_show_then_hide('.weui_mask_transparent')

    def clera_value(self):
        '''恢复包含元素数据'''
        btn = ButtonPhonePage(self.driver)
        self.click_included_btn('包含元素_非父子关系')
        lis = self.find_elements('input[name="_selects"]')
        num = 0
        if len(lis)>=7:
            for li in lis:
                num+=1
                if num>=7:
                    li.click()
            btn.click_button('删除')
            self.accept_alert() #接受警告框
            self.driver.back()
            self.wait_elem_show_then_hide('.weui_mask_transparent')
        else:
            self.driver.back()
            self.wait_elem_show_then_hide('.weui_mask_transparent')










class IncludedPage(FormPage):
    """包含元素"""
    driver = ''


    def getrecord(self,name):
        '''根据控件名获取包含元素的总记录数'''
        text = self.find_elem('div[getname="' + name + '"]  div.input-group+span').text
        return text

    def clicknew(self,name):
        '''根据控件名点击新建按钮'''
        self.find_elem('div[getname="' + name + '"] a:nth-child(1)').click()

    def clickdeleete(self,name):
        '''根据控件名点击删除按钮'''
        self.find_elem('div[getname="' + name + '"] a:nth-child(2)').click()

    def switch_grid(self,name):
        iframe = self.find_elem('iframe[getname="' + name + '"]')
        self.driver.switch_to.frame(iframe)

    def clicknewgrid(self, name):
        '''根据控件名点击网格新建按钮'''
        self.find_elem('div.activity__bd a:nth-child(1)').click()

    def clickdeleetegrid(self, name):
        '''根据控件名点击网格删除按钮'''
        self.find_elem('div.activity__bd a:nth-child(2)').click()

    def clicksavegrid(self,name):
        '''根据控件名点击网格保存按钮'''
        self.find_elem('div.activity__bd a:nth-child(3)').click()

    def clickcancelgrid(self, name):
        '''根据控件名点击网格取消所有按钮'''
        self.find_elem('div.activity__bd a:nth-child(4)').click()


    def is_included_existed(self,name):
        """根据控件名判断包含元素控件是否存在，存在返回Ture,不存在返回False"""
        return self.is_element_visible('div[getname="' + name + '"]')

    def successnew(self,name):
        '''判断是否新建记录成功'''
        try:
            self.find_elem('div[getname="' + name + '"]  tr.listDataTh + tr')
            return True
        except Exception as e:
            return False
        finally:
            ###清除数据，保持干净
            self.find_elem('div[getname="' + name + '"]  td.listDataThFirstTd > input[type="checkbox"]').click()
            #time.sleep(0.5)
            self.find_elem('div[getname="' + name + '"] a:nth-child(2)').click()
            self.driver.switch_to_alert().accept()

    def successnewgrid(self, name):
        '''判断网格视图是否新建记录成功'''
        try:
            self.find_elem('div.gridView__bd div.obpm-view__table-bd tr')
            return True
        except Exception as e:
            return False
        finally:
            ###清除数据，保持干净
            time.sleep(0.1) #必须，等待重绘
            self.find_elem('div.gridView__bd  input.obpm-check:nth-child(1)').click()
            #time.sleep(0.5)
            self.find_elem('div.activity__bd a:nth-child(2)').click()
            self.driver.switch_to_alert().accept()



