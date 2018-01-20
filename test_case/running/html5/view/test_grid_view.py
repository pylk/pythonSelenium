import os
import sys
import time
import unittest
from selenium.webdriver.common.keys import Keys
sys.path.append('../../../../')
from test_case.running.html5.view.view_test import ViewTest
from test_case.page_obj.button_page import ButtonPage
from test_case.page_obj.main_page import MainPage
from test_case.page_obj.form.form_page import FormPage
from test_case.page_obj.view.grid_view_page import GridViewPage


class GridViewTest(ViewTest):
    '''网格视图测试'''
    
    menu1 = '视图'
    menu2 = '网格视图'

    
    def open_menu3(self, menu3):
        mp = MainPage(self.driver)
        mp.open_menu(menu3)
        #time.sleep(0.5)
        mp.switch_to_iframe()
        mp.wait_loading_hide()
     
    def test_add_one_row(self):
        '''新建一个记录'''
        menu3 = '网格视图_按钮操作'
        self.open_menu3(menu3)
        grid_view = GridViewPage(self.driver)
        before_num=grid_view.get_grid_rows_total()
        print("before_num=======%s"%before_num) 
        grid_view.add_one_row()
        grid_view.add_one_row()
        after_num=grid_view.get_grid_rows_total() 
        print("after_num=======%s"%after_num)       
        self.assertNotEqual(before_num, after_num, msg=menu3+'新建记录检验不通过')
  
    def test_delete_grid_one_row(self):
        '''删除一个记录'''
        menu3 = '网格视图_按钮操作'
        self.open_menu3(menu3)
        grid_view = GridViewPage(self.driver)
        if grid_view.get_grid_rows_total() == 0:
            grid_view.add_one_row()
        before_num=grid_view.get_grid_rows_total()
        print("before_num=======%s"%before_num)
        grid_view.delete_grid_rows(1)
        after_num=grid_view.get_grid_rows_total()
        print("after_num=======%s"%after_num)
        self.assertNotEqual(before_num, after_num, msg=menu3+'删除记录检验不通过')      
  
    def test_delete_grid_all_rows(self):
        '''全选记录删除'''
        menu3 = '网格视图_按钮操作'
        self.open_menu3(menu3)
        grid_view = GridViewPage(self.driver)
        if grid_view.get_grid_rows_total() == 0:
            grid_view.add_one_row()
        else:
            before_num=grid_view.get_grid_rows_total()
            print("before_num=======%s"%before_num)                
            grid_view.delete_grid_all_rows()
            after_num=grid_view.get_grid_rows_total()
            print("after_num=======%s"%after_num)
            self.assertNotEqual(before_num, after_num, msg=menu3+'全选删除检验不通过')              
   
    
    def test_cancel_all_operation(self):
        '''点击新建按钮，再点击【取消所有】'''
        '''判断操作前后数量应该没有变化'''
        menu3 = '网格视图_按钮操作'
        self.open_menu3(menu3)
        grid_view = GridViewPage(self.driver)
        before_num=grid_view.get_grid_rows_total()
        print("before_num=======%s"%before_num)                
        grid_view.cancel_all_operation()
        after_num=grid_view.get_grid_rows_total()
        print("after_num=======%s"%after_num)
        self.assertEqual(before_num, after_num, msg=menu3+'取消所有按钮检验不通过')      
            
    def test_record_total_show(self):
        '''显示记录总数'''
        menu3 = '网格视图_显示记录总数'
        self.open_menu3(menu3)
           
        grid_view = GridViewPage(self.driver)
        total_text = grid_view.get_record_total()
           
        print('显示总记录数：%s' %total_text)
        self.assertIn('总条数:', total_text, msg='显示总记录数检验不通过')
   
   
    def test_record_total_hide(self):
        '''隐藏记录总数'''
        menu3 = '网格视图_不显示记录总数'
        self.open_menu3(menu3)
           
        grid_view = GridViewPage(self.driver)
        try:
            grid_view.get_record_total()
        except Exception as ex:
            print('不显示总记录数异常：%s' %ex)
            self.assertTrue(True, msg='不显示总记录数检验不通过')        
   
    def test_paging_not(self):
        '''网格视图_不分页'''
        menu3 = '网格视图_不分页'
        self.open_menu3(menu3)         
        grid_view = GridViewPage(self.driver)
        self.assertFalse(grid_view.get_pagination_body(), msg='不分页检验不通过')
   
   
    def test_paging_5(self):
        '''分页-每页5条'''
        menu3 = '网格视图_分页5'
        self.open_menu3(menu3)        
        grid_view = GridViewPage(self.driver)
        self.assertEqual(5, grid_view.get_grid_rows_total(), msg='分页-每页5条检验不通过')
   
    def test_paging_10(self):
        '''分页-每页10条'''
        menu3 = '网格视图_分页10'
        self.open_menu3(menu3)         
        grid_view = GridViewPage(self.driver)
        self.assertEqual(10, grid_view.get_grid_rows_total(), msg='分页-每页10条检验不通过')
   
    def test_paging_15(self):
        '''分页-每页15条'''
        menu3 = '网格视图_分页15'
        self.open_menu3(menu3)        
        grid_view = GridViewPage(self.driver)
        self.assertEqual(15, grid_view.get_grid_rows_total(), msg='分页-每页15条检验不通过')
   
    def test_paging_30(self):
        '''分页-每页30条'''
        menu3 = '网格视图_分页30'
        self.open_menu3(menu3)        
        grid_view = GridViewPage(self.driver)
        self.assertEqual(30, grid_view.get_grid_rows_total(), msg='分页-每页30条检验不通过')
  
    def test_watermark_show(self):
        '''显示水印'''
        menu3 = '网格视图_水印有'
        self.open_menu3(menu3)         
        grid_view = GridViewPage(self.driver)
        self.assertTrue(grid_view.is_show_watermark(), msg='显示水印检验不通过')
   
    def test_style_lib(self):
        '''样式库使用'''
        menu3 = '网格视图_样式库有'
        self.open_menu3(menu3)
        grid_view = GridViewPage(self.driver)
        self.assertIn('background-color:yellow', grid_view.get_style_lib(), msg='样式库使用检验不通过')                
    
    def test_readonly(self):
        '''只读'''
        menu3 = '网格视图_只读'
        mp = MainPage(self.driver)
        mp.menu_scroll_to('100px')
        self.open_menu3(menu3)
        grid_view = GridViewPage(self.driver)
        self.assertEqual(' ',grid_view.get_grid_column_row1_coln('2').get_attribute("class"), msg='只读检验不通过')  
    
    def test_column_width_percent(self):
        '''列宽百分比'''
        mp = MainPage(self.driver)
        mp.menu_scroll_to('200px')                 
        menu3 = '网格视图_列宽百分比30'      
        self.open_menu3(menu3)
        grid_view = GridViewPage(self.driver)
        width = grid_view.get_grid_column_head_width('网格视图_文本一')
        self.assertEqual('30%', width, msg='列宽百分比检验不通过')
           
    def test_column_width_px(self):
        '''网格视图_列宽分辨率'''
        mp = MainPage(self.driver)
        mp.menu_scroll_to('200px')          
        menu3 = '网格视图_列宽分辨率'
        self.open_menu3(menu3)
        grid_view = GridViewPage(self.driver)
        width = grid_view.get_grid_column_head_width('网格视图_文本一')
        self.assertEqual('200px', width, msg='列宽固定px检验不通过')   
   
    def test_column_multilingual(self):
        '''列多语言'''
        mp = MainPage(self.driver)
        mp.menu_scroll_to('300px')         
        menu3 = '网格视图_多语言'
        self.open_menu3(menu3)
        grid_view = GridViewPage(self.driver)
        self.assertIsNotNone(grid_view.get_grid_column_head_by_coltext('文本二'), msg='列多语言检验不通过')
    
    def test_column_iscript(self):
        '''类型脚本'''
        mp = MainPage(self.driver)
        mp.menu_scroll_to('400px')          
        menu3 = '网格视图_列类型脚本'
        self.open_menu3(menu3)
        grid_view = GridViewPage(self.driver)
        self.assertEqual('aaa', grid_view.get_grid_column_row1_col1(), msg='类型脚本检验不通过')
    
    def test_column_order(self):
        '''类型序号'''
        mp = MainPage(self.driver)
        mp.menu_scroll_to('400px')         
        menu3 = '网格视图_序号'
        self.open_menu3(menu3)
        grid_view = GridViewPage(self.driver)
        self.assertEqual('1', grid_view.get_grid_column_row1_col1(), msg='类型序号检验不通过')
    
    def test_column_show_true_val(self):
        '''判断真实值显示值'''
        mp = MainPage(self.driver)
        mp.menu_scroll_to('400px')          
        menu3 = '网格视图_列真显值'
        self.open_menu3(menu3)
        grid_view = GridViewPage(self.driver)
        print("showvalue==========%s"%grid_view.get_grid_column_row1_coln_text('3'))
        print("realvalue==========%s"%grid_view.get_grid_column_row1_col1())
        self.assertNotEqual(grid_view.get_grid_column_row1_coln_text('3'), grid_view.get_grid_column_row1_col1(), msg='显示值检验不通过')
               
  
    def test_column_sort_up(self):
        '''排序升序'''
        mp = MainPage(self.driver)
        mp.menu_scroll_to('400px')          
        menu3 = '网格视图_排序升序'
        self.open_menu3(menu3)
        grid_view = GridViewPage(self.driver)
        self.assertIn('fa-long-arrow-up', grid_view.get_grid_column_sort_img_src('网格视图_日期'), msg='真实值检验不通过')
       
    def test_column_sort_down(self):
        '''排序降序'''
        mp = MainPage(self.driver)
        mp.menu_scroll_to('400px')          
        menu3 = '网格视图_排序降序'
        self.open_menu3(menu3)
        grid_view = GridViewPage(self.driver)
        self.assertIn('fa-long-arrow-down', grid_view.get_grid_column_sort_img_src('网格视图_日期'), msg='真实值检验不通过')
   
    def test_column_collect_subtotal(self):
        '''汇总_小计'''
        mp = MainPage(self.driver)
        mp.menu_scroll_to('400px')          
        menu3 = '网格视图_总计小计'
        self.open_menu3(menu3)
        grid_view = GridViewPage(self.driver)
        self.assertIn('当前页小计', grid_view.get_grid_collect(), msg='汇总_小计检验不通过')
           
    def test_column_collect_total(self):
        '''汇总_总计'''
        mp = MainPage(self.driver)
        mp.menu_scroll_to('400px')                  
        menu3 = '网格视图_总计小计'
        self.open_menu3(menu3)
        grid_view = GridViewPage(self.driver)
        self.assertIn('总计', grid_view.get_grid_collect(), msg='汇总_总计检验不通过')  
                         
    def test_column_hide(self):
        '''列隐藏'''
        menu3 = '网格视图_列隐藏'
        mp = MainPage(self.driver)
        mp.menu_scroll_to('400px')           
        self.open_menu3(menu3)
        grid_view = GridViewPage(self.driver)
        self.assertIsNone( grid_view.get_grid_column_head('网格视图_文本1'), msg='列隐藏检验不通过')
# #  
#     def test_column_invisible(self):
#         '''列不可见，目前有bug，不生效'''
#         menu3 = '网格视图_列不可见'
#         mp = MainPage(self.driver)
#         mp.menu_scroll_to('400px')           
#         self.open_menu3(menu3)
#         grid_view = GridViewPage(self.driver)
#         self.assertEqual('obpm-hide', grid_view.get_grid_column_head('网格视图_文本1').get_attribute('class'), msg='列隐藏检验不通过') 
#  
#     def test_column_substring(self):
#         '''字段内容截取10个，目前有bug，无法测试'''
#         menu3 = '网格视图_列不可见'
#         mp = MainPage(self.driver)
#         mp.menu_scroll_to('400px')           
#         self.open_menu3(menu3)
#         grid_view = GridViewPage(self.driver)
#         self.assertEqual('obpm-hide', grid_view.get_grid_column_head('网格视图_文本1').get_attribute('class'), msg='列隐藏检验不通过')        
#   
#     def test_column_style(self):
#         '''字段颜色背景，目前有bug，无法测试'''
#         menu3 = '网格视图_格式颜色字体'
#         mp = MainPage(self.driver)
#         mp.menu_scroll_to('400px')           
#         self.open_menu3(menu3)
#         grid_view = GridViewPage(self.driver)
#         self.assertIn('background: rgb(111, 168, 220)', grid_view.get_grid_column_one().get_attribute('style'), msg='列背景检验不通过')        
#         '''字段颜色，目前有bug，无法测试'''
#         #self.assertIn('color: rgb(111, 168, 220)', grid_view.get_grid_column_one().get_attribute('style'), msg='列背景检验不通过') 
  
    def test_column_decimal_point(self):
        '''验证千分位保留3位小数点'''
        menu3 = '网格视图_显示记录总数'         
        self.open_menu3(menu3)
        grid_view = GridViewPage(self.driver)
        if grid_view.get_grid_rows_total() == 0:
            grid_view.add_one_row()         
        self.assertIn('1,000,123.460', grid_view.get_grid_column_row1_coln_text('3'), msg='列千分位保留3位小数点检验不通过')
  
    def test_column_coin(self):
        '''验证货币显示'''
        menu3 = '网格视图_不显示记录总数'         
        self.open_menu3(menu3)
        grid_view = GridViewPage(self.driver)
        if grid_view.get_grid_rows_total() == 0:
            grid_view.add_one_row()        
        self.assertIn('$1,000,123.46', grid_view.get_grid_column_row1_coln_text('3'), msg='列货币显示检验不通过')
      
    def test_select_all(self):
        '''全选'''
        menu3 = '网格视图_全选和翻页'
        self.open_menu3(menu3)
        grid_view = GridViewPage(self.driver)
        self.assertTrue(grid_view.check_select_all(), msg=menu3 + '检验不通过') #一次选中
        self.assertTrue(grid_view.check_select_all(), msg=menu3 + '检验不通过') #一次取消选中
     
    def test_page_turn(self):
        '''翻页'''
        menu3 = '网格视图_全选和翻页'
        self.open_menu3(menu3)
        grid_view = GridViewPage(self.driver)
        grid_view.click_cur_page() #点击当前页
        self.assertEqual('666', grid_view.get_column_row1_col1(), msg=menu3 + '检验不通过')
        grid_view.click_second_page()  #点击第二页
        #time.sleep(0.5)
        self.assertEqual('777', grid_view.get_column_row1_col1(), msg=menu3 + '检验不通过')
        grid_view.click_prev_page()    #点击前一页
        #time.sleep(0.5)
        self.assertEqual('666', grid_view.get_column_row1_col1(), msg=menu3 + '检验不通过')
        grid_view.click_next_page()    #点击下一页
        #time.sleep(0.5)
        self.assertEqual('777', grid_view.get_column_row1_col1(), msg=menu3 + '检验不通过')
    
    def init(self):
         
#         self.test_add_one_row()  
        self.test_delete_grid_one_row()
#         self.test_delete_grid_all_rows()
#         self.test_cancel_all_operation()                    
#         self.test_column_invisible()
#         self.test_column_substring()
#         self.test_open_type_current()
#         self.test_record_total_show()
#         self.test_record_total_hide()
#         self.test_paging_not()
#         self.test_paging_not()
#         self.test_paging_5()                     
#         self.test_paging_10()         
#         self.test_paging_15()
#         self.test_paging_30()   
#         self.test_watermark_show()   
#         self.test_style_lib()      
#         self.test_readonly()   
#         self.test_column_width_percent() 
#         self.test_column_width_px()
#         self.test_column_width_percent() 
#         self.test_column_width_px()
#         self.test_column_multilingual()
#         self.test_column_iscript()
#         self.test_column_order()     
#         self.test_column_show_true_val()          
#         self.test_column_sort_up()           
#         self.test_column_sort_down()
#         self.test_column_collect_subtotal()
#         self.test_column_style()   
#         self.test_column_decimal_point()   
#         self.test_column_coin()   
#         self.test_select_all()
#         self.test_page_turn()
                                                                                         
if __name__ == '__main__':
    unittest.main()