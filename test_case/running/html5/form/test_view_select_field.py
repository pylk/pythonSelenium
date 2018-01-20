import os,sys
sys.path.append('../../../../')
import time
import unittest
from selenium.webdriver.common.keys import Keys
from test_case.page_obj.form.view_select_page import ViewSelectPage
from test_case.page_obj.main_page import MainPage
from test_case.page_obj.page import Page

sys.path.append('../')
from test_case.running.html5.form.component_test import ComponentTest
from selenium.webdriver.support.ui import Select


class ViewSelectTest(ComponentTest):
    '''视图选择框测试'''

    menu1 = '表单'
    menu2 = '表单控件'
    menu3 = '视图选择框'  # 主页打开菜单时使用

    def test_type_case(self):
        '''类型'''
        value = '说明文字：自动化测试'
        name = '视图选择框说明文字'
        self.scroll_to('0')
        comp = ViewSelectPage(self.driver, value)
        comp.open_default().click()
        mp = MainPage(self.driver)
        mp.switch_to_parent()   # 切换到主页
        title = comp.find_elem_visible('div.aui_header>span.aui_title').text
        self.assertIn("视图框", title, msg=name + "检验不通过")

    def test_mapped_case(self):
        '''默认模式映射'''
        value = '说明文字：自动化测试'
        name = '视图选择框默认模式映射'
        #time.sleep(0.5)
        self.scroll_to('0')
        comp = ViewSelectPage(self.driver, value)
        mp = MainPage(self.driver)
        
        # 打开视图选择框
        comp.open_default().click()
        #time.sleep(0.5)
        # 找到打开视图选择框的iframe,并切过去
        mp.switch_to_div_iframe()
        # 选择元素
        comp.find_elem_is_clickable('div[id="valuemap0"]+a').click()
        #time.sleep(0.5)
        mp.switch_to_parent()   # 切换到主页
        mp.switch_to_iframe()   # 切换到当前打开的iframe
        # 返回真实字段的元素值
        self.assertEqual("1", comp.return_inputvalue(), msg=name + "检验不通过")

    def test_mosaic_case(self):
        '''拼接模式映射'''
        value = '拼接模式'
        name = '视图选择框拼接模式映射'
        #time.sleep(0.5)
        self.scroll_to('100')
        comp = ViewSelectPage(self.driver, value)
        mp = MainPage(self.driver)
        # 打开视图选择框
        comp.open_default().click()
        #time.sleep(0.5)
        mp.switch_to_div_iframe()   # 切换到弹出层
        comp.find_elem_is_clickable('tbody>tr:nth-child(2)>td:nth-child(1)>a').click()
        comp.find_elem_is_clickable('tbody>tr:nth-child(3)>td:nth-child(2)>a').click()
        #点击确认按钮
        comp.click_primary_btn()
        #time.sleep(0.5)
        # 返回到表单所在的iframe
        mp.switch_to_parent()   # 切换到主页
        mp.switch_to_iframe()   # 切换到当前打开的iframe
        # 返回真实字段的元素值
        val = comp.return_inputvalue()
        self.assertIn("1;选择框2", val, msg=name + "检验不通过")

    def test_mosaic_clear_case(self):
        '''拼接模式清除操作'''
        value = '拼接模式'
        name = '视图选择框拼接模式清除操作'
        #time.sleep(0.5)
        self.scroll_to('100')
        comp = ViewSelectPage(self.driver, value)
        mp = MainPage(self.driver)
        # 打开视图选择框
        comp.open_default().click()
        #time.sleep(0.5)
        mp.switch_to_div_iframe()   # 切换到弹出层
        #
        comp.find_elem_is_clickable('tbody>tr:nth-child(2)>td:nth-child(1)>a').click()
        comp.find_elem_is_clickable('tbody>tr:nth-child(3)>td:nth-child(2)>a').click()
        comp.window_scrollTo('100')
        # 点击清除按钮
        comp.click_default_btn()
        #点击确认按钮
        comp.click_primary_btn()
        #time.sleep(0.5)
        # 返回到表单所在的iframe
        mp.switch_to_parent()   # 切换到主页
        mp.switch_to_iframe()   # 切换到当前打开的iframe
        # 返回真实字段的元素值
        val = comp.return_inputvalue()
        self.assertEqual("", val, msg=name + "检验不通过")


    def test_multiterm_case(self):
        '''多项选择模式映射'''
        value = '多项选择'
        name = '视图选择框多项选择模式映射'
        #time.sleep(0.5)
        self.scroll_to('100')
        comp = ViewSelectPage(self.driver, value)
        mp = MainPage(self.driver)
        # 打开视图选择框
        comp.open_default().click()
        #time.sleep(0.5)
        mp.switch_to_div_iframe()   # 切换到弹出层
        #
        comp.find_elem_is_clickable('div#dspview_divid tr:nth-child(2) > td.listDataTrFirstTd > input').click()
        comp.find_elem_is_clickable('div#dspview_divid tr:nth-child(5) > td.listDataTrFirstTd > input').click()
        comp.find_elem_is_clickable('div.col-xs-12 li:nth-child(1) > a').click()
        #time.sleep(0.5)
        # 返回到表单所在的iframe
        mp.switch_to_parent()   # 切换到主页
        mp.switch_to_iframe()   # 切换到当前打开的iframe
        # 返回真实字段的元素值
        val = comp.return_inputvalue()
        self.assertIn("1;4", val, msg=name + "检验不通过")

    def test_multiterm_remove_case(self):
        '''多项选择模式清除已选项'''
        value = '多项选择'
        name = '视图选择框多项选择模式清除已选项'
        #time.sleep(0.5)
        self.scroll_to('100')
        comp = ViewSelectPage(self.driver, value)
        mp = MainPage(self.driver)
        
        # 打开视图选择框
        comp.open_default().click()
        #time.sleep(0.5)
        mp.switch_to_div_iframe()   # 切换到弹出层
        #
        comp.find_elem_is_clickable('div#dspview_divid tr:nth-child(2) > td.listDataTrFirstTd > input').click()
        comp.find_elem_is_clickable('div#dspview_divid tr:nth-child(5) > td.listDataTrFirstTd > input').click()
        comp.find_elem_is_clickable('td.right-box  li.active > a').click()
        comp.find_elem_is_clickable('div.col-xs-12 li:nth-child(1) > a').click()
        
        #time.sleep(0.5)
        # 返回到表单所在的iframe
        mp.switch_to_parent()   # 切换到主页
        mp.switch_to_iframe()   # 切换到当前打开的iframe
        
        # 返回真实字段的元素值
        val = comp.return_inputvalue()
        self.assertEqual("", val, msg=name + "检验不通过")

    def test_recalculation_case(self):
        '''重计算'''
        value = '重计算'
        name = '视图选择框重计算'
        self.scroll_to('0')
        comp = ViewSelectPage(self.driver, value)
        comp.sendkeyforInput() #给真实值字段输入“隐藏”
        #time.sleep(0.5)
        comp.trigged_update()
        css = 'input.btn-default[value="重计算"]'
        bool = comp.is_elementPresent(css)
        self.assertTrue(bool,msg=name + "检验不通过")

    def test_show_when_hide_case(self):
        '''隐藏时显示值'''
        self.scroll_to('80')
        name = '视图选择框隐藏时显示值'
        comp = ViewSelectPage(self.driver, name)
        title = comp.find_elem('td.视图选择框_隐藏时显示值>span').text
        self.assertIn(title,'该控件已隐藏',msg=name + "检验不通过")

    def test_display_case(self):
        """条件只读"""
        value = '只读条件'
        name = '视图选择框：只读条件'
        self.scroll_to('100')
        #time.sleep(0.5)
        comp = ViewSelectPage(self.driver, value)
        a = comp.open_default()
        bool = a.get_attribute('disabled')
        self.assertTrue(bool,msg=name + "检验不通过")

    def test_confirm_case(self):
        """确定条件为false"""
        
        value = '确定条件'
        name = '视图选择框：确定条件'
        self.scroll_to('200')
        #time.sleep(0.5)
        comp = ViewSelectPage(self.driver, value)
        mp = MainPage(self.driver)
        # 打开视图选择框
        comp.open_default().click()
        mp.switch_to_div_iframe()   # 切换到弹出层
        comp.wait_view_select_tab_show() #等待视图选择框显示
        # 选择元素
        comp.find_elem_visible('div[id="valuemap0"]+a').click()
        #time.sleep(0.5)
        #去到警告框
        p = self.driver.switch_to_alert().text
        #time.sleep(0.5)
        self.driver.switch_to_alert().accept()
        self.assertIn(p,"确定条件出错，请联系后台管理员",msg=name + "检验不通过")

#模板有问题注释
    # def test_afterconfirm_case(self):
    #     """确定后执行脚本"""
    #     value = '确定后执行脚本'
    #     name = '视图选择框：确定后执行脚本'
    #     self.scroll_to('200')
    #     #time.sleep(0.5)
    #     comp = ViewSelectPage(self.driver, value)
    #     mp = MainPage(self.driver)
    #
    #     # 打开视图选择框
    #     comp.open_default().click()
    #     # 找到打开视图选择框的iframe,并切过去
    #     mp.switch_to_div_iframe()
    #     # 选择元素
    #     comp.find_elem_is_clickable('div[id="valuemap0"]+a').click()
    #     #time.sleep(0.5)
    #     mp.switch_to_parent()   # 切换到主页
    #     mp.switch_to_iframe()   # 切换到当前打开的iframe
    #
    #     self.scroll_to('0')
    #     p = comp.find_elem_visible('input[name="显示值"]').text
    #     self.assertEqual(p, "确定后执行条件生效", msg=name + "检验不通过")

    def init(self):
#         self.test_confirm_case()
#         self.test_mapped_case()
        self.test_afterconfirm_case()
    
    
if __name__ == '__main__':
    unittest.main()




