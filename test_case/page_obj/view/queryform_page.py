import time

from test_case.page_obj.page  import Page
from test_case.page_obj.form.input_page import InputPage
from test_case.page_obj.form.radio_page import RadioPage

class QueryFormPage(Page):
    '''查询表单'''

    def switch_to_parent(self):
        print('切换回父iframe')
        self.driver.switch_to.default_content()

    def switch_to_div_iframe(self):
        self.switch_to_parent()
        div_iframe = self.find_elem('.aui_loading+iframe')
        self.driver.switch_to.frame(div_iframe)

    def view_scroll_to(self, y):
        '''列表和日历视图滚动条定位'''
        script = 'var $con = $("body");if($con.size()>0)$con.getNiceScroll(0).doScrollTop('+y+',10)' #滚动到控件可以看到后面的代码执行才不会报错
        self.driver.execute_script(script)
        time.sleep(0.5) #等待滚动完成

    def close_righttop_message(self):
        '''关闭右上角的消息提示'''
        try:
            message_close = self.find_elem('.message-popup-close')
            message_close.click()
        except Exception as ex:
            print('关闭右上角的消息提示异常:%s' %ex)

    def open_fold_query_icon(self):
        '''查询图标展开查询头'''
        self.find_elem('.btn.btn-info').click()

    def open_fold_query_high(self):
        '''查询 高级 展开折叠查询头'''
        self.find_elem('.search-senior').click()
        self.wait_elem_show_then_hide('.comSearchBtn')#等待查询按钮消失

    def open_fold_query(self,num):
        '''查询按钮方式选择'''
        if num == 1:
            self.open_fold_query_icon()
        elif num == 2:
            self.open_fold_query_high()
        self.wait_elem_visible('.container-fluid') #等待查询头完全展开

    def get_openfold_query_return(self):
        '''判断查询头折叠/展开'''
        oc = self.find_elem('#searchFormTable')
        return oc.value_of_css_property('display') == 'block'

    def is_open_query_form(self):
        '''判断查询头是否已经展开完全'''
        oc = self.find_elem('#searchFormTable')
        dis = oc.value_of_css_property('display')
        return dis == 'block'

    def wait_query_open(self):
        '''等待查询头展开'''
        for num in range(1, 20):
            if self.is_open_query_form():
                break
            time.sleep(0.1)

    def is_close_query_form(self):
        '''判断查询头是否已经折叠完全'''
        oc = self.find_elem('#searchFormTable')
        dis = oc.value_of_css_property('display')
        print('display------>oc-->' % dis)
        return dis == 'none'

    def wait_query_close(self):
        '''等待查询头折叠'''
        for num in range(1, 20):
            if self.is_close_query_form():
                break
            time.sleep(0.1)

    def wait_query_fload(self):
        '''等待查询头折叠'''
        if self.get_openfold_query_return() == True:
            self.wait_elem_disappear('#searchFormTable')

    def multiline_textbox_inputquery(self,contect,num):
        '''多行文本框输入查询'''
        self.open_fold_query(num)   # 点击展开查询
        #time.sleep(0.5)
        ip = InputPage(self.driver, '多行文本框')
        ip.element.send_keys(contect)   # 输入文本
        self.scroll_to_target_element(self.find_elem('#searchFormTable .btn-primary')) #滚到查询按钮位置
        self.hide_elem_by_jq('#activityTable')  # 隐藏按钮栏避免遮挡
        self.hide_elem_by_jq('#activityTable>.searchDiv')  # 隐藏按钮栏避免遮挡

        self.find_elem_visible('#searchFormTable .btn-primary').click() #点击查询按钮
        self.wait_query_fload()  # 等待查询头折叠

    def multiline_textbox_reset_inputquery(self,contect,num):
        '''多行文本框重置输入查询'''
        self.multiline_textbox_inputquery(contect,num)
        self.wait_loading_hide()  # 等待视图的loading消失
        self.open_fold_query(num)
        self.hide_elem_by_jq('#activityTable')  # 隐藏按钮栏避免遮挡
        self.hide_elem_by_jq('#activityTable>.searchDiv')  # 隐藏按钮栏避免遮挡
        self.scroll_to_target_element(self.find_elem('#searchFormTable .row'))  # 滚到查询按钮位置
        self.find_elem_visible('#searchFormTable .btn-reset').click()   # 点击重置按钮
        self.find_elem_visible('#searchFormTable .btn-primary').click() # 点击查询按钮
        self.wait_query_fload()  # 等待查询头折叠


    def radio_selectquery(self,num):
        '''单选框选择查询'''
        self.open_fold_query(num)
        #time.sleep(0.5)
        self.hide_elem_by_jq('#activityTable')  # 隐藏按钮栏避免遮挡
        self.hide_elem_by_jq('#activityTable>.searchDiv')  # 隐藏按钮栏避免遮挡
        rp = RadioPage(self.driver, '单选框')

        #self.view_scroll_to('0')  # 点击时要定位回顶部，避免被遮挡
        rp.elements[0].click()  # 单选点击
        #time.sleep(0.5)
        self.scroll_to_target_element(self.find_elem('#searchFormTable .row'))  # 滚到查询按钮位置

        self.find_elem('#searchFormTable .btn-primary').click() # 点击查询按钮
        self.wait_query_fload()  # 等待查询头折叠


    def multiselect_selectquery(self,num):
        '''多选选择查询'''
        self.open_fold_query(num)
        #time.sleep(0.5)
        self.find_elem_is_clickable('#searchFormTable input[text="苹果"]').click()  # 勾选桃子选择
        #time.sleep(0.5)
        self.scroll_to_target_element(self.find_elem('#searchFormTable .row'))  # 滚到查询按钮位置
        self.hide_elem_by_jq('#activityTable')  # 隐藏按钮栏避免遮挡
        self.hide_elem_by_jq('#activityTable>.searchDiv')  # 隐藏按钮栏避免遮挡

        #time.sleep(0.5)
        self.find_elem_visible('#searchFormTable .btn-primary').click() # 点击查询按钮
        self.wait_query_fload()  # 等待查询头折叠
        #time.sleep(0.5)

    def drop_down_selectquery(self,num):
        '''下拉选择框选择查询'''
        self.open_fold_query(num)
        cb = self.find_elem_is_clickable('select[name="下拉框"]')  # 点击展开下拉选项
        cb.click()
        cb.find_element_by_css_selector('option:nth-child(2)').click()  # 下拉选择
        #time.sleep(0.5)
        self.scroll_to_target_element(self.find_elem('#searchFormTable .row'))  # 滚到查询按钮位置
        self.hide_elem_by_jq('#activityTable')  # 隐藏按钮栏避免遮挡
        self.hide_elem_by_jq('#activityTable>.searchDiv')  # 隐藏按钮栏避免遮挡

        #time.sleep(0.5)
        self.find_elem('#searchFormTable .btn-primary').click()
        self.wait_query_fload()  # 等待查询头折叠
        #time.sleep(0.5)

    def date_selection_selectquery(self,date,num):
        '''日期选择框选择查询'''
        self.open_fold_query(num)
        #time.sleep(0.5)
        self.view_scroll_to('0')
        self.driver.find_element_by_name('日期选择框').send_keys(date)
        #time.sleep(0.5)
        self.scroll_to_target_element(self.find_elem('#searchFormTable .row'))  # 滚到查询按钮位置
        self.hide_elem_by_jq('#activityTable')  # 隐藏按钮栏避免遮挡
        self.hide_elem_by_jq('#activityTable>.searchDiv')  # 隐藏按钮栏避免遮挡

        self.find_elem('#searchFormTable .btn-primary').click()
        self.wait_query_fload()  # 等待查询头折叠
        #time.sleep(0.5)

    def department_selection_selectquery(self,num):
        '''部门选择框选择查询'''
        self.open_fold_query(num)
        #time.sleep(0.5)
        cb = self.driver.find_element_by_name('部门选择框')
        cb.click()
        cb.find_element_by_css_selector('option:nth-child(3)').click()
        #time.sleep(0.5)
        self.scroll_to_target_element(self.find_elem('#searchFormTable .row'))  # 滚到查询按钮位置
        self.hide_elem_by_jq('#activityTable') #隐藏按钮栏避免遮挡
        self.hide_elem_by_jq('#activityTable>.searchDiv')  # 隐藏按钮栏避免遮挡
        self.find_elem_visible('#searchFormTable .btn-primary').click()
        self.wait_query_fload()  # 等待查询头折叠


    def tree_department_selection_selectquery(self,num):
        '''树形部门选择框选择查询'''
        self.open_fold_query(num) #展开查询表单
        #time.sleep(0.5)
        self.find_elem_visible('#searchFormTable input[name="树形部门选择框"]+span[title="请选择"]').click() #点击树形部门添加按钮
        #time.sleep(0.5)
        self.switch_to_div_iframe()
        self.find_elem_visible('i.wtree-arrow').click() #点击顶级部门
        time.sleep(0.5)
        target = self.find_elem_visible('#deplist li[data-name="测试部"] input[type="checkbox"]')
        if(target==None):
            for i in range(10):
                print('点击顶级部门次数 %s' %i)
                self.find_elem_visible('i.wtree-arrow').click()  # 点击顶级部门
                target2 = self.find_elem_visible('#deplist li[data-name="测试部"] input[type="checkbox"]')
                if(target2!=None):
                    target2.click()
                    break
        else:
            target.click()
        self.find_elem_visible('#btn-save').click()
        self.wait_lock_screen_div_not_visible() #等待锁屏消失
        self.switch_to_parent()
        self.switch_to_iframe()
        self.view_scroll_to('400')
        #time.sleep(0.5)
        self.find_elem_visible('#searchFormTable .btn-primary').click()
        self.wait_query_fload()  # 等待查询头折叠

    def user_selection_selectquery(self,num):
        '''用户选择框选择查询'''
        self.open_fold_query(num)
        #time.sleep(0.5)
        self.find_elem_visible('#searchFormTable tr:nth-child(5)>td:nth-child(2)>span>span').click()
        #time.sleep(0.5)
        self.switch_to_div_iframe()
        self.find_elem_visible('div.list_div[title="员工"]').click()  #点击员工角色
        if(self.is_element_visible('#righttitle[title="员工"]')==False):
            for i in range(10):
                print('%s'%i)
                self.find_elem_visible('div.list_div[title="员工"]').click()  # 点击员工角色
                if(self.is_element_visible('#righttitle[title="员工"]')):
                    break
        self.find_elem_visible('#addAll').click() #点击添加本页所有
        self.wait_elem_visible('span[title="点击删除"]')
        self.find_elem_visible('#doReturn').click()
        self.switch_to_parent()
        self.wait_lock_screen_div_not_visible() #等待灰色锁屏消失
        self.switch_to_iframe()
        #time.sleep(0.5)
        self.view_scroll_to('400')
        self.wait_elem_visible('#searchFormTable .btn-primary')
        self.find_elem_visible('#searchFormTable .btn-primary').click()  #点击查询按钮
        self.wait_query_fload()  # 等待查询头折叠


    def left_right_selection_selectquery(self,num):
        '''左右选择框选择查询'''
        self.open_fold_query(num)
        lr = self.find_elem('#左右选择框ms2side__sx')
        lr.find_element_by_css_selector('option:nth-child(2)').click()
        self.find_elem('.AddOne').click()
        #time.sleep(0.5)
        self.scroll_to_target_element(self.find_elem('#searchFormTable .row'))  # 滚到查询按钮位置
        self.hide_elem_by_jq('#activityTable')  # 隐藏按钮栏避免遮挡
        self.hide_elem_by_jq('#activityTable>.searchDiv')  # 隐藏按钮栏避免遮挡

        self.find_elem_visible('#searchFormTable .btn-primary').click()
        self.wait_query_fload()  # 等待查询头折叠
        #time.sleep(0.5)

    def smart_alert_selectquery(self,num):
        '''智能选择框选择查询'''
        self.open_fold_query(num)
        self.hide_elem_by_jq('#activityTable')  # 隐藏按钮栏避免遮挡
        self.hide_elem_by_jq('#activityTable>.searchDiv')  # 隐藏按钮栏避免遮挡
        sas = self.find_elem('#searchFormTable input[name="智能提示选择框_show"]')
        self.scroll_to_target_element(sas)
        self.wait_elem_visible('#searchFormTable input[name="智能提示选择框_show"]')
        sas.send_keys('aa')
        #time.sleep(0.5)
        target = self.find_elem('.typeahead')
        self.scroll_to_target_element(target)
        self.wait_elem_visible('.typeahead')
        target.click()
        self.scroll_to_target_element(self.find_elem('#searchFormTable .row'))  # 滚到查询按钮位置

        self.find_elem_visible('#searchFormTable .btn-primary').click()
        self.wait_query_fload()  # 等待查询头折叠
        #time.sleep(0.5)