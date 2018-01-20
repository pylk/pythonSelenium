import os
import sys
import time
import unittest
from selenium.webdriver.common.keys import Keys
sys.path.append('../../../../')
from test_case.running.html5.app_test import AppTest
from test_case.page_obj.button_page import ButtonPage
from test_case.page_obj.main_page import MainPage
from test_case.page_obj.form.tab_page import TabPage
from test_case.page_obj.view.grid_view_page import GridViewPage
from test_case.page_obj.view.list_view_page import TabListViewPage
from test_case.page_obj.form.input_page import InputPage


class TabTest(AppTest):
    '''选项卡测试'''
    
    menu1 = '表单'
    menu2 = '表单控件'

    def open_menu3(self, menu3):
        mp = MainPage(self.driver)
        mp.open_menu(menu3)
        #time.sleep(0.5)
        mp.switch_to_iframe()

    def test_tab_switch_case(self):
        '''选项卡切换'''
        #判断切换后的字段是否可见
        mp = MainPage(self.driver)
        tab_name = '页签'
        menu3 = '选项卡_普通'
        self.open_menu3(menu3)
        tabpage = TabPage(self.driver,tab_name)
        tabpage.tab_switch()
        compname = tabpage.get_tab_item_by_name("选项卡_页签2_文本一")
        self.assertTrue(compname.is_displayed(), msg=menu3+'切换Tab检验不通过') 
                    
    def test_tab_save_case(self):
        '''选项卡保存'''
        #判断切换后的字段是否可见
        mp = MainPage(self.driver)
        tab_name = '页签'
        menu3 = '选项卡_普通'
        self.open_menu3(menu3)
        btn = ButtonPage(self.driver)
        btn.click_button(btn.save)
        btn.wait_loading_hide()
        tabpage = TabPage(self.driver,tab_name)
        self.assertIn('保存成功', tabpage.save_get_msg(), msg=menu3+'保存检验不通过')
     
    def test_tab_readonly_case(self):
        '''选项卡只读'''
        #判断切换后的字段是否可见
        mp = MainPage(self.driver)
        #time.sleep(0.5)
        name = '选项卡_页签1_文本一'
        menu3 = '选项卡_只读条件'
        self.open_menu3(menu3)
        tabpage = TabPage(self.driver,name)
        self.assertTrue(tabpage.span_is_displayed(), msg=menu3+'检验不通过')    
                   
    def test_tab_hide_case(self):
        '''选项卡隐藏'''
        #判断切换后的字段是否可见
        mp = MainPage(self.driver)
        #time.sleep(0.5)
        tab_name = '页签1'
        menu3 = '选项卡_隐藏条件'
        self.open_menu3(menu3)
        tabpage = TabPage(self.driver,tab_name)
        self.assertFalse(tabpage.find_tab_by_title().is_displayed(), msg=menu3+'检验不通过')  
     
                   
    def test_tab_selected_case(self):
        '''选项卡默认选择'''
        #判断切换后的字段是否可见
        mp = MainPage(self.driver)
        #time.sleep(0.5)
     
        tab_selected = '选项卡_页签2_文本一'
        menu3 = '选项卡_页签选中脚本'
        self.open_menu3(menu3)
        #默认是页签，判断页签是否在页面可见，其他tab不可见
        tabpage = TabPage(self.driver,"页签")
        compname = tabpage.get_tab_item_by_name('选项卡_页签2_文本一')
        self.assertTrue(compname.is_displayed(), msg=menu3+'检验不通过') 
     
     
    def test_tab_add_grid_case(self):
        '''增加网格视图记录'''
        #判断切换后的字段是否可见
        mp = MainPage(self.driver)        
        #time.sleep(0.5)
        menu3 = '选项卡_父子关系视图及重计算'
        self.open_menu3(menu3)        
        #网格视图是在iframe下
        mp.switch_to_grid_iframe()        
        grid_view = GridViewPage(self.driver)
        before_num=grid_view.get_grid_rows_total()
        print("before_num=======%s"%before_num)
        grid_view.add_one_row()
        after_num=grid_view.get_grid_rows_total()
        print("before_num=======%s"%before_num)
        self.assertNotEqual(before_num, after_num, msg=menu3+'新建记录检验不通过') 
      
    def test_tab_cancel_grid_case(self):
        '''网格视图取消所有'''
        #判断切换后的字段是否可见
        mp = MainPage(self.driver)       
        #time.sleep(0.5)
        menu3 = '选项卡_父子关系视图及重计算'
        self.open_menu3(menu3)        
        #网格视图是在iframe下
        mp.switch_to_grid_iframe()        
        grid_view = GridViewPage(self.driver)
        before_num=grid_view.get_grid_rows_total()
        print("before_num=======%s"%before_num)
        grid_view.cancel_all_operation()
        after_num=grid_view.get_grid_rows_total()
        print("after_num=======%s"%after_num)
        self.assertEqual(before_num, after_num, msg=menu3+'取消所有按钮检验不通过')  
#    
     
    def test_tab_delete_grid_case(self):
        '''网格视图删除一个记录'''
        #判断切换后的字段是否可见
        mp = MainPage(self.driver)
        menu3 = '选项卡_父子关系视图及重计算'
        self.open_menu3(menu3)        
        #网格视图是在iframe下
        mp.switch_to_grid_iframe()        
        grid_view = GridViewPage(self.driver)
        if grid_view.get_grid_rows_total() == 0:
            grid_view.add_one_row()
            print("录入数据了====")
        before_num=grid_view.get_grid_rows_total()
        print("before_num=======%s"%before_num)
        grid_view.delete_grid_rows(1)
        after_num=grid_view.get_grid_rows_total()
        print("after_num=======%s"%after_num)
        self.assertNotEqual(before_num, after_num, msg=menu3+'删除记录检验不通过')     
    
    
     
    def test_tab_delete_all_grid_case(self):
        '''网格视图删除全选记录'''
        #判断切换后的字段是否可见
        mp = MainPage(self.driver)
        menu3 = '选项卡_父子关系视图及重计算'
        self.open_menu3(menu3)        
        #网格视图是在iframe下
        mp.switch_to_grid_iframe()        
        grid_view = GridViewPage(self.driver)
        if grid_view.get_grid_rows_total() == 0:
            grid_view.add_one_row()
            print("录入数据了====")
        else:
            before_num=grid_view.get_grid_rows_total()
            print("before_num=======%s"%before_num)                
            grid_view.delete_grid_all_rows()
            after_num=grid_view.get_grid_rows_total()
            print("after_num=======%s"%after_num)
            self.assertNotEqual(before_num, after_num, msg=menu3+'全选删除检验不通过')    
      
    def test_tab_list_addrow_case(self):
        '''新建选项卡子记录'''  
        mp = MainPage(self.driver)
        menu3 = '选项卡_父子关系视图及重计算'
        self.open_menu3(menu3)
        #切换到另外的页签
        tab_name = '非父子视图'
        tabpage = TabPage(self.driver,tab_name)
        tabpage.tab_switch() 
        #time.sleep(0.5)
        tab_view = TabListViewPage(self.driver)
        btn_title = tab_view.tab_list_add_row()
        self.assertEqual('保存', btn_title, msg=menu3+'新建记录检验不通过')              
     
    def test_tab_list_delete_row_case(self):
        '''删除选项卡子记录'''  
    
        menu3 = '选项卡_父子关系视图及重计算'
        self.open_menu3(menu3)
        #切换到另外的页签
        tab_name = '非父子视图'
        tabpage = TabPage(self.driver,tab_name)
        tabpage.tab_switch() 
        tab_view = TabListViewPage(self.driver)
        before_num=tab_view.get_tab_list_record_total()
        print("before_num=======%s"%before_num)
        tismsg = tab_view.tab_list_delete_row(1)
        after_num=tab_view.get_tab_list_record_total()
        print("after_num=======%s"%after_num)
        self.assertNotEqual(before_num, after_num, msg=menu3+'全选删除检验不通过')   
     
     
    def test_tab_reflesh_recalcalate_case(self):
        '''选项卡刷新重计算'''  
        '''输入只读，则列表按钮隐藏，输入隐藏，则第二个视图，隐藏'''
        menu3 = '选项卡_父子关系视图及重计算'
        self.open_menu3(menu3)
        #切换到另外的页签
        tab_name = '非父子视图'
        tabpage = TabPage(self.driver,tab_name)
        tabpage.tab_switch() 
        #验证只读时，列表视图的按钮是否可见
        input_page = InputPage(self.driver,"重计算")
        input_page.send_keys_get_value("只读")
        input_page.switch_key()      
           
        btn = ButtonPage(self.driver)
        btn_title =  btn.get_tab_list_button_by_title("新建")
        self.assertNotEqual('新建',btn_title,msg='选项卡列表只读检验不通过')
          
        #网格视图是在iframe下
        input_page.send_keys_get_value("隐藏")
        input_page.switch_key() 
        tabpage2 = TabPage(self.driver,tab_name).find_tab_by_title()             
        self.assertFalse(tabpage2.is_displayed(), msg='选项卡列表隐藏检验不通过')              
   
    def test_collapse_openall_case(self):
        '''选项卡折叠视图全部展开'''
        menu3 = '选项卡_折叠_是否全部展开_是'
        self.open_menu3(menu3) 
        tabpage = TabPage(self.driver)
        compname1 = tabpage.get_tab_item_by_name("选项卡_页签1_文本一")
        self.assertTrue(compname1.is_displayed(), msg=menu3+'选项卡折叠视图全部展开检验不通过') 
        compname2 = tabpage.get_tab_item_by_name("选项卡_页签2_文本一")
        self.assertTrue(compname2.is_displayed(), msg=menu3+'选项卡折叠视图全部展开检验不通过')                           
        compname3 = tabpage.get_tab_item_by_name("选项卡_页签3_文本一")
        self.assertTrue(compname3.is_displayed(), msg=menu3+'选项卡折叠视图全部展开检验不通过')            
   
    def test_collapse_hide_open_case(self):
        '''选项卡折叠视图收起展开'''
        menu3 = '选项卡_折叠_全部展开_否'
        self.open_menu3(menu3) 
        tabpage = TabPage(self.driver)
        compname1 = tabpage.get_tab_item_by_name("选项卡_页签1_文本一")
        self.assertTrue(compname1.is_displayed(), msg=menu3+'选项卡折叠视图收起展开检验不通过') 
        #第二个折叠视图默认收起
        compname2 = tabpage.get_tab_item_by_name("选项卡_页签2_文本一")
        self.assertFalse(compname2.is_displayed(), msg=menu3+'选项卡折叠视图收起检验不通过')                           
        #展开第二个折叠项
        tabpage.click_tab_collapse('2')
        #折叠视图展开，判断是否可以显示
        compname3 = tabpage.get_tab_item_by_name("选项卡_页签2_文本一")
        self.assertTrue(compname3.is_displayed(), msg=menu3+'选项卡折叠视图展开检验不通过')              
    
    def test_collapse_readOnly_case(self):
        '''选项卡折叠视图刷新只读'''
        menu3 = '选项卡_折叠重计算'
        self.open_menu3(menu3) 
        tabpage = TabPage(self.driver)
        #验证只读时，列表视图的按钮是否可见
        input_page = InputPage(self.driver,"重计算")
        input_page.send_keys_get_value("只读")
        input_page.switch_key()      
#     #有bug，暂时无法测试
#         comp = InputPage(self.driver, "选项卡_页签1_文本一")
#         self.assertTrue(comp.readonly_test(), msg='选项卡下表单只读检验不通过')
                    
        btn = ButtonPage(self.driver)
        btn_title =  btn.get_gridview_button(btn.new_btn)
        self.assertNotEqual('新建',btn_title,msg='选项卡折叠网格视图只读检验不通过')            
        btn_title =  btn.get_tab_list_button_by_title("新建")
        self.assertNotEqual('新建',btn_title,msg='选项卡折叠视图只读检验不通过')
   
   
    def test_collapse_hide_case(self):
        '''选项卡折叠视图刷新隐藏'''
        menu3 = '选项卡_折叠重计算'
        self.open_menu3(menu3) 
        tabpage = TabPage(self.driver)
        #验证只读时，列表视图的按钮是否可见
        input_page = InputPage(self.driver,"重计算")
        input_page.send_keys_trigger_refresh("隐藏")
        tabpage = TabPage(self.driver)
        #展开第二个折叠项
        collapse=['1','2','3']
        for collapseone in collapse:           
            collapse1 = tabpage.find_tab_collapse(collapseone)
            dispaly = collapse1.get_attribute("style")
            self.assertIn("display: none;",dispaly,msg=collapseone+'选项卡折叠刷新隐藏检验不通过')   
             
    def test_collapse_addrow_case(self):
        '''选项卡折叠方式增加网格视图记录'''
        #判断切换后的字段是否可见
        mp = MainPage(self.driver)        
        #time.sleep(0.5)
        menu3 = '选项卡_父子关系视图及重计算'
        self.open_menu3(menu3)        
        #网格视图是在iframe下
        mp.switch_to_grid_iframe()        
        grid_view = GridViewPage(self.driver)
        before_num=grid_view.get_grid_rows_total()
        print("before_num=======%s"%before_num)
        grid_view.add_one_row()
        after_num=grid_view.get_grid_rows_total()
        self.assertNotEqual(before_num, after_num, msg=menu3+'新建记录检验不通过') 
   
    def test_collapse_cancel_grid_case(self):
        '''选项卡折叠方式网格视图取消所有'''
        #判断切换后的字段是否可见
        mp = MainPage(self.driver)       
        #time.sleep(0.5)
        menu3 = '选项卡_父子关系视图及重计算'
        self.open_menu3(menu3)        
        #网格视图是在iframe下
        mp.switch_to_grid_iframe()        
        grid_view = GridViewPage(self.driver)
        before_num=grid_view.get_grid_rows_total()
        print("before_num=======%s"%before_num)
        grid_view.cancel_all_operation()
        after_num=grid_view.get_grid_rows_total()
        print("after_num=======%s"%after_num)
        self.assertEqual(before_num, after_num, msg=menu3+'取消所有按钮检验不通过') 
   
    def test_collapse_delete_grid_case(self):
        '''网格视图删除一个记录'''
        #判断切换后的字段是否可见
        mp = MainPage(self.driver)
        menu3 = '选项卡_父子关系视图及重计算'
        self.open_menu3(menu3)        
        #网格视图是在iframe下
        mp.switch_to_grid_iframe()        
        grid_view = GridViewPage(self.driver)
        if grid_view.get_grid_rows_total() == 0:
            grid_view.add_one_row()
            #time.sleep(0.5)
            print("录入数据了====")
        before_num=grid_view.get_grid_rows_total()
        print("before_num=======%s"%before_num)
        grid_view.delete_grid_rows(1)
        after_num=grid_view.get_grid_rows_total()
        print("after_num=======%s"%after_num)
        self.assertNotEqual(before_num, after_num, msg=menu3+'删除记录检验不通过')   
   
      
    def test_collapse_list_addrow_case(self):
        '''新建选项卡折叠方式列表记录'''  
        mp = MainPage(self.driver)
        menu3 = '选项卡_折叠重计算'
        self.open_menu3(menu3)
        #切换到另外的页签      
        tab_view = TabListViewPage(self.driver)
        btn_title = tab_view.tab_list_add_row()
        self.assertEqual('保存', btn_title, msg=menu3+'折叠方式列表新建记录检验不通过')  
     
    def test_collapse_list_delete_row_case(self):
        '''删除选项卡折叠方式列表记录'''  
     
        menu3 = '选项卡_折叠重计算'
        self.open_menu3(menu3)
        #切换到另外的页签
        tab_view = TabListViewPage(self.driver)
        before_num=tab_view.get_tab_list_record_total()
        print("before_num=======%s"%before_num)
        tismsg = tab_view.tab_list_delete_row(1)
        after_num=tab_view.get_tab_list_record_total()
        print("after_num=======%s"%after_num)
        self.assertNotEqual(before_num, after_num, msg=menu3+'折叠方式列表删除检验不通过')  
                                                                                                                                                                                                                                 
    def init(self):
        
#         self.test_tab_switch_case()
#         self.test_tab_save_case()         
#         self.test_tab_readonly_case()
#         self.test_tab_hide_case()  
#         self.test_tab_selected_case() 
#         self.test_tab_add_grid_case() 
#         self.test_tab_cancel_grid_case() 
#         self.test_tab_delete_grid_case()         
#         self.test_tab_delete_all_grid_case()         
#         self.test_tab_list_addrow_case()
#         self.test_tab_list_delete_row_case()
#         self.test_tab_reflesh_recalcalate_case()   
#         self.test_collapse_openall_case()
#         self.test_collapse_hide_open_case() 
#         self.test_collapse_readOnly_case()
#         self.test_collapse_readOnly_case() 
        self.test_collapse_hide_case()  
#         self.test_collapse_addrow_case()    
#         self.test_collapse_cancel_grid_case()  
#         self.test_collapse_delete_grid_case()  
#         self.test_collapse_list_addrow_case() 
#         self.test_collapse_list_delete_row_case()   
               
    def setUp(self):
        mp = MainPage(self.driver)
        mp.refresh_main()
        if self.menu1 != '':
            mp.open_menu(self.menu1)
        #time.sleep(0.3)
        
        if self.menu2 != '':
            mp.open_menu(self.menu2)
        #time.sleep(0.3)
                   
    def scroll_to(self, y):
        '''执行js脚本，操作滚动条滚动到离页面顶部y值的位置'''
        script = 'var $con = $("#_contentTable");if($con.size()>0)$con.getNiceScroll(0).doScrollTop('+y+',10)' #滚动到控件可以看到后面的代码执行才不会报错
        self.driver.execute_script(script)
        time.sleep(0.1) #必须
    
if __name__ == '__main__':
    unittest.main()