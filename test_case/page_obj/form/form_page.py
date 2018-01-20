import time
import os
import sys
import string
sys.path.append('../../../')

from test_case.page_obj.page import Page
from test_case.page_obj.page import PhonePage
from test_case.page_obj.button_page import ButtonPage
from test_case.page_obj.button_page import ButtonPhonePage



class SuperFormPage(object):
    """FormPage和FormPhonePage的基类"""

    def get_components(self):
        '''根据名称获取控件'''
        print('获取测试控件：%s' % self.comp_name)
        locator = '[name="' + self.comp_name + '"]'
        if self.find_elems(locator)!=None:
            elems = self.find_elems(locator)
            self.scroll_to_target_element(elems[0])
            return elems
        else:
            print('获取控件异常：%s')

    def get_component(self):
        '''根据名称获取控件'''
        print('获取测试控件：%s' % self.comp_name)
        locator = '[name="' + self.comp_name + '"]'
        elem = self.find_elem(locator)
        if elem!=None:
            self.scroll_to_target_element(elem)
            return elem
        else:
            return None


    def get_file_path(self,filename):
        #输入文件名-返回data文件夹下的testfile目录的文件的路径
        num = 0
        path = ''
        aLists = os.getcwd ().split ('\\') #获取当前文件的路径，并且把它弄成列表
        print (aLists)
        if 'test_case' in aLists:
            for aList in aLists:
                num += 1
                if aList == "test_case":
                    for i in range (0, num-1):
                        path = path + aLists[i] + '/'
        if 'test_case' not in aLists:
            for aList in aLists:
                    path = path + aList + '/'
        filedir = path + 'data/test_files/'+filename
        print ('11111'+filedir)
        return filedir


    def get_listelement_attr(self,attribute_name):
        '''根据属性名获取元素集的每一个元素属性，用于单选，复选等控件'''
        elements_attr_list = []
        elements = self.get_components()
        for element in elements:
            elements_attr_list.append(element.get_attribute(attribute_name))
        return elements_attr_list

    def elements_attr_test(self,attr_name,attr_val):
        '''判断一组元素的attr_name属性值是否为attr_val'''
        test_elements_attr_list = []
        for long in self.get_components():
            test_elements_attr_list.append(attr_val)
        elements_attr_list = self.get_listelement_attr(attr_name)
        if test_elements_attr_list == elements_attr_list:
            return True
        else:
            return False

    def readonly_test(self):
        '''控件只读（显示和条件）'''
        readonly = self.get_attr('readonly')
        disabled = self.get_attr('disabled')
        return readonly == 'true' or disabled == 'true'



class FormPage(Page,SuperFormPage):
    '''表单界面测试'''
    
    def get_nextids(self):
        '''获取提交节点'''
        try:
            nexts = self.driver.find_elements_by_name('_nextids')
            return len(nexts)
        except Exception as ex:
            print('获取提交节点异常：%s' %ex)
            return 0
    
    def get_style_lib(self):
        '''返回样式库内容'''
        styles = self.find_elems('style')
        for iter in styles:
            return iter.get_attribute('innerText')
    
    def is_show_watermark(self):
        '''是否显示水印'''
        try:
            image = self.find_elem('body').value_of_css_property('background-image')
            return(image != 'none')
        except Exception as ex:
            return False
    
    def open_and_switch_to_print_page(self):
        '''打开并切换到打印页面'''
        bp = ButtonPage(self.driver)
        bp.click_button(bp.form_page_print)
        #time.sleep(0.1)
        self.switch_to_another_window()

    def get_tag_name(self):
        '''PC端获取单行、多行文本框等的标签名'''
        return  self.find_elem('tbody .form-control ').tag_name

    def get_curpage_span(self):
        '''获取当前页面所有span的text'''
        textlist = []
        lis = self.find_elems('span')
        for li in lis:
            text = li.text
            if text !='':
                textlist.append(text)
        return textlist


class FormPhonePage (PhonePage,SuperFormPage):
    '''手机端表单界面测试'''

    def get_curpage_span(self):
        '''获取当前页面所有span的text'''
        return  self.find_element('span').text

    def get_nextids(self):
        '''获取提交节点'''
        try:
            nexts = self.driver.find_elements_by_name ('_nextids')
            return len (nexts)
        except Exception as ex:
            print ('获取提交节点异常：%s' % ex)
            return 0

    def get_style_lib(self):
        '''返回样式库内容'''
        styles = self.find_elems ('style')
        for iter in styles:
            return iter.get_attribute ('innerText')

    def get_tag_name(self):
        '''手机端获取单行、多行文本框等的标签名'''
        return  self.find_element('.contactField.requiredField').tag_name

    def is_desription_effect(self,compname):
        '''判断描述是否生效'''
        # 获取所有label值，判断是否存在传入的名称的lable
        elem = self.find_element('[name="'+compname+'"]')
        discript = elem.get_attribute('discript')
        dps = self.find_elements('div.formfield-wrap>label')
        for dp in dps:
            if dp.text == discript:
                # 判断label的text是否与discript属性相等
                return True
        return False

    def notnull_test(self):
        '''判断非空'''
        bt = ButtonPhonePage(self.driver)
        bt.click_button('保存')
        pp = PhonePage(self.driver)
        return pp.get_msg()

    def switch_to_phone_iframe(self):
        # 切到iframe 手机端
        self.driver.switch_to.default_content()
        div_iframe = self.find_elem('div.content>iframe')
        self.driver.switch_to.frame(div_iframe)


