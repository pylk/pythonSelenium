import os,sys
sys.path.append('../../../')
import re
import time
from .view_page import ViewPage
from test_case.page_obj.button_page  import ButtonPage


class TreeViewPage(ViewPage):
    '''树形视图'''
    
    def switch_to_tree_view_iframe(self):
        '''切换右侧树形视图iframe'''
        tree_iframe = self.find_elem('#viewFrame')
        self.driver.switch_to.frame(tree_iframe)

    def switch_to_parent(self):
        '''退出iframe'''
        self.driver.switch_to.default_content()

    def view_open(self):
        '''视图类型--展开'''
        self.find_elem('.jstree-closed ins').click()

    def view_fold1(self):
        '''视图类型-折叠二级'''
        self.find_elem('.jstree-open .jstree-open ins').click()

    def view_fold2(self):
        '''视图类型-折叠一级'''
        self.find_elem('.jstree-open ins').click()

    def get_view_open_return(self):
        ht = self.find_elem('.jstree-open ul').size
        return ht.get('height') > 0

    def get_view_fold_return(self):
        h = self.find_elem('.jstree-closed ul').location
        return h.get('x') == 0

    def open_leaf(self):
        '''打开无下级二级'''
        self.find_elem('.jstree-leaf').click()

    def Is_lower_exist(self):
        '''判断是否存在下级节点,存在返回Ture,不存在返回False'''
        if self.find_elem('.jstree-leaf') != None:
            return True
        else:
            return False

    def creat_leaf_data(self):
        '''新建数据'''
        # 打开无下级二级
        bp = ButtonPage(self.driver)
        bp.click_button(bp.new_btn)
        bp.wait_Tabloading_show_then_hide()
        self.find_elem('#_formHtml p:nth-child(1) input').send_keys('211')
        self.find_elem('#_formHtml p:nth-child(2) input').send_keys('322')
        self.find_elem('#_formHtml p:nth-child(3) input').send_keys('自动化测试')
        bp.click_button(bp.save)
        bp.wait_Tabloading_show_then_hide()
        bp.click_button(bp.to_return)
        bp.wait_loading_hide()  #表单中
        bp.wait_loading_hide()  #视图中

    def delete_data(self):
        '''清除数据'''
        bp = ButtonPage(self.driver)
        # 打开有下级的二级
        #time.sleep(0.5)
        self.find_elem_is_clickable('.jstree-closed').click()
        # 切换右边iframe
        self.switch_to_tree_view_iframe()
        # 勾选全选
        #time.sleep(0.5)
        self.find_elem_is_clickable('.listDataThFirstTd').click()
        bp.click_button(bp.del_btn)
        self.click_alert_accept()
        bp.wait_loading_hide()

    def get_creat_leaf_data_return(self):
        re = self.find_elem('.listDataTrTd')
        return re.text == '322'

    def creat_leaf(self):
        # 判断是否存在下级，有则删除测试数据，没有则新建数据
        if self.Is_lower_exist() == False:
            self.delete_data()
            self.creat_leaf_data()
        elif self.Is_lower_exist() == True:
            self.open_leaf()
            self.switch_to_tree_view_iframe()
            self.creat_leaf_data()

    def search_value(self):
        '''树形视图-查询值'''
        self.find_elem('.form-control').send_keys('自动化')
        #time.sleep(0.5)
        self.find_elem('.btn-myapp').click()

    def get_search_value_return(self):
        sls = self.find_elems('.jstree-search')
        x = []
        for sl in sls:
            if re.search('自动化', sl.text):
                # print(sl.text)
                x.append(True)
            else:
                x.append(False)
        # print(x)
        return 'False' not in x

    def check_quantity(self):
        '''检查树对应的数量'''
        self.switch_to_tree_view_iframe()
        cq = self.find_elems('.listDataTr')
        x = []
        if len(cq) == 1:
            x.append(True)
        else:
            x.append(False)
        self.switch_to_parent()
        #time.sleep(0.5)
        ifr = self.find_elem("div.tab-pane.active>iframe")
        self.driver.switch_to.frame(ifr)
        #time.sleep(0.5)
        self.find_elem('.jstree-closed a').click()
        self.switch_to_tree_view_iframe()
        if len(cq) == 2:
            x.append(True)
        else:
            x.append(False)
        return 'False' not in x

    def form_type(self):
        '''树形视图-表单类型'''
        self.find_elem('.jstree-closed a').click()
        self.switch_to_tree_view_iframe()
        return self.find_elem('.formTable')

    def link_type_customlink_inner(self):
        '''树形视图-链接类型-自定义链接内部'''
        self.find_elem('.jstree-closed a').click()
        self.switch_to_tree_view_iframe()
        return self.find_elem('#mailForm')

    def link_type_custom_reports(self):
        '''树形视图-链接类型-自定义报表'''
        self.find_elem('.jstree-closed a').click()
        self.switch_to_tree_view_iframe()
        #time.sleep(0.5)
        return self.driver.find_element_by_name('oReport')

    def wait_tree_view_loading_show_then_hide(self):
        '''等待展开节点时的loading消失'''
        self.wait_elem_show_then_hide('.jstree-loading')
