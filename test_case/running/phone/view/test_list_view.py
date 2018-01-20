import sys
sys.path.append('../../../../')
import time
import unittest
from test_case.running.phone.view.view_test import ViewPhoneTest
from test_case.page_obj.button_page import ButtonPhonePage
from test_case.page_obj.main_page import MainPhonePage
from test_case.page_obj.view.list_view_page import ListViewPhonePage


class ListViewPhoneTest(ViewPhoneTest):
    '''列表视图测试'''
    
    menu1 = '视图'
    menu2 = '列表视图'
    
    def test_paging_not(self):
        '''不分页'''
        menu3 = '列表视图_分页_否'
        mp = MainPhonePage(self.driver)
        mp.open_menus(self.menu1, self.menu2, menu3)  # 打开菜单
        
        lp = ListViewPhonePage(self.driver)
        lp.wait_Tabloading_show_then_hide()
        self.assertEqual('', lp.get_pagination_body(), msg='不分页检验不通过')

    def test_paging_5(self):
        '''分页-每页5条'''
        menu3 = '列表视图_分页_5条'
        mp = MainPhonePage(self.driver)
        mp.open_menus(self.menu1, self.menu2, menu3)  # 打开菜单
        
        lp = ListViewPhonePage(self.driver)
        lp.wait_Tabloading_show_then_hide()
        self.assertEqual(5, lp.get_rows_total(), msg='分页-每页5条检验不通过')

    def test_paging_10(self):
        '''分页-每页10条'''
        menu3 = '列表视图_分页_10条'
        mp = MainPhonePage(self.driver)
        mp.open_menus(self.menu1, self.menu2, menu3)  # 打开菜单
        
        lp = ListViewPhonePage(self.driver)
        lp.wait_Tabloading_show_then_hide()
        self.assertEqual(10, lp.get_rows_total(), msg='分页-每页10条检验不通过')

    def test_paging_15(self):
        '''分页-每页15条'''
        menu3 = '列表视图_分页_15条'
        mp = MainPhonePage(self.driver)
        mp.open_menus(self.menu1, self.menu2, menu3)  # 打开菜单
        
        lp = ListViewPhonePage(self.driver)
        lp.wait_Tabloading_show_then_hide()
        self.assertEqual(15, lp.get_rows_total(), msg='分页-每页15条检验不通过')

    def test_paging_30(self):
        '''分页-每页30条'''
        menu3 = '列表视图_分页_30条'
        mp = MainPhonePage(self.driver)
        mp.open_menus(self.menu1, self.menu2, menu3)  # 打开菜单
        
        lp = ListViewPhonePage(self.driver)
        lp.wait_Tabloading_show_then_hide()
        self.assertEqual(30, lp.get_rows_total(), msg='分页-每页30条检验不通过')
        
    #只读功能
    def test_readonly_not(self):
        '''非只读'''
        menu3 = '列表视图_只读_否'
        mp = MainPhonePage(self.driver)
        mp.open_menus(self.menu1, self.menu2, menu3)  # 打开菜单
        lp = ListViewPhonePage(self.driver)
        lp.wait_Tabloading_show_then_hide()
        lp.open_fisrt_doc()
        lp.wait_Tabloading_show_then_hide()
        btn = ButtonPhonePage(self.driver)
        self.assertTrue(btn.is_button_exist('保存'), msg='非只读检验不通过')
         
    def test_readonly(self):
        '''只读'''
        menu3 = '列表视图_只读_是'
        mp = MainPhonePage(self.driver)
        mp.open_menus(self.menu1, self.menu2, menu3)  # 打开菜单
        lp = ListViewPhonePage(self.driver)
        lp.wait_Tabloading_show_then_hide()
        lp.open_fisrt_doc()
        lp.wait_Tabloading_show_then_hide()
        btn = ButtonPhonePage(self.driver)
        self.assertTrue(btn.is_button_exist('新建'), msg='非只读检验不通过')
         
    '''列功能验证'''
         
    def test_column_multilingual(self):
        '''列多语言'''
        menu3 = '列表视图_列_多语言'
        mp = MainPhonePage(self.driver)
        mp.open_menus(self.menu1, self.menu2, menu3)  # 打开菜单
        lp = ListViewPhonePage(self.driver)
        lp.wait_Tabloading_show_then_hide()
        self.assertIsNotNone(lp.get_column_head('文本二'), msg='列多语言检验不通过')
     
    def test_column_iscript(self):
        '''类型脚本'''
        menu3 = '列表视图_列_类型_脚本'
        mp = MainPhonePage(self.driver)
        mp.open_menus(self.menu1, self.menu2, menu3)  # 打开菜单
        lp = ListViewPhonePage(self.driver)
        lp.wait_Tabloading_show_then_hide()
        self.assertEqual('aaa', lp.get_column_row1_col1(), msg='类型脚本检验不通过')
         
    def test_column_order(self):
        '''类型序号'''
        menu3 = '列表视图_列_类型_序号'
        mp = MainPhonePage(self.driver)
        mp.open_menus(self.menu1, self.menu2, menu3)  # 打开菜单
        lp = ListViewPhonePage(self.driver)
        lp.wait_Tabloading_show_then_hide()
        self.assertEqual('1', lp.get_column_row1_col1(), msg='类型序号检验不通过')
     
    def test_column_show_val(self):
        '''显示值'''
        menu3 = '列表视图_列_值类型_显示值'
        mp = MainPhonePage(self.driver)
        mp.open_menus(self.menu1, self.menu2, menu3)  # 打开菜单
        lp = ListViewPhonePage(self.driver)
        lp.wait_Tabloading_show_then_hide()
        self.assertEqual('测试部', lp.get_column_row1_col1(), msg='显示值检验不通过')
     
    def test_column_true_val(self):
        '''真实值'''
        menu3 = '列表视图_列_值类型_真实值'
        mp = MainPhonePage(self.driver)
        mp.open_menus(self.menu1, self.menu2, menu3)  # 打开菜单
        lp = ListViewPhonePage(self.driver)
        lp.wait_Tabloading_show_then_hide()
        self.assertEqual('11e7-5f99-e70d1a49-917f-e799edecb417', lp.get_column_row1_col1(), msg='真实值检验不通过')
     
    def test_column_sort_up(self):
        '''排序升序'''
        menu3 = '列表视图_列_排序_升序'
        mp = MainPhonePage(self.driver)
        mp.open_menus(self.menu1, self.menu2, menu3)  # 打开菜单
        lp = ListViewPhonePage(self.driver)
        lp.wait_Tabloading_show_then_hide()
        self.assertIn('up.gif', lp.get_column_sort_img_src('列表视图_部门选择框'), msg='真实值检验不通过')
     
    def test_column_sort_down(self):
        '''排序降序'''
        menu3 = '列表视图_列_排序_降序'
        mp = MainPhonePage(self.driver)
        mp.open_menus(self.menu1, self.menu2, menu3)  # 打开菜单
        lp = ListViewPhonePage(self.driver)
        lp.wait_Tabloading_show_then_hide()
        self.assertIn('down.gif', lp.get_column_sort_img_src('列表视图_部门选择框'), msg='真实值检验不通过')
         
    def test_column_return_mark(self):
        '''流程回退标识'''
        menu3 = '列表视图_列_流程回退标识'
        mp = MainPhonePage(self.driver)
        mp.open_menus(self.menu1, self.menu2, menu3)  # 打开菜单
        lp = ListViewPhonePage(self.driver)
        lp.wait_Tabloading_show_then_hide()
        self.assertIn('backstatelabel01.gif', lp.get_column_row1_col1_img(), msg='真实值检验不通过')
        self.assertIn('#ff0000', lp.get_column_row1_col1_font(), msg='真实值检验不通过')
    
    def test_column_hide(self):
        '''列隐藏'''
        menu3 = '列表视图_列_隐藏条件'
        mp = MainPhonePage(self.driver)
        mp.open_menus(self.menu1, self.menu2, menu3)  # 打开菜单
        lp = ListViewPhonePage(self.driver)
        lp.wait_Tabloading_show_then_hide()
        self.assertFalse(lp.is_column_head_hide('列表视图_树形视图选择框'), msg='列隐藏检验不通过')
    
    def test_column_type_jump(self):
        '''列-操作类型-跳转'''
        menu3 = '列表视图_列_操作类型_跳转'
        mp = MainPhonePage(self.driver)
        mp.open_menus(self.menu1, self.menu2, menu3)  # 打开菜单
        
        lp = ListViewPhonePage(self.driver)
        lp.wait_Tabloading_show_then_hide()
        lp.click_jump()
        btn = ButtonPhonePage(self.driver)
        lp.wait_Tabloading_show_then_hide()
        self.assertTrue(btn.is_button_exist('保存'), msg='非只读检验不通过')
         
    def test_column_type_del(self):
        '''列-操作类型-删除'''
        menu3 = '列表视图_列_操作类型_删除'
        mp = MainPhonePage(self.driver)
        mp.open_menus(self.menu1, self.menu2, menu3)  # 打开菜单
        lp = ListViewPhonePage(self.driver)
        lp.wait_Tabloading_show_then_hide()
        if lp.get_rows_total() == 0:
            lp.add_one_row()
         
        lp.wait_Tabloading_show_then_hide()
        if lp.get_rows_total() == 1:
            lp.click_del()
        lp.wait_Tabloading_show_then_hide()
        self.assertEqual(0, lp.get_rows_total(), msg='列-操作类型-删除检验不通过')
         
    def test_column_type_submit(self):
        '''列-操作类型-提交流程'''
        menu3 = '列表视图_列_操作类型_提交流程'
        mp = MainPhonePage(self.driver)
        mp.open_menus(self.menu1, self.menu2, menu3)  # 打开菜单
        lp = ListViewPhonePage(self.driver)
        lp.wait_Tabloading_show_then_hide()
        if lp.get_rows_total() != 0:
            lp.clear_all_data()
        
        lp.wait_Tabloading_show_then_hide()
        if lp.get_rows_total() == 0:
            lp.add_one_row()
         
        lp.wait_Tabloading_show_then_hide()
        if lp.get_rows_total() == 1:
            lp.click_submit()
        
        lp.wait_Tabloading_show_then_hide()
        lp.set_val_and_submit('请审批')
        lp.wait_Tabloading_show_then_hide()
        
        #点击行数据
        lp.open_fisrt_doc()
        lp.wait_Tabloading_show_then_hide()
        bp = ButtonPhonePage(self.driver)
        self.assertEqual(0, bp.is_button_exist('流程处理'), msg='列-操作类型-提交流程检验不通过')
         
    def test_column_open_by_module(self):
        '''列-操作类型-以模板表单方式打开'''
        menu3 = '列表视图_列_操作类型_以模板表单方式打开'
        mp = MainPhonePage(self.driver)
        mp.open_menus(self.menu1, self.menu2, menu3)  # 打开菜单
        lp = ListViewPhonePage(self.driver)
        lp.wait_Tabloading_show_then_hide()
        lp.click_module_btn()
        btn = ButtonPhonePage(self.driver)
        lp.wait_Tabloading_show_then_hide()
        self.assertFalse(btn.is_button_exist('新建'), msg='非只读检验不通过')
     
    def test_val_type_number(self):
        '''列-格式-类型-数值-小数3位且使用千分位分隔符'''
        menu3 = '列表视图_列_格式类型_数值_小数位千分位'
        mp = MainPhonePage(self.driver)
        mp.open_menus(self.menu1, self.menu2, menu3)  # 打开菜单
        lp = ListViewPhonePage(self.driver)
        lp.wait_Tabloading_show_then_hide()
        self.assertEqual('22,222.000', lp.get_column_row1_col1(), msg=menu3 + '检验不通过')
     
    def test_val_type_cash(self):
        '''列-格式-类型-货币_小数位美元'''
        menu3 = '列表视图_列_格式类型_货币_小数位美元'
        mp = MainPhonePage(self.driver)
        mp.open_menus(self.menu1, self.menu2, menu3)  # 打开菜单
        lp = ListViewPhonePage(self.driver)
        lp.wait_Tabloading_show_then_hide()
        self.assertEqual('$22,222.000', lp.get_column_row1_col1(), msg=menu3 + '检验不通过')
     
    def test_val_type_font_length(self):
        '''列_显示文字方式_文字长度'''
        menu3 = '列表视图_列_显示文字方式_文字长度'
        mp = MainPhonePage(self.driver)
        mp.open_menus(self.menu1, self.menu2, menu3)  # 打开菜单
        lp = ListViewPhonePage(self.driver)
        lp.wait_Tabloading_show_then_hide()
        self.assertEqual('666666...', lp.get_column_row1_col1(), msg=menu3 + '检验不通过')
     
    def test_page_turn(self):
        '''翻页'''
        menu3 = '列表视图_全选和翻页'
        mp = MainPhonePage(self.driver)
        mp.open_menus(self.menu1, self.menu2, menu3)  # 打开菜单
        lp = ListViewPhonePage(self.driver)
        lp.wait_Tabloading_show_then_hide()
        
        lp.click_next_page()    #点击下一页
        lp.wait_Tabloading_show_then_hide()
        self.assertEqual('777', lp.get_column_row1_col1(), msg=menu3 + '检验不通过')
        
        lp.click_prev_page()    #点击前一页
        lp.wait_Tabloading_show_then_hide()
        self.assertEqual('666', lp.get_column_row1_col1(), msg=menu3 + '检验不通过')
        
        lp.click_end_page()    #点击末页
        lp.wait_Tabloading_show_then_hide()
        self.assertEqual('999', lp.get_column_row1_col1(), msg=menu3 + '检验不通过')
    
        lp.click_first_page()    #点击首页
        lp.wait_Tabloading_show_then_hide()
        self.assertEqual('666', lp.get_column_row1_col1(), msg=menu3 + '检验不通过')
        
    def init(self):
#         self.test_paging_not()
#         self.test_paging_5()
#         self.test_paging_10()
#         self.test_paging_15()
#         self.test_paging_30()
#         self.test_readonly_not()
#         self.test_readonly()
#         self.test_column_multilingual()
#         self.test_column_iscript()
#         self.test_column_order()
#         self.test_column_show_val()
#         self.test_column_true_val()
#         self.test_column_sort_up()
#         self.test_column_sort_down()
#         self.test_column_return_mark()
#         self.test_column_hide()
#         self.test_column_type_jump()
#         self.test_column_type_del()
        self.test_column_type_submit()
#         self.test_column_open_by_module()
#         self.test_val_type_number()
#         self.test_val_type_cash()
#         self.test_val_type_font_length()
#         self.test_page_turn()
        
    
if __name__ == '__main__':
    unittest.main()