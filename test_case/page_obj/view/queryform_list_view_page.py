import re
import time

from test_case.page_obj.view.queryform_page  import QueryFormPage
from test_case.page_obj.form.input_page import InputPage
from test_case.page_obj.form.input_page import InputPhonePage
from test_case.page_obj.button_page import ButtonPhonePage
from test_case.page_obj.page import PhonePage


class SuperQueryFormPage(object):
    
    def judge_search_content_inlist(self,list,content):
        '''判断输入内容搜索后是否成功'''
        for li in list:
            #正则表达式的模糊查询，匹配部分或全部 需要import re
            if re.search(content,li.text):
                continue
            else:
                return False    # 期望是返回False


    '''
    @param list: 查找的列表
    @param text: 被查找的内容
    return: 成功时返回True，失败时返回False
    '''
    def judge_search_text_inlist(self,list,text):
        '''判断输入内容搜索后是否成功'''
        x = []
        for li in list:
            #正则表达式的模糊查询，匹配部分或全部 需要import re
            if re.search(text,li.text):
                x.append(True)
            else:
                x.append(False)
        a = False
        return (not (a in x))


class QueryFormListViewPage(QueryFormPage, SuperQueryFormPage):
    '''查询表单-列表视图'''

    def single_input(self):
        '''单行文本框查询'''
        ip = InputPage(self.driver, '单行文本框')
        ip.element.send_keys('test1')   # 输入文本
        self.find_elem('.comSearchBtn').click() # 点击查询按钮
        self.wait_query_fload()  # 等待查询头折叠
        self.wait_loading_hide() # 等待视图的loading消失
        sis = self.find_elems('#dataTable .listDataTr td:nth-child(2)') # 获取搜索后的单行文本列值
        return self.judge_search_content_inlist(sis,'test1')

    def multiline_textbox(self):
        '''多行文本框查询'''   
        qp = QueryFormPage(self.driver)
        qp.multiline_textbox_inputquery('test1',2)
        self.wait_loading_hide()  # 等待视图的loading消失
        mts = qp.find_elems('#dataTable .listDataTr td:nth-child(3)')
        return self.judge_search_content_inlist(mts, 'test1')

    def multiline_textbox_reset(self):
        '''多行文本框重置设置'''
        qp = QueryFormPage(self.driver)
        qp.multiline_textbox_reset_inputquery('test1',2)
        self.wait_loading_hide()  # 等待视图的loading消失
        mts = qp.find_elems('#dataTable .listDataTr td:nth-child(3)')
        x = []
        for mt in mts:
            x.append(mt.text)
        return 'test2test2' in x

    def radio(self):
        '''单选框查询'''
        qp = QueryFormPage(self.driver)
        qp.radio_selectquery(2)
        self.wait_loading_hide()  # 等待视图的loading消失
        rds = qp.find_elems('#dataTable .listDataTr td:nth-child(4)')
        return self.judge_search_content_inlist(rds, '男')

    def multiselect(self):
        '''多选框查询'''
        qp = QueryFormPage(self.driver)
        qp.multiselect_selectquery(2)
        self.wait_loading_hide()  # 等待视图的loading消失
        ms = qp.find_elems('#dataTable .listDataTr td:nth-child(5)')
        return self.judge_search_content_inlist(ms, '苹果')

    def drop_down(self):
        '''下拉框查询'''
        qp = QueryFormPage(self.driver)
        qp.drop_down_selectquery(2)
        self.wait_loading_hide()  # 等待视图的loading消失
        dd = qp.find_elems('#dataTable .listDataTr td:nth-child(6)')
        return self.judge_search_content_inlist(dd, '广州')

    def date_selection(self):
        '''日期选择框查询'''  
        qp = QueryFormPage(self.driver)
        qp.date_selection_selectquery('2018-02-04',2)
        self.wait_loading_hide()  # 等待视图的loading消失
        ds = qp.find_elems('#dataTable .listDataTr td:nth-child(7)')
        return self.judge_search_content_inlist(ds, '2018-02-04')

    def department_selection(self):
        '''部门选择框查询'''
        qp = QueryFormPage(self.driver)
        qp.department_selection_selectquery(2)
        self.wait_loading_hide()  # 等待视图的loading消失
        ds = qp.find_elems('#dataTable .listDataTr td:nth-child(8)')
        return self.judge_search_content_inlist(ds, '产品部')

    def tree_department_selection(self):
        '''树形部门选择框查询'''
        qp = QueryFormPage(self.driver)
        qp.tree_department_selection_selectquery(2)
        self.wait_loading_hide()  # 等待视图的loading消失
        ds = qp.find_elems('#dataTable .listDataTr td:nth-child(9)')
        return self.judge_search_content_inlist(ds, '产品部')

    def user_selection(self):
        '''用户选择框查询'''
        qp = QueryFormPage(self.driver)
        qp.user_selection_selectquery(2)
        self.wait_loading_hide()  # 等待视图的loading消失
        us = qp.find_elems('#dataTable .listDataTr td:nth-child(10)')
        return self.judge_search_content_inlist(us, '李玲')

    def left_right_selection(self):
        '''左右选择框查询'''
        qp = QueryFormPage(self.driver)
        qp.left_right_selection_selectquery(2)
        self.wait_loading_hide()  # 等待视图的loading消失
        lrs = qp.find_elems('#dataTable .listDataTr td:nth-child(11)')
        return self.judge_search_content_inlist(lrs, '广州')

    def smart_alert(self):
        '''智能提示选择框查询'''
        qp = QueryFormPage(self.driver)
        qp.smart_alert_selectquery(2)
        self.wait_loading_hide()  # 等待视图的loading消失
        sa = qp.find_elems('#dataTable .listDataTr td:nth-child(12)')
        return self.judge_search_content_inlist(sa,'aa')
    

class QueryFormPhonePage(PhonePage, SuperQueryFormPage):
    '''手机端查询表单-视图'''

    def click_fold_query(self):
        '''点击打开查询表单'''
        bp = ButtonPhonePage(self.driver)
        bp.click_button('查询')

    def is_open_query_page(self):
        '''是否已打开查询表单'''
        return self.find_element('#_searchPanel').is_displayed()
        
    def click_close_query(self):
        '''关闭查询表单界面'''
        self.find_elem_is_clickable('#btn-modal-close').click()

    def click_search(self):
        '''点击查询表单界面的查询按钮'''
        self.find_element('#_searchPanel .btn-block[title="查询"]').click()

    def check_search_result(self, col_num, search_val):
        '''检查结果'''
        sis = self.find_elems('#listView .listDataTr td:nth-child('+col_num+')') # 获取搜索后的单行文本列值
        return self.judge_search_text_inlist(sis, search_val)

    def check_result_4_reset(self, col_num, example_val):
        '''重置后检查结果'''
        sis = self.find_elems('#listView .listDataTr td:nth-child('+col_num+')') # 获取搜索后的单行文本列值
        return self.judge_search_text_inlist_4_reset(sis, example_val)
        
    '''
    @param list: 查找的列表
    @param text: 被查找的内容
    return: 成功时返回True，失败时返回False
    '''
    def judge_search_text_inlist_4_reset(self,list,example_val):
        '''判断输入内容搜索后是否成功'''
        x = []
        for val in example_val:
            park = False
            for li in list:
                #正则表达式的模糊查询，匹配部分或全部 需要import re
                if re.search(val,li.text):  #匹配时在x数组中插入True并停止循环
                    park = True
                    break
            x.append(park) #无匹配时在x数组中插入False
        a = False
        return (not (a in x))   # 只要有一个False即有误
        
