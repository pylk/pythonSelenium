import re
import string
import sys

import time

sys.path.append('../../')
from test_case.page_obj.main_page import MainPhonePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class FlowCenterPhonePage(MainPhonePage):
    '''流程中心'''

    def click_all_filter(self, name):
        '''点击 全部 或者 筛选'''
        self.wait_elem_visible('pending-app-filter')  # 等待 全部/筛选 显示
        lis = self.find_elements('.pending-app-filter-item')  # 获取 全部/筛选
        for li in lis:
            if li.text == name:
                # 等待元素可点击
                li.click()
                self.wait_loading_hide()
                #time.sleep(0.5)  # 等待面板展开或者折叠

    def is_open_fold(self, name):
        '''判断 全部 和 筛选 是否打开或折叠'''
        self.click_all_filter(name)
        return self.find_element('.pending-nav').get_attribute('style') == 'display: block;'

    def is_filter_effect(self, list):
        '''判断筛选是否生效'''
        self.click_all_filter('筛选\n▲')
        self.wait_elem_visible('.pending-nav')  # 点击筛选后面板展开
        selected = self.find_element('.pending-nav li:nth-child(2)')
        selected.click()  # 点击面板中的第二个
        # 获取筛选后的结果
        for li in list:
            print(li.get_attribute('style'))
            if li.get_attribute('style') != 'display: none;':
                x = li.find_element_by_css_selector('.tabLiConA.text-left').text
                # [xxxxx] 去除两端中括号
                return x.strip().strip('[]') in selected.text

    def subject_search(self):
        '''主题搜索'''
        self.find_element('#_subject').send_keys('抄送设置')
        self.find_element('#searchBtn').click()
        self.wait_Tabloading_show_then_hide()

    def get_subject_search_return(self):
        '''返回主题搜索结果'''
        lis = self.find_elements('#finished .tabLiConA')
        for li in lis:
            if '抄送设置' in li.text:
                print(li.text)
                continue
            else:
                return False
        return True

    def click_new_build(self):
        '''点击我发起的'''
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#finish-pend'))).click()
        self.wait_Tabloading_show_then_hide()

    def get_click_newbuild_return(self):
        '''返回点击 我发起的 筛选结果'''
        lis = self.find_elements('.noAvatar')
        for li in lis:
            if li.text == '李玲':
                continue
            else:
                return False
        return True
