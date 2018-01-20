import sys
sys.path.append('../../../')
from test_case.page_obj.page import PhonePage

class FlowSubmitPanelPage(PhonePage):
    '''流程提交面板'''

    def click_usefulopinions(self):
        '''展开/收起常用意见'''
        self.find_element_is_clickable('.weui-cell_access .pull-right').click()

    def select_usefulopinions(self,name):
        '''选择意见'''
        lis = self.find_elements('.flow-submit__proposal-box .weui-cell_access')
        for li in lis:
            if li.text == name:
                li.click()
                break
            else:
                print('no such element')

    def get_usefulopinions(self):
        '''获取意见框中的值'''
#         text = self.find_elem('textarea[name="_attitude"]').get_attribute('value')
        return self.find_elem('.weui-textarea').get_attribute('value')
#         return text