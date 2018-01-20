import os,sys
sys.path.append('../../../')
import re
import time
from test_case.page_obj.view.queryform_page  import QueryFormPage
from test_case.page_obj.form.input_page import InputPage

class QueryFormTreeViewPage(QueryFormPage):
    '''查询表单-树形视图'''
    
    def switch_to_right_iframe(self):
        '''切换到右侧的iframe页面'''
        iframeMenu = self.find_elem("#viewFrame")
        try:
            self.driver.switch_to.frame(iframeMenu)
        except Exception as ex:
            print('获取iframe异常：%s' %ex)
        #time.sleep(0.5)

    def switch_to_div_iframe(self):
        self.switch_to_parent()
        div_iframe = self.find_elem('div.aui_content > iframe')
        self.driver.switch_to.frame(div_iframe)
        try:
            body_iframe = self.find_elem('body > iframe')
            if body_iframe!=None:
                self.driver.switch_to.frame(body_iframe)
        except Exception as ex:
            print('打开弹出层内的iframe异常：%s' % ex)

    def view_scroll_to(self, y):
        '''列表和日历视图滚动条定位'''
        script = 'var $con = $("body");if($con.size()>0)$con.getNiceScroll(0).doScrollTop('+y+',10)' #滚动到控件可以看到后面的代码执行才不会报错
        self.driver.execute_script(script)
        #time.sleep(0.5)

    def judge_search_content_inlist(self,list,content):
        '''判断输入内容搜索后是否成功'''
        for li in list:
            #正则表达式的模糊查询，匹配部分或全部 需要import re
            if re.search(content,li.text):
                continue
            else:
                return False    # 期望是返回False

    def single_input(self):
        '''单行文本框查询'''
        ip = InputPage(self.driver, '单行文本框')
        ip.element.send_keys('')
        self.find_elem('.comSearchBtn').click() # 点击查询按钮
        self.wait_loading_hide()
        #time.sleep(0.5)
        sis = self.find_elems('#dataTable .listDataTr td:nth-child(2)')
        return self.judge_search_content_inlist(sis,'')

    def multiline_textbox(self):
        '''多行文本框查询'''
        qp = QueryFormPage(self.driver)
        qp.multiline_textbox_inputquery('eee',2)
        self.wait_loading_hide()
        mts = qp.find_elems('#dataTable .listDataTr td:nth-child(3)')
        return self.judge_search_content_inlist(mts, 'eee')

    def multiline_textbox_reset(self):
        '''多行文本框重置设置'''
        qp = QueryFormPage(self.driver)
        qp.multiline_textbox_reset_inputquery('eee',2)
        self.wait_loading_hide()
        mts = qp.find_elems('#dataTable .listDataTr td:nth-child(3)')
        x = []
        for mt in mts:
            x.append(mt.text)
        return 'bbb' in x

    def radio(self):
        '''单选框查询'''
        qp = QueryFormPage(self.driver)
        qp.radio_selectquery(2)
        self.wait_loading_hide()
        rds = qp.find_elems('#dataTable .listDataTr td:nth-child(4)')
        return self.judge_search_content_inlist(rds, '男')

    def multiselect(self):
        '''多选框查询'''
        qp = QueryFormPage(self.driver)
        qp.multiselect_selectquery(2)
        self.wait_loading_hide()
        ms = qp.find_elems('#dataTable .listDataTr td:nth-child(5)')
        return self.judge_search_content_inlist(ms, '苹果')

    def drop_down(self):
        '''下拉框查询'''
        qp = QueryFormPage(self.driver)
        qp.drop_down_selectquery(2)
        self.wait_loading_hide()
        dd = qp.find_elems('#dataTable .listDataTr td:nth-child(6)')
        return self.judge_search_content_inlist(dd, '广州')

    def date_selection(self):
        '''日期选择框查询'''  
        qp = QueryFormPage(self.driver)
        qp.date_selection_selectquery('2018-02-04',2)
        self.wait_loading_hide()
        ds = qp.find_elems('#dataTable .listDataTr td:nth-child(7)')
        return self.judge_search_content_inlist(ds, '2018-02-04')

    def department_selection(self):
        '''部门选择框查询'''
        qp = QueryFormPage(self.driver)
        qp.department_selection_selectquery(2)
        self.wait_loading_hide()
        ds = qp.find_elems('#dataTable .listDataTr td:nth-child(8)')
        return self.judge_search_content_inlist(ds, '产品部')

    def tree_department_selection(self):
        '''树形部门选择框查询'''
        qp = QueryFormPage(self.driver)
        qp.open_fold_query(2) #点击高级查询
        qp.find_elem_visible('.btn-default[title="请选择"]').click() #点击添加树形部门按钮
        self.switch_to_div_iframe()
        #time.sleep(0.5)
        qp.find_elem_visible('.wtree-dept >div > .wtree-adron').click() #点击展开顶级部门
        qp.find_elem_visible('#deplist li li:nth-child(2) input').click() #点击勾选第二个部门
        qp.find_elem_visible('#btn-save').click()
        qp.wait_elem_disappear('#btn-save')
        self.switch_to_parent()
        self.switch_to_iframe()
        self.switch_to_right_iframe()
        self.view_scroll_to('400')
        #time.sleep(0.5)
        qp.find_elem_visible('#searchFormTable .btn-primary').click()
        self.wait_loading_hide()
        ds = qp.find_elems('#dataTable .listDataTr td:nth-child(9)')
        return self.judge_search_content_inlist(ds, '产品部')

    def user_selection(self):
        '''用户选择框查询'''
        qp = QueryFormPage(self.driver)
        qp.open_fold_query(2)
        qp.find_elem_is_clickable('#searchFormTable tr:nth-child(5)>td:nth-child(2)>span>span').click()
        self.switch_to_div_iframe()
        #time.sleep(0.5)
        qp.find_elem_visible('div.list_div[title="员工"]').click()
        #time.sleep(0.5)
        qp.find_elem_is_clickable('.list_div_click').click()
        #time.sleep(0.5)
        qp.find_elem_visible('#doReturn').click()
        #time.sleep(0.5)
        self.switch_to_parent()
        self.switch_to_iframe()
        self.switch_to_right_iframe()
        #time.sleep(0.5)
        self.view_scroll_to('400')
        qp.find_elem_visible('#searchFormTable .btn-primary').click()
        self.wait_loading_hide()
        #time.sleep(0.5)
        us = qp.find_elems('#dataTable .listDataTr td:nth-child(10)')
        return self.judge_search_content_inlist(us, '李玲')

    def left_right_selection(self):
        '''左右选择框查询'''
        qp = QueryFormPage(self.driver)
        qp.left_right_selection_selectquery(2)
        self.wait_loading_hide()
        lrs = qp.find_elems('#dataTable .listDataTr td:nth-child(11)')
        return self.judge_search_content_inlist(lrs, '广州')

    def smart_alert(self):
        '''智能提示选择框查询'''
        qp = QueryFormPage(self.driver)
        qp.smart_alert_selectquery(2)
        self.wait_loading_hide()
        sa = qp.find_elems('#dataTable .listDataTr td:nth-child(12)')
        return self.judge_search_content_inlist(sa,'aa')