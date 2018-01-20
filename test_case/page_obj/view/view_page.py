import os,sys
import time
sys.path.append('../../../')
from test_case.page_obj.page  import Page
from test_case.page_obj.button_page import ButtonPage


class ViewPage(Page):
    '''视图'''
    
    def view_scroll_to(self, y):
        '''列表和日历视图滚动条定位'''
        script = 'var $con = $("body");if($con.size()>0)$con.getNiceScroll(0).doScrollTop('+y+',10)' #滚动到控件可以看到后面的代码执行才不会报错
        self.driver.execute_script(script)
        #time.sleep(0.5)
    
    def get_select_all(self):
        '''获取全选按钮'''
        try:
            return self.find_elem('#viewHtml .table-head .listDataThFirstTd input[type="checkbox"]')
        except Exception as ex:
            print('获取全选框异常：%s' %ex)
    
    def click_select_all(self):
        '''点击全选'''
        select_all = self.get_select_all()
        select_all.click()

    def check_select_all(self):
        '''点击全选并验证是否选中或未选中'''
        select_all = self.get_select_all()
        select_all.click()
        selects = self.find_elems('#viewHtml .table-body input[name="_selects"]')
        for select in selects:
            if select.is_selected()==select_all.is_selected():
                pass
            else:
                return False
        return True
    
    def click_cur_page(self):
        try:
            self.find_elem('#pagination-panel span.current:nth-child(2)').click()
        except Exception as ex:
            print('视图翻页点击当前页异常：%s' %ex)
        
    def click_second_page(self):
        try:
            self.find_elem('#pagination-panel a:nth-child(3)').click()
        except Exception as ex:
            print('视图翻页点击第二页异常：%s' %ex)
        
    def click_prev_page(self):
        try:
            self.find_elem('#pagination-panel .prev').click()
        except Exception as ex:
            print('视图翻页点击前一页异常：%s' %ex)
        
    def click_next_page(self):
        try:
            self.find_elem('#pagination-panel .next').click()
        except Exception as ex:
            print('视图翻页点击下一页异常：%s' %ex)
        
    def is_show_watermark(self):
        '''是否显示水印'''
        try:
            image = self.find_elem('body').value_of_css_property('background-image')
            return(image != 'none')
        except Exception as ex:
            return False
    
    def get_style_lib(self):
        '''返回样式库内容'''
        styles = self.find_elems('style')
        for iter in styles:
            return iter.get_attribute('innerText')
    
    def get_record_total(self):
        '''获取视图记录总数'''
        try:
            return self.find_elem('.totalRowPanel').text
        except Exception as ex:
            print('获取视图记录总数' %ex)
            return ''
    
    def get_pagination_body(self):
        '''获取分页dom元素'''
        try:
            return self.find_elem('#pagination-panel .pagination-body').text
        except Exception as ex:
            print('获取分页文本异常，该视图无数：%s' %ex)
            return False
    
    def get_column_row1_col1(self):
        '''获取首行首列的值'''
        return self.find_elem_visible('#viewHtml tbody tr.listDataTr td.listDataTrTd').text


    def delete_all_data(self):
        '''删除所有数据'''
        bp = ButtonPage(self.driver)
        self.find_elem('.listDataThFirstTd').click()
        bp.click_button(bp.del_btn)
        self.click_alert_accept()
        bp.wait_Tabloading_show_then_hide()  # 等待loading消失
        bp.wait_elem_visible('.content-space-txt.text-center') #判断数据已经删除完