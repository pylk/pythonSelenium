import sys
sys.path.append('../../../')
import time
from test_case.page_obj.view.queryform_page  import QueryFormPage
from test_case.page_obj.form.input_page import InputPage
from test_case.page_obj.button_page import ButtonPage
from test_case.page_obj.form.radio_page import RadioPage


class QueryFormCalendarViewPage(QueryFormPage):
    '''查询表单-日历视图'''

    def switch_calender(self):
        '''切换页面'''
        now = self.find_elem('a.eventTitle').text
        # 截取第一位到第四位的字符
        if int(now[0:4]) > 2017:
            ycount = int(now[0:4]) - 2017
            i = 0
            while (ycount > i):
                self.find_elem('a.btn-green[title = 上一年]').click()
                self.wait_loading_hide()
                i = i + 1
        elif int(now[0:4]) < 2017:
            ycount = 2017 - int(now[0:4])
            i = 0
            while (ycount > i):
                self.find_elem('a.btn-green[title = 下一年]').click()
                self.wait_loading_hide()
                i = i + 1
        if '-' in now[-2]:
            if int(now[-1]) > 7:
                mcount = int(now[-1]) - 7
                i = 0
                while (mcount > i):
                    self.find_elem('a.btn-green[title = 上一月]').click()
                    self.wait_loading_hide()
                    i = i + 1
            if int(now[-1]) < 7:
                mcount = 7 - int(now[-1])
                i = 0
                while (mcount > i):
                    self.find_elem('a.btn-green[title = 下一月]').click()
                    self.wait_loading_hide()
                    i = i + 1
        else:
            mcount = int(now[-2]) - 7
            i = 0
            while (mcount > i):
                self.find_elem('a.btn-green[title = 上一月]').click()
                self.wait_loading_hide()
                i = i + 1

    def is_the_date(self):
        '''判断日期是否正确'''
        if self.find_elem('a.eventTitle').text != '2017-7':
            self.switch_calender()

    def single_input(self):
        '''单行文本框查询'''
        ip = InputPage(self.driver, '单行文本框')
        ip.element.send_keys('test4')
        self.view_scroll_to('400')
        #time.sleep(0.5)
        self.find_elem('#searchFormTable .btn-primary').click()
        self.wait_query_fload()  # 等待查询头折叠
        #time.sleep(0.5)
        self.wait_loading_hide()
        dv = self.find_elem('#cal14')
        return dv.text == '14'

    def multiline_textbox(self):
        '''多行文本框查询'''
        qp = QueryFormPage(self.driver)
        qp.multiline_textbox_inputquery('test4',1)
        self.wait_loading_hide()
        dv = qp.find_elem('#cal14')
        return dv.text == '14'

    def multiline_textbox_reset(self):
        '''多行文本框重置设置'''
        qp = QueryFormPage(self.driver)
        qp.multiline_textbox_reset_inputquery('test4',1)
        self.wait_loading_hide()
        gv = qp.find_elem('#cal14')
        return 'test1' in gv.text

    def radio(self):
        '''单选框查询'''
        qp = QueryFormPage(self.driver)
        qp.radio_selectquery(1)
        self.wait_loading_hide()
        dv = qp.find_elem('#cal14')
        return dv.text == '14'

    def multiselect(self):
        '''多选框查询'''
        qp = QueryFormPage(self.driver)
        qp.multiselect_selectquery(1)
        self.wait_loading_hide()
        dv = qp.find_elem('#cal14')
        return dv.text == '14'

    def drop_down(self):
        '''下拉框查询'''
        qp = QueryFormPage(self.driver)
        qp.drop_down_selectquery(1)
        self.wait_loading_hide()
        dv = qp.find_elem('#cal14')
        return dv.text == '14'

    def date_selection(self):
        '''日期选择框查询'''
        qp = QueryFormPage(self.driver)
        qp.date_selection_selectquery('2017-07-10',1)
        self.wait_loading_hide()
        dv = qp.find_elem('#cal14')
        return dv.text == '14'

    def department_selection(self):
        '''部门选择框查询'''
        qp = QueryFormPage(self.driver)
        qp.department_selection_selectquery(1)
        self.wait_loading_hide()
        dv = qp.find_elem('#cal14')
        return dv.text == '14'

    def tree_department_selection(self):
        '''树形部门选择框查询'''
        qp = QueryFormPage(self.driver)
        qp.tree_department_selection_selectquery(1)
        self.wait_loading_hide()
        dv = qp.find_elem('#cal14')
        return dv.text == '14'

    def user_selection(self):
        '''用户选择框查询'''
        qp = QueryFormPage(self.driver)
        qp.user_selection_selectquery(1)
        self.wait_loading_hide()
        dv = qp.find_elem('#cal14')
        return dv.text == '14'

    def left_right_selection(self):
        '''左右选择框查询'''
        qp = QueryFormPage(self.driver)
        qp.left_right_selection_selectquery(1)
        self.wait_loading_hide()
        dv = qp.find_elem('#cal14')
        return dv.text == '14'

    def smart_alert(self):
        '''智能提示选择框查询'''
        qp = QueryFormPage(self.driver)
        qp.smart_alert_selectquery(1)
        self.wait_loading_hide()
        dv = qp.find_elem('#cal10')
        return dv.text == '10'



