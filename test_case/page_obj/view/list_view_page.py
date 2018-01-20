import os,sys
sys.path.append('../../../')
import time
from test_case.page_obj.view.view_page import ViewPage
from test_case.page_obj.main_page import MainPage
from test_case.page_obj.button_page  import ButtonPage
from test_case.page_obj.button_page  import ButtonPhonePage
from test_case.page_obj.form.input_page import InputPage
from test_case.page_obj.form.input_page import InputPhonePage
from test_case.page_obj.page  import PhonePage


class ListViewPage(ViewPage):
    '''列表视图'''

    def get_rows_total(self):
        '''获取当前页显示的数据行数量'''
        elems = self.find_elems('.listDataTrFirstTd',timeout=2)
        if elems == None:
            return 0
        else:
            return len(elems)
    
    def click_row(self):
        '''点击第一行数据'''
        self.find_elem_is_clickable('.listDataTr>.listDataTrTd').click()
        self.wait_loading_hide() #等待表单页面的loading加载完
        self.wait_elem_visible('.formActBtn')#等待按钮操作栏显示
    
    def get_column_head(self, column_name):
        '''根据列名称获取列头'''
        return self.find_elem('#viewHtml tr.listDataTh td[title="'+column_name+'"]')

    
    def get_column_head_width(self, column_name):
        '''根据列名称获取列头宽度'''
        return self.get_column_head(column_name).get_attribute('width')
    
    def get_column_sort_img_src(self, column_name):
        '''获取排序字段图片的src属性值'''
        try:
            return self.find_elem('#viewHtml tr.listDataTh td[title="'+column_name+'"] img').get_attribute('src')
        except Exception as ex:
            print('获取排序字段图片的src属性值异常：%s' %ex)
        
    def get_column_row1_col1_img(self):
        '''获取类型脚本输出的值'''
        return self.find_elem('#viewHtml tbody tr.listDataTr td.listDataTrTd img').get_attribute('src')
    
    def get_column_row1_col1_font(self):
        '''获取类型脚本输出的值'''
        return self.find_elem('#viewHtml tbody tr.listDataTr td.listDataTrTd font').get_attribute('color')
    
    def get_collect(self):
        '''获取汇总文本'''
        try:
            return self.find_elem('table#dataTable > tbody tr.listDataTr:nth-last-child(1) td:nth-child(2)').text
        except Exception as ex:
            print('获取汇总文本异常：%s' %ex)
    
    def get_column_button(self, val):
        '''获取列表中的操作按钮'''
        return self.find_elem('#dataTable > tbody > tr.listDataTr input[type="button"][value="'+val+'"]')
        
    def click_jump(self):
        '''点击列表跳转类型的操作按钮'''
        self.get_column_button('跳转').click()
    
    def get_table_caption(self):
        '''获取case001表格的表头'''
        try:
            return self.find_elem('#_formHtml > table > caption').text
        except Exception as ex:
            print('获取case001表格的表头异常：%s' %ex)
    
    def add_one_row(self):
        '''新建一条数据'''
        bp = ButtonPage(self.driver)
        bp.click_button(bp.new_btn)
        bp.wait_Tabloading_show_then_hide()
        ip = InputPage(self.driver, '列表视图_单行文本框')
        ip.element.send_keys(20)
        bp.click_button(bp.save_start)  #点击流程启动按钮
        bp.wait_Tabloading_show_then_hide()
        bp.click_button(bp.to_return)   #点击返回按钮
        bp.wait_loading_hide()  #表单中
        
    def add_one_row2(self):
        '''新建一条数据'''
        bp = ButtonPage(self.driver)
        bp.click_button(bp.new_btn)
        bp.wait_loading_hide()
        ip = InputPage(self.driver, '单行文本')
        ip.element.send_keys('保存')
        bp.click_button(bp.save)
        ip.wait_loading_hide()
        bp.click_button(bp.to_return)
        ip.wait_loading_hide()  #表单中
        
    def add_one_row_div(self):
        '''在弹出层中新建一条记录'''
        bp = ButtonPage(self.driver)
        bp.click_button(bp.new_btn)
        mp = MainPage(self.driver)
        mp.wait_Tabloading_show_then_hide()
        mp.switch_to_div_iframe()
        ip = InputPage(self.driver, '单行文本')
        ip.element.send_keys('保存')
        bp.click_button(bp.save)
        mp.wait_Tabloading_show_then_hide()
        bp.click_button(bp.to_return)
        mp.wait_loading_hide()  #表单中
        mp.switch_to_iframe()
    
    def click_del(self):
        '''点击列表删除类型的操作按钮'''
        self.get_column_button('删除').click()
        self.wait_alert_show()
        self.click_alert_dismiss()
        self.wait_alert_dispaly()
        self.get_column_button('删除').click()
        self.wait_alert_show()
        self.click_alert_accept()
        
    def click_submit(self):
        '''点击列表提交流程类型按钮'''
        self.get_column_button('提交流程').click()
    
    def set_val_and_submit(self, val):
        '''设置提交审批意见并确定提交'''
        self.find_elem('.aui_content textarea').send_keys(val)
        self.find_elem_is_clickable('.aui_state_highlight').click() #点击确认按钮
    
    def click_module_btn(self):
        '''点击列表以模板表单方式打开类型按钮'''
        self.get_column_button('以模板表单方式打开').click()
    
    def get_column_row1_col1_backgroundcolor(self):
        '''获取列背景颜色'''
        try:
            return self.find_elem('#viewHtml tbody tr.listDataTr td.listDataTrTd').value_of_css_property('background-color')
        except Exception as ex:
            print('获取列背景颜色异常：%s' %ex)
            return ''
    
    def get_column_row1_col1_color(self):
        '''获取列颜色'''
        try:
            return self.find_elem('#viewHtml tbody tr.listDataTr td.listDataTrTd > a').value_of_css_property('color')
        except Exception as ex:
            print('获取列颜色异常：%s' %ex)
            return ''
        
    def get_column_row1_col1_fontsize(self):
        '''获取列字体大小'''
        try:
            return self.find_elem('#viewHtml tbody tr.listDataTr td.listDataTrTd > a').value_of_css_property('font-size')
        except Exception as ex:
            print('获取列字体大小异常：%s' %ex)
            return ''
    
    def get_column_row1_col1_title(self):
        '''获取提示文字'''
        try:
            return self.find_elem('#viewHtml tbody tr.listDataTr td.listDataTrTd > a').get_attribute('title')
        except Exception as ex:
            print('获取提示文字异常：%s' %ex)
            return ''
    
    def open_fisrt_doc(self):
        '''打开第一个记录'''
        action = self.find_elem_is_clickable('table#dataTable tbody>tr').click()
        self.wait_Tabloading_show_then_hide() #等待表单加载
    
    def clear_all_data(self):
        '''清空所有数据'''
        bp = ButtonPage(self.driver)
        bp.click_button(bp.clear_btn)
        self.click_alert_accept()
        self.wait_loading_hide()
        if self.get_rows_total()!=0:
            print("清空所有数据失效")
        
    def get_head_td1_text(self):
        '''获取视图首列列头的text'''
        try:
            return self.find_elem('#viewHtml thead tr.listDataTh td.listDataThTd>a').text
        except Exception as ex:
            print('获取视图首列列头的text异常%s' %ex)
            return ''
    
    def get_print_table_head_td1_text(self):
        '''获取打印视图首列列头的text'''
        try:
            return self.find_elem('table#dataTable tr.listDataTh td.listDataThTd').text
        except Exception as ex:
            print('获取打印视图首列列头的text异常%s' %ex)
            return ''
        
    def judge_delete(self, name):
        """判断是否已存在记录有则删除"""
        s = self.driver.find_elements_by_link_text(name)
        if len(s) >= 1:
            print("记录已存在，需要删除")
            self.find_elem_is_clickable('td.listDataThFirstTd > input[type="checkbox"]').click() #点击全选
            btn = ButtonPage(self.driver)
            btn.click_button(btn.del_btn)
            self.driver.switch_to_alert().accept()
            self.wait_loading_hide()
            self.wait_elem_visible('.content-space-txt.text-center') #判断数据已经删除完
        else:
            print("记录不存在，不需要删除")

    def delete_record(self):
        #删除记录
        self.find_elem_is_clickable('td.listDataThFirstTd > input[type="checkbox"]').click()
        btn = ButtonPage(self.driver)
        btn.click_button(btn.del_btn)
        self.driver.switch_to_alert().accept()
        self.wait_loading_hide()


class TabListViewPage(ListViewPage):
     
    def click_tab_list_rows(self):
        '''获取第一个复选框'''
        return self.find_elems('table#dataTable> tbody input[name="_selects"]')

    def click_tab_list_all_rows(self):
        '''获取全选复选框'''
        return self.find_elems('tbody#dataTable td.listDataThFirstTd')

    def tab_list_add_row(self):
        btn = ButtonPage(self.driver)
        btn_title = btn.get_tab_list_button(btn.new_btn).get_attribute('title')

        #点击新建按钮
        btn.click_tab_list_button(btn.new_btn)
        #time.sleep(0.5)
        #切换到弹出层打开的页面
        mp = MainPage(self.driver)        
        mp.switch_to_div_iframe()
        #time.sleep(0.5)
        btn_title = btn.get_button_title(btn.save)
        btn.click_button(btn.save)
        btn.wait_loading_hide()
        return btn_title            

    
    def tab_list_delete_row(self,num):
        '''选项卡点击列表删除类型的操作按钮'''
        '''删除记录数，1或者当前显示数'''
        checkboxs = self.click_tab_list_rows()
        print("checkboxs=====%s"%checkboxs)
        if checkboxs:
            if num == 1:
                checkboxs[0].click()
 
            else:
                 for checkbox in checkboxs:
                     checkbox.click() 
                   
                      
            bp = ButtonPage(self.driver)
            bp.click_tab_list_button(bp.del_btn)
            #time.sleep(0.5)
            self.click_alert_dismiss()
            #time.sleep(0.5)
            bp.wait_loading_hide()
            bp.click_tab_list_button(bp.del_btn)
            #time.sleep(0.5)
            tismsg = self.get_alert_text() 
            self.click_alert_accept()
            self.wait_loading_hide()
            #time.sleep(0.5)
            return tismsg
        
    def get_tab_list_record_total(self):
        '''获取视图记录总数'''
        try:
            return self.find_elem('div#acttable ul > div:nth-child(2) > span').text
        except Exception as ex:
            print('获取视图记录总数' %ex)
            return ''

    
    
class ListViewPhonePage(PhonePage):
    
    def get_pagination_body(self):
        '''获取分页dom元素'''
        try:
            return self.find_elem('#footer .pagination').text
        except Exception as ex:
            print('获取分页文本异常，该视图无数：%s' %ex)
    
    def get_rows_total(self):
        '''获取当前页显示的数据行数量'''
        if self.find_elements('.listDataTr') != None:
            return len(self.find_elements('.listDataTr'))
        else:
            return 0

    def clear_all_data(self):
        '''清空所有数据'''
        #获取打开表单的列表，点击所有checkbox
        lis = self.find_elements('.listDataTrFirstTd input')
        self.wait_elem_disappear('.weui_mask_transparent')
        if lis!=None and len(lis)>0:
            for li in lis:
                li.click()
            #点击删除按钮
            bt = ButtonPhonePage(self.driver)
            bt.click_button('删除')
            #点击确定
            self.click_alert_accept()
            self.wait_loading_hide()
            time.sleep(0.5)

    def open_fisrt_doc(self):
        '''打开第一个记录'''
        self.wait_elem_show_then_hide('.weui_loading_toast')
        self.wait_elem_show_then_hide('.weui_mask_transparent')
        self.wait_elem_show_then_hide('#msg')
        self.find_element('.listDataTrTd').click()

    def get_column_row1_col2(self):
        '''获取首行第二列的值'''
        time.sleep(0.5)
        result = self.find_element('.listDataTrTd')
        return result.text

    def open_doc_by_title(self,title):
        '''根据记录值打开记录'''
        self.wait_elem_disappear('.weui_mask_transparent')
        locator = 'td[title="' + title + '"]'
        self.find_elem(locator).click()

    def get_column_head(self, column_name):
        '''根据列名称获取列头'''
        try:
            return self.find_element('#listView tr.listDataTh th[title="'+column_name+'"]')
        except Exception as ex:
            print('根据列名称获取列头异常：%s' %ex)
    
    def get_column_row1_col1(self):
        '''获取首行首列的值'''
        return self.find_element('#listView tbody tr.listDataTr td.listDataTrTd').text

    def get_column_sort_img_src(self, column_name):
        '''获取排序字段图片的src属性值'''
        try:
            return self.find_element('#listView tr.listDataTh th[title="'+column_name+'"] img').get_attribute('src')
        except Exception as ex:
            print('获取排序字段图片的src属性值异常：%s' %ex)
        
    def get_column_row1_col1_img(self):
        '''获取类型脚本输出的值'''
        return self.find_element('#listView tbody tr.listDataTr td.listDataTrTd img').get_attribute('src')
    
    def get_column_row1_col1_font(self):
        '''获取类型脚本输出的值'''
        return self.find_element('#listView tbody tr.listDataTr td.listDataTrTd font').get_attribute('color')
    
    def is_column_head_hide(self, column_name):
        '''根据列名称判断列头是否隐藏'''
        try:
            return self.find_element('#listView tr.listDataTh th[title="'+column_name+'"]').is_displayed()
        except Exception as ex:
            print('根据列名称获取列头异常：%s' %ex)
            return False
    
    def get_column_button(self, val):
        '''获取列表中的操作按钮'''
        return self.find_element('#listView tbody > tr.listDataTr input[type="button"][value="'+val+'"]')
        
    def click_jump(self):
        '''点击列表跳转类型的操作按钮'''
        self.get_column_button('跳转').click()        
    
    def click_confirm_accept(self):
        '''弹出确定框点击确认'''
        self.find_elem('#confirmPanel a.btn-delete').click()
        
    def click_confirm_dismiss(self):
        '''弹出确定框点击取消'''
        self.find_elem('#confirmPanel a.btn-cancel').click()

    def set_confirm_val(self, val):
        self.find_elem('#confirmPanel [name="temp_remark"]').send_keys(val)

    def click_del(self):
        '''点击列表删除类型的操作按钮'''
        self.get_column_button('删除').click()
        self.click_confirm_dismiss()
        self.wait_Tabloading_show_then_hide()
        self.get_column_button('删除').click()
        self.click_confirm_accept()
    
    def add_one_row(self):
        '''新建一条数据'''
        bp = ButtonPhonePage(self.driver)
        bp.click_button('新建')
        self.wait_Tabloading_show_then_hide()
        ip = InputPhonePage(self.driver, '列表视图_单行文本框')
        ip.element.send_keys(20)
        bp.click_button('保存')
        self.wait_Tabloading_show_then_hide()
        self.wait_msg_show_then_hide()
        bp.click_button('返回')
    
    def click_submit(self):
        '''点击列表提交流程类型按钮'''
        self.get_column_button('提交流程').click()
    
    def set_val_and_submit(self, val):
        '''设置提交审批意见并确定提交'''
        self.set_confirm_val(val)
        self.click_confirm_accept()
    
    def click_module_btn(self):
        '''点击列表以模板表单方式打开类型按钮'''
        self.get_column_button('以模板表单方式打开').click()
    
    def click_prev_page(self):
        '''点击前一页'''
        try:
            self.find_element('#footer span[title="上一页"]').click()
        except Exception as ex:
            print('视图翻页点击前一页异常：%s' %ex)
        
    def click_next_page(self):
        '''点击下一页'''
        try:
            self.find_element('#footer span[title="下一页"]').click()
        except Exception as ex:
            print('视图翻页点击下一页异常：%s' %ex)
        
    def click_first_page(self):
        '''点击首页'''
        try:
            self.find_element('#footer span[title="首页"]').click()
        except Exception as ex:
            print('视图翻页点击首页异常：%s' %ex)
        
    def click_end_page(self):
        '''点击末页'''
        try:
            self.find_element('#footer span[title="末页"]').click()
        except Exception as ex:
            print('视图翻页点击末页异常：%s' %ex)
    
    def click_td_menu(self):
        '''点击列设置图标'''
        self.find_element('.tdMenu').click()
    
    def cancel_all_td(self):
        '''取消所有列的显示'''
        checkboxs = self.find_elements('.tableList-menu-container .ui-checkbox input[type="checkbox"]')
        for checkbox in checkboxs:
            if checkbox.is_selected() == True:
                checkbox.click()
    
    def hide_td_menus(self):
        '''点击隐藏选择列的菜单'''
        self.find_element('.tableList-screen').click()
    
    def check_td_by_title(self, title):
        '''根据列显示值设置要显示的列'''
        divs = self.find_elements('.tableList-menu-container .ui-checkbox')
        for div in divs:
            if div.text == title:
                div.find_element_by_css_selector('input[type="checkbox"]').click()
    
    def set_td_by_title(self, title):
        '''根据列头title选择显示的列'''
        self.click_td_menu()
        self.cancel_all_td()
        self.check_td_by_title(title)
        self.hide_td_menus()
        
    