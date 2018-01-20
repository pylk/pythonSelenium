import os,sys
sys.path.append('../../../')
import time
import unittest
import run_test_all_html5
from selenium.webdriver.common.keys import Keys
from test_case.page_obj.button_page import ButtonPage
from test_case.page_obj.page  import Page


class GanttViewPage(Page):
    """甘特视图"""

    def check_add(self,name):
        '''根据文本来检测是否新建记录成功'''
        s = self.driver.find_elements_by_link_text(name)
        if len(s) >=1:
            return True
        else:
            return False

    def judge_delete(self,name):
        """判断是否已存在记录有则删除"""
        s = self.driver.find_elements_by_link_text(name)
        if len(s) >=1:
            print("记录已存在，需要删除")
            #time.sleep(0.5)
            self.driver.find_element_by_xpath('//a[@title="'+name+'"]/parent::div/input').click()
            btn = ButtonPage(self.driver)
            btn.click_activityTable_button(btn.del_btn)
            self.driver.switch_to_alert().accept()
            btn.wait_loading_hide()
            #time.sleep(0.5)
        else:
            print("记录不存在，不需要删除")


    def checkhour(self):
        '''用视图年月日格式的行数的第五行来体现是不是小时形式显示'''
        if self.find_elem('#dataTable  div.rightPanel  div.row.ganttTitle:nth-child(5)')!=None:
            return True
        else:
            return False

    def check_hang(self,num):
        '''num表示视图年月日格式的行数'''
        if self.find_elem('#dataTable  div.rightPanel  div.row.ganttTitle:nth-child('+num+')>div')!=None:
            return True
        else:
            return False



