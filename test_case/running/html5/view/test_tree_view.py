import os,sys
sys.path.append('../../../../')
import time
import unittest
from test_case.running.html5.view.view_test import ViewTest
from test_case.page_obj.button_page import ButtonPage
from test_case.page_obj.main_page import MainPage
from test_case.page_obj.view.tree_view_page import TreeViewPage


class TreeViewTest(ViewTest):
    '''树形视图测试'''

    menu1 = '视图'
    menu2 = '树形视图'

    def open_menu3(self, menu3):
        mp = MainPage(self.driver)
        mp.open_menu(menu3)
        #time.sleep(0.3)
        mp.switch_to_iframe()
        mp.wait_loading_hide()

    def test_viewtype_foldopen(self):
        '''树形视图-视图类型--折叠打开'''
        menu3 = '树形视图_视图类型'
        self.open_menu3(menu3)

        tp = TreeViewPage(self.driver)
        tp.view_open()
        time.sleep(0.5) #必须
        self.assertTrue(tp.get_view_open_return(),msg='树形视图-视图类型-一级打开校验不通过')
        tp.view_open()
        time.sleep(0.5) #必须
        self.assertTrue(tp.get_view_open_return(), msg='树形视图-视图类型-二级打开校验不通过')
        tp.view_fold1()
        time.sleep(0.5) #必须
        self.assertTrue(tp.get_view_fold_return(), msg='树形视图-视图类型-二级折叠校验不通过')
        tp.view_fold2()
        time.sleep(0.5) #必须
        self.assertTrue(tp.get_view_fold_return(), msg='树形视图-视图类型-一级折叠校验不通过')

    def test_creat_leaf_data(self):
        '''树形视图-视图类型--创建数据'''
        menu3 = '树形视图_视图类型'
        self.open_menu3(menu3)

        tp = TreeViewPage(self.driver)
        tp.view_open() #展开顶级节点
        tp.wait_tree_view_loading_show_then_hide()
        tp.creat_leaf()
        self.assertTrue(tp.get_creat_leaf_data_return(),msg='树形视图-视图类型-创建数据校验不通过')

    def test_search_value(self):
        '''树形视图-视图类型--查询值'''
        menu3 = '树形视图_视图类型'
        self.open_menu3(menu3)

        tp = TreeViewPage(self.driver)
        tp.search_value()
        self.assertTrue(tp.get_search_value_return(),msg='树形视图-视图类型-查询值校验不通过')

    def test_check_quantity(self):
        '''树形视图-视图类型--树形菜单对应数目'''
        menu3 = '树形视图_视图类型'
        self.open_menu3(menu3)
        tp = TreeViewPage(self.driver)
        self.assertTrue(tp.check_quantity(),msg='树形视图-视图类型--树形菜单对应数目校验不通过')

    def test_form_type(self):
        '''树形视图-表单类型'''
        menu3 = '树形视图_表单类型'
        self.open_menu3(menu3)

        tp = TreeViewPage(self.driver)
        self.assertTrue(tp.form_type(), msg='树形视图-表单类型校验不通过')

    def test_linktype_customlink_inner(self):
        '''树形视图_链接类型_自定义链接内部'''
        menu3 = '树形视图_链接类型_自定义链接内部'
        self.open_menu3(menu3)

        tp = TreeViewPage(self.driver)
        self.assertTrue(tp.link_type_customlink_inner(),msg='树形视图_链接类型_自定义链接内部校验不通过')

    def test_linktype_custom_reports(self):
        '''树形视图_链接类型_自定义报表'''
        menu3 = '树形视图_链接类型_自定义报表'
        self.open_menu3(menu3)

        tp = TreeViewPage(self.driver)
        self.assertTrue(tp.link_type_custom_reports(),msg='树形视图_链接类型_自定义报表校验不通过')


    def init(self):
        self.test_viewtype_foldopen()
        # self.test_creat_leaf_data()
        # self.test_search_value()
        # self.test_check_quantity()
        # self.test_form_type()
        # self.test_linktype_customlink_inner()
#         self.test_linktype_custom_reports()

if __name__ == '__main__':
    unittest.main()
