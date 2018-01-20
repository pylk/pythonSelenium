import os,sys
sys.path.append('../../../')

from test_case.page_obj.form.form_page import FormPage
from test_case.page_obj.form.form_page import FormPhonePage


class SuperHtmlPage(object):
    
    def get_the_value(self):
        '''获取文本值'''
        try:
            if self.get_the_div_iframe()!=None:
                iframe = self.get_the_div_iframe()
                self.switch_to_the_iframe(iframe)
                body = self.find_elem('body')
                return body.text
            else:
                return ''
        except Exception as ex:
            print('html控件获取文本值异常：%s' %ex)
            return ''
    


class HtmlPage(FormPage, SuperHtmlPage):
    '''html控件'''
    
    def __init__(self, driver, comp_name):
        '''类初始化执行'''
        self.driver = driver
        self.comp_name = comp_name
    
    def get_the_div(self):
        '''获取the div'''
        return self.find_elem('#'+self.comp_name+'_id')

        
    def get_the_div_iframe(self):
        '''获取the div下的隐藏元素'''
        if self.get_the_div()!=None:
            the_div = self.get_the_div()
            return the_div.find_element_by_css_selector('div.edui-editor-iframeholder > iframe')
        else:
            return None
    
    def get_the_div_width(self):
        '''获取编辑器宽度'''
        if self.get_the_div()!=None:
            the_div = self.get_the_div()
            return the_div.size['width']
        else:
            return ''
    
    def get_the_div_height(self):
        '''获取编辑器宽度'''
        if self.get_the_div()!=None:
            the_div = self.get_the_div()
            iframe_div = the_div.find_element_by_css_selector('.edui-editor-iframeholder')
            return iframe_div.size['height']
        else:
            return ''
    
    def get_the_div_width_percent(self):
        '''获取编辑器宽度(百分比)'''
        if self.get_the_div()!=None:
            the_div = self.get_the_div()
            return the_div.find_element_by_css_selector('div.edui-editor.edui-default').get_attribute('style')
        else:
            return ''
    
    def get_readonly_div_text(self):
        '''获取只读内容'''
        try:
            if self.find_elem('textarea[name="'+self.comp_name+'"]')!=None:
                com = self.find_elem('textarea[name="'+self.comp_name+'"]')
                div = com.find_element_by_xpath('../div')
                if div:
                    return div.text
                else:
                    return ''
            else:
                return ''
        except Exception as ex:
            print('html编辑器获取只读内容异常：%s' %ex)
            return ''
        
    def is_displayed(self):
        return self.find_elem('textarea[name="'+self.comp_name+'"]').is_displayed()


class HtmlPhonePage(FormPhonePage, SuperHtmlPage):
    '''手机端html控件'''
    
    def __init__(self, driver, comp_name):
        '''类初始化执行'''
        self.driver = driver
        self.comp_name = comp_name
        
    def get_attr(self, name):
        '''根据属性名获取控件属性值'''
        return self.find_element('textarea[name="'+self.comp_name+'"]').get_attribute(name)

    def get_the_div_iframe(self):
        '''获取iframe控件'''
        return self.find_element('textarea[name="'+self.comp_name+'"] + .formfield-wrap div[name="'+self.comp_name+'"] iframe.html-edit-panel')
        
    def check_dom(self):
        '''检查文档结构'''
        return self.find_element('textarea[name="'+self.comp_name+'"] + .formfield-wrap div[name="'+self.comp_name+'"] iframe.html-edit-panel')
    
    def is_displayed(self):
        '''html控件是否可见'''
        return self.get_the_div_iframe().is_displayed()
    
    def get_readonly_div_text(self):
        '''获取只读内容'''
        return self.find_element('textarea[name="'+self.comp_name+'"] + div.formfield-wrap div.html-edit').text
        
    