import os,sys
sys.path.append('../../../')
from test_case.page_obj.form.form_page import FormPage
from test_case.page_obj.form.form_page import FormPhonePage


class CalculatePage(FormPage):
    '''计算脚本控件'''
    
    def has_the_text(self, text):
        calctexts = self.find_elems('span.calctext-field')
        for calctext in calctexts:
            if calctext.text == text:
                return True
        
        return False


class CalculatePhonePage(FormPhonePage):
    '''手机端计算脚本控件'''


    
