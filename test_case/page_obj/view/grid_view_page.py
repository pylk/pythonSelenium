import os,sys
sys.path.append('../../../')
import time
from test_case.page_obj.main_page import MainPage
from test_case.page_obj.button_page  import ButtonPage
from test_case.page_obj.form.input_page import InputPage
from test_case.page_obj.view.view_page import ViewPage


class GridViewPage(ViewPage):
    '''网格视图'''
    
    def add_one_row(self):
        bp = ButtonPage(self.driver)
        bp.click_gridview_button(bp.new_btn)
        bp.wait_loading_hide()
        #time.sleep(0.5)
        ip = InputPage(self.driver, '网格视图_数字')
        ip.element.send_keys("1000123.46")
        bp.get_gridview_defaultbutton('保存')
        bp.wait_loading_hide()
        #time.sleep(0.5)

    def cancel_all_operation(self):
        '''点击新建，再点【取消所有】'''
        bp = ButtonPage(self.driver)
        bp.click_gridview_button(bp.new_btn)
        bp.wait_loading_hide()
        #time.sleep(0.5)        
        bp.click_gridview_defaultbutton("取消所有")
        #time.sleep(0.5)
   
    def click_grid_rows(self):
        '''获取第一页复选框'''
        return self.find_elems('tbody#obpm-view__table input[name="_selects"]')

    def click_grid_all_rows(self):
        '''全选'''
        self.find_elem('div#gridView__box td[data-id="selectAll"]').click()
    
    def delete_grid_all_rows(self):
        '''删除全选记录'''
        self.click_grid_all_rows()
        bp = ButtonPage(self.driver)
        bp.click_gridview_button(bp.del_btn)
        #time.sleep(0.5)
        self.click_alert_dismiss()
        #time.sleep(0.5)
        bp.click_gridview_button(bp.del_btn)
        #time.sleep(0.5)
        self.click_alert_accept() 
        self.wait_loading_hide()
        #time.sleep(0.5)
            

    def delete_grid_rows(self,num):
        '''删除记录数，1或者当前显示数'''
        checkboxs = self.click_grid_rows()
        print("checkboxs======%s"%checkboxs)
        if checkboxs:
            if num == 1:
                checkboxs[0].click()

            else:
                 for checkbox in checkboxs:
                     checkbox.click()
                        
            bp = ButtonPage(self.driver)
            bp.click_gridview_button(bp.del_btn)
            #time.sleep(0.5)
            self.click_alert_dismiss()
            #time.sleep(0.5)
            self.wait_loading_hide()
            bp.click_gridview_button(bp.del_btn)
            #time.sleep(0.5)
            self.click_alert_accept() 
            self.wait_loading_hide()
            #time.sleep(0.5)
    
     
    def get_grid_rows_total(self):
        '''获取当前页显示的数据行数量'''
        elems = self.find_elems('tbody#obpm-view__table input[name="_selects"]')
        if elems == None:
            return 0
        else:
            return len(elems)

    def get_grid_column_head(self, column_name):
        '''根据列名称获取列头'''
        return self.find_elem_visible('div#gridView__box td[colname="'+column_name+'"]')

    def get_grid_column_head_by_coltext(self,coltext):
        '''根据多语言标签获取列头'''
        return self.find_elem_visible('td[coltext="' + coltext + '"]')

    
    def get_grid_column_head_width(self, column_name):
        '''根据列名称获取列头宽度'''
        return self.get_grid_column_head(column_name).get_attribute('data-width')

    def get_grid_column_one(self):
        '''第一列的值'''
        return self.find_elem('tbody#obpm-view__table td.obpm-isedit')

    def get_grid_column_row1_col1(self):
        '''第一列的值'''
        return self.get_grid_column_one().text

    def get_grid_column_row1_coln(self,num):
        '''第n列的值'''
        return self.find_elem('tbody#obpm-view__table tr>td:nth-child('+num+')')
        
    def get_grid_column_row1_coln_text(self,num):
        '''第n列的值'''
        return self.find_elem('tbody#obpm-view__table tr>td:nth-child('+num+')').text

    def get_grid_column_sort_img_src(self, column_name):
        '''获取排序字段class属性值'''
        try:
            return self.find_elem('div#gridView__box td[colname="'+column_name+'"] > i').get_attribute('class')
        except Exception as ex:
            print('获取排序字段class属性值：%s' %ex)        

    def get_grid_collect(self):
        '''获取汇总文本'''
        try:
            return self.find_elem('tbody#obpm-view__table tr:nth-last-child(1) td:nth-child(2)').text
        except Exception as ex:
            print('获取汇总文本异常：%s' %ex)        