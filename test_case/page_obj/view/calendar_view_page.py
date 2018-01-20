import os,sys
sys.path.append('../../../')
import time
import unittest
import run_test_all_html5
from selenium.webdriver.common.keys import Keys
from test_case.page_obj.button_page import ButtonPage
from test_case.page_obj.page  import Page
from datetime import datetime
import random


class CalendarviewPage(Page):
    """日历视图"""
    
    def check_add(self,name):
        '''根据文本来检测是否新建记录成功'''
        s = self.driver.find_elements_by_partial_link_text(name)
        if len(s) >=1:
            return True
        else:
            return False

    def new_record(self,text):
        '''新建一条日历视图记录'''
        btn = ButtonPage(self.driver)
        today = self.gettoday()
        #time.sleep(0.5)
        btn.click_activityTable_button(btn.new_btn)
        btn.wait_loading_hide()
        #time.sleep(0.5)
        self.find_elem('input[name="填单时间"]').send_keys(today)
        self.find_elem('input[name="结束时间"]').send_keys("2018-07-01")
        #time.sleep(0.5)
        self.find_elem('textarea[name="备注"]').send_keys(text)
        btn.click_button(btn.save)
        btn.wait_loading_hide()
        btn.click_button(btn.to_return)
        btn.wait_loading_hide() #表单中
        #time.sleep(0.5)
        self.scroll_to('100')

    def switch_calendartype(self,title):
        '''根据名称切换日历视图类型'''
        self.find_elem('div.btn-group>a[title="'+title+'"]').click()
        #time.sleep(0.5)

    def click_more(self):
        '''点击more'''
        self.find_elem('#cal1 tr:nth-child(2)>td>div:nth-child(1)>div:nth-child(5)> a').click()
        self.wait_loading_hide()
        #time.sleep(0.5)

    def get_viewText(self):
        '''获取视图的内容'''
        #切到弹出框
        self.switch_to_Popup()
        text = self.find_elem('#viewHtml > div.table-body').text
        return text

    def scroll_to(self, y):
        '''执行js脚本，操作滚动条滚动到离页面顶部y值的位置'''
        #time.sleep(0.5)
        script = 'var $con = $("body");if($con.size()>0)$con.getNiceScroll(0).doScrollTop(' + y + ',10)'  # 滚动到控件可以看到后面的代码执行才不会报错
        self.driver.execute_script(script)
        #time.sleep(0.1)

    def gettoday(self):
        '''返回系统当前日期'''
        today = datetime.now().strftime('%Y-%m-%d')
        return today


    def buildnum(self):
        '''生成随机数'''
        li = ['0','1','2','3','4','5','6','7','8','9']
        num1 = random.sample(li,3)
        num = ''.join( num1 )
        return num


    def get_dayandweek_title(self):
        '''获取日周视图的title'''
        text = self.find_elem('#cal_viewcontent > table:nth-child(2)  table:nth-child(1)  tr:nth-child(1)').text
        return text

    def get_month_title(self):
        '''获取月视图的title'''
        text = self.find_elem('#cal_viewcontent  tr.weekDay').text
        return text

    def goto_yearmonth(self,n,r):
        '''去到具体的年月'''
        self.n = int(n)
        self.r = int(r)
        text = self.find_elem('#cal_viewcontent  a.btn.btn-green.eventTitle').text
        li = list(text)
        y1 = li[3]
        y = int(y1)
        if li[6]!=None:
            m1 = li[5]+li[6]
            m = int(m1)
        else:
            m1 = li[5]
            m = int(m1)
        while y < self.n:
            self.find_elem_is_clickable('#cal_viewcontent  a[title="下一年"]').click()
            self.wait_Tabloading_show_then_hide()
            y += 1
        while y > self.n:
            self.find_elem_is_clickable('#cal_viewcontent  a[title="上一年"]').click()
            self.wait_Tabloading_show_then_hide()
            y = y - 1
        while m < self.r:
            self.find_elem_is_clickable('#cal_viewcontent  a[title="下一月"]').click()
            self.wait_Tabloading_show_then_hide()
            m = m + 1
        while m > self.r:
            self.find_elem_is_clickable('#cal_viewcontent  a[title="上一月"]').click()
            self.wait_Tabloading_show_then_hide()
            m = m - 1