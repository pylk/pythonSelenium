import time
import sys
sys.path.append('../../../')
from test_case.page_obj.view.queryform_page import QueryFormPage
from test_case.page_obj.button_page import ButtonPage
from test_case.page_obj.form.input_page import InputPage


class QueryFormGanttViewPage(QueryFormPage):
    '''查询表单-甘特视图'''

    def single_input(self):
        '''单行文本框查询'''
        ip = InputPage(self.driver, '单行文本框')
        self.view_scroll_to('0')
        ip.element.send_keys('任务2')
        self.view_scroll_to('400')
        #time.sleep(0.5)
        self.find_elem('#searchFormTable .btn-primary').click()
        self.wait_query_fload()  # 等待查询头折叠
        self.wait_loading_hide() # 等待loading消失
        #time.sleep(0.5)
        gv = self.find_elem('.leftPanel div.label')
        return gv.text == '任务2'

    def multiline_textbox(self):
        '''多行文本框查询'''
        qp = QueryFormPage(self.driver)
        qp.multiline_textbox_inputquery('60',1)
        self.wait_loading_hide()  # 等待loading消失
        gv = qp.find_elem('.leftPanel div.label')
        return gv.text == '任务2'

    def multiline_textbox_reset(self):
        '''多行文本框重置设置'''
        qp = QueryFormPage(self.driver)
        qp.multiline_textbox_reset_inputquery('60',1) #多行文本框重置输入查询
        self.wait_loading_hide()  # 等待loading消失
        gv = qp.find_elem('.leftPanel div.label')
        return gv.text == '任务'

    def radio(self):
        '''单选框查询'''
        qp = QueryFormPage(self.driver)
        qp.radio_selectquery(1)
        self.wait_loading_hide()  # 等待loading消失
        gv = qp.find_elem('.leftPanel div.label')
        return gv.text == '任务2'

    def multiselect(self):
        '''多选框查询'''
        qp = QueryFormPage(self.driver)
        qp.multiselect_selectquery(1)
        self.wait_loading_hide()  # 等待loading消失
        gv = qp.find_elem('.leftPanel div.label')
        return gv.text == '任务2'

    def drop_down(self):
        '''下拉框查询'''  
        qp = QueryFormPage(self.driver)
        qp.drop_down_selectquery(1)
        self.wait_loading_hide()  # 等待loading消失
        gv = qp.find_elem('.leftPanel div.label')
        return gv.text == '任务2'

    def date_selection(self):
        '''日期选择框查询'''
        qp = QueryFormPage(self.driver)
        qp.date_selection_selectquery('2017-07-01',1)
        self.wait_loading_hide()  # 等待loading消失
        gv = qp.find_elem('.leftPanel div.label')
        return gv.text == '任务2'

    def department_selection(self):
        '''部门选择框查询'''
        qp = QueryFormPage(self.driver)
        qp.department_selection_selectquery(1)
        self.wait_loading_hide()  # 等待loading消失
        gv = qp.find_elem('.leftPanel div.label')
        return gv.text == '任务2'

    def tree_department_selection(self):
        '''树形部门选择框查询'''
        qp = QueryFormPage(self.driver)
        qp.tree_department_selection_selectquery(1)
        self.wait_loading_hide()  # 等待loading消失
        gv = qp.find_elem('.leftPanel div.label')
        return gv.text == '任务2'

    def user_selection(self):
        '''用户选择框查询'''
        qp = QueryFormPage(self.driver)
        qp.user_selection_selectquery(1)
        self.wait_loading_hide()  # 等待loading消失
        gv = qp.find_elem('.leftPanel div.label')
        return gv.text == '任务2'

    def left_right_selection(self):
        '''左右选择框查询'''
        qp = QueryFormPage(self.driver)
        qp.left_right_selection_selectquery(1)
        self.wait_loading_hide()  # 等待loading消失
        gv = qp.find_elem('.leftPanel div.label')
        return gv.text == '任务2'

    def smart_alert(self):
        '''智能提示选择框查询'''
        qp = QueryFormPage(self.driver)
        qp.smart_alert_selectquery(1)
        self.wait_loading_hide()  # 等待loading消失
        gv = qp.find_elem('.leftPanel div.label')
        return gv.text == '任务2'
