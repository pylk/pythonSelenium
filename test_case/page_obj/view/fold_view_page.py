import os,sys
sys.path.append('../../../')
import time
from .view_page import ViewPage
from test_case.page_obj.main_page import MainPage
from test_case.page_obj.button_page  import ButtonPage
from test_case.page_obj.form.input_page import InputPage


class FoldViewPage(ViewPage):

    def open(self):
        self.find_elem('.folded').click()

    def get_open_return(self):
        return self.find_elem('.FoldDetail .collapsible').text

    def fold(self):
        self.find_elem_is_clickable('.unfolded').click()

    def get_fold_return(self):
        '''获取文件夹返回'''
        if self.find_elem('.unfolded')!=None:
            return True
        else:
            return False


    def get_record_total(self):
        '''获取视图记录总数'''
        try:
            return self.find_elem('#total-row-text').text
        except Exception as ex:
            #print('获取视图记录总数' % ex)
            return ''

    def get_rows_total(self):
        '''获取当前页显示的数据行数量'''
        elems = self.find_elems('table#dataTable > tbody input[name="_selects"]')
        if elems == None:
            return 0
        else:
            return len(elems)

    def click_row(self):
        '''点击第一行数据'''
        self.find_elem('table#dataTable > tbody td.listDataTrTd').click()

    def get_column_head(self, column_name):
        '''根据列名称获取列头'''
        try:
            tname = self.find_elem('.listDataThTd')
            if tname.text == column_name:
                return tname
        except Exception as ex:
            print('根据列名称获取列头异常：%s' % ex)
            return 'none'

    def get_column_head_width(self, column_name):
        '''根据列名称获取列头宽度'''
        return self.get_column_head(column_name).value_of_css_property('width')

    def get_column_head_persent_by_name(self, column_name):
        '''根据列名称获取列头宽度百分比'''
        return  self.get_column_head(column_name).get_attribute('width')

    def get_column_head_persent(self,column_name):
        '''获取列头宽度百分比'''
        ps = self.find_elem('.listDataThTd')
        if ps.text == column_name:
            return ps.get_attribute('style')

    def get_column_row1_col1(self):
        '''获取首行首列的值'''
        return self.find_elem('.folded').text

    def get_row1_col1_valueshowtrue(self):
        '''获取首行首列的值'''
        return self.find_elem('.collapsible').text

    def get_column_sort_img_src(self, column_name):
        '''获取排序字段图片的src属性值'''
        try:
            return self.find_elem(
                '#viewHtml tr.listDataTh td[title="' + column_name + '"] img').get_attribute('src')
        except Exception as ex:
            print('获取排序字段图片的src属性值异常：%s' % ex)

    def get_column_row1_col1_img(self):
        '''获取类型脚本输出的值'''
        return self.find_elem('#viewHtml tbody tr.listDataTr td.listDataTrTd img').get_attribute(
            'src')

    def get_column_row1_col1_font(self):
        '''获取类型脚本输出的值'''
        return self.find_elem('#viewHtml tbody tr.listDataTr td.listDataTrTd font').get_attribute(
            'color')

    def get_collect(self):
        '''获取汇总文本'''
        try:
            return self.find_elem(
                'table#dataTable > tbody tr.listDataTr:nth-last-child(1) td:nth-child(2)').text
        except Exception as ex:
            print('获取汇总文本异常：%s' % ex)

    def get_column_button(self, val):
        '''获取列表中的操作按钮'''
        return self.find_elem(
            '#dataTable > tbody > tr.listDataTr input[type="button"][value="' + val + '"]')

    def click_jump(self):
        '''点击列表跳转类型的操作按钮'''
        self.get_column_button('跳转').click()

    def get_table_caption(self):
        '''获取case001表格的表头'''
        try:
            return self.find_elem('#_formHtml > table > caption').text
        except Exception as ex:
            print('获取case001表格的表头异常：%s' % ex)

    def add_one_row(self):
        '''新建一条数据'''
        bp = ButtonPage(self.driver)
        bp.click_activityTable_button(bp.new_btn)
        bp.wait_Tabloading_show_then_hide()
        ip = InputPage(self.driver, '折叠视图_单行文本框')
        ip.element.send_keys(20)
        bp.click_button(bp.save_start)
        bp.wait_Tabloading_show_then_hide()
        bp.click_button(bp.to_return)
        bp.wait_loading_hide()  #表单中
        bp.wait_loading_hide()  #视图中

    def click_del(self):
        '''点击列表删除类型的操作按钮'''
        self.get_column_button('删除').click()
        # self.wait_alert_show()
        # self.click_alert_dismiss()
        # self.wait_alert_dispaly()
        self.accept_alert()
        # self.get_column_button('删除').click()
        # self.wait_alert_show()
        # self.click_alert_accept()

    def click_submit(self):
        '''点击列表提交流程类型按钮'''
        self.get_column_button('提交流程').click()

    def set_val_and_submit(self, val):
        '''设置提交审批意见并确定提交'''
        self.find_elem('.aui_content textarea').send_keys(val)
        self.find_elem('.aui_state_highlight').click()

    def click_module_btn(self):
        '''点击列表以模板表单方式打开类型按钮'''
        self.get_column_button('以模板表单方式打开').click()

    def click_module_btn(self):
        '''点击列表以模板表单方式打开类型按钮'''
        self.get_column_button('以模板表单方式打开').click()

    def get_column_row1_col1_backgroundcolor(self):
        '''获取列背景颜色'''
        try:
            return self.find_elem(
                '#viewHtml tbody tr.listDataTr td.listDataTrTd').value_of_css_property('background-color')
        except Exception as ex:
            print('获取列背景颜色异常：%s' % ex)
            return ''

    def get_column_row1_col1_color(self):
        '''获取列颜色'''
        try:
            return self.find_elem(
                '#viewHtml tbody tr.listDataTr td.listDataTrTd > a').value_of_css_property('color')
        except Exception as ex:
            print('获取列颜色异常：%s' % ex)
            return ''

    def get_column_row1_col1_fontsize(self):
        '''获取列字体大小'''
        try:
            return self.find_elem(
                '#viewHtml tbody tr.listDataTr td.listDataTrTd > a').value_of_css_property('font-size')
        except Exception as ex:
            print('获取列字体大小异常：%s' % ex)
            return ''

    def get_column_row1_col1_title(self):
        '''获取提示文字'''
        try:
            return self.find_elem('#viewHtml tbody tr.listDataTr td.listDataTrTd > a').get_attribute(
                'title')
        except Exception as ex:
            print('获取提示文字异常：%s' % ex)
            return ''

    def open_fisrt_doc(self):
        '''打开第一个记录'''
        self.find_elem('table#dataTable tbody>tr').click()

    def clear_all_data(self):
        '''清空所有数据'''
        bp = ButtonPage(self.driver)
        bp.click_button(bp.clear_btn)
        self.click_alert_accept()
        self.wait_loading_hide()
        #time.sleep(0.5)

    def get_head_td1_text(self):
        '''获取视图首列列头的text'''
        try:
            return self.find_elem('#viewHtml thead tr.listDataTh td.listDataThTd>a').text
        except Exception as ex:
            print('获取视图首列列头的text异常%s' % ex)
            return ''

    def get_print_table_head_td1_text(self):
        '''获取打印视图首列列头的text'''
        try:
            return self.find_elem('table#dataTable tr.listDataTh td.listDataThTd').text
        except Exception as ex:
            print('获取打印视图首列列头的text异常%s' % ex)
            return ''


class TabListViewPage(FoldViewPage):
    def click_tab_list_rows(self):
        '''获取第一个复选框'''
        return self.find_elems('table#dataTable> tbody input[name="_selects"]')

    def click_tab_list_all_rows(self):
        '''获取全选复选框'''
        return self.find_elems('tbody#dataTable td.listDataThFirstTd')

    def tab_list_add_row(self):
        btn = ButtonPage(self.driver)
        btn_title = btn.get_tab_list_button(btn.new_btn).get_attribute('title')

        # 点击新建按钮
        btn.click_tab_list_button(btn.new_btn)
        btn.wait_loading_hide()
        #time.sleep(0.5)
        # 切换到弹出层打开的页面
        mp = MainPage(self.driver)
        mp.switch_to_div_iframe()
        #time.sleep(0.5)
        btn_title = btn.get_button_title(btn.save)
        btn.click_button(btn.save)
        btn.wait_loading_hide()
        return btn_title

    def tab_list_delete_row(self, num):
        '''选项卡点击列表删除类型的操作按钮'''
        '''删除记录数，1或者当前显示数'''
        checkboxs = self.click_tab_list_rows()
        print("checkboxs=====%s" % checkboxs)
        if checkboxs:
            if num == 1:
                checkboxs[0].click()

            else:
                for checkbox in checkboxs:
                    checkbox.click()

            bp = ButtonPage(self.driver)
            bp.click_tab_list_button(bp.del_btn)
            bp.wait_loading_hide()
            #time.sleep(0.5)
            self.click_alert_dismiss()
            #time.sleep(0.5)
            bp.click_tab_list_button(bp.del_btn)
            bp.wait_loading_hide()
            #time.sleep(0.5)
            tismsg = self.get_alert_text()
            self.click_alert_accept()
            bp.wait_loading_hide()
            #time.sleep(0.5)
            return tismsg

    def get_tab_list_record_total(self):
        '''获取视图记录总数'''
        try:
            return self.find_elem('div#acttable ul > div:nth-child(2) > span').text
        except Exception as ex:
            print('获取视图记录总数' % ex)
            return ''

    def init(self):
        pass

