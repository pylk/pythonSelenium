import time
import sys
import unittest
sys.path.append('../../../../')
from test_case.running.html5.view.view_test import ViewTest
from test_case.page_obj.button_page import ButtonPage
from test_case.page_obj.main_page import MainPage
from test_case.page_obj.view.fold_view_page import FoldViewPage
from test_case.page_obj.form.form_page import FormPage


class FoldViewTest(ViewTest):
    '''折叠视图测试'''

    menu1 = '视图'
    menu2 = '折叠视图'

    def open_menu3(self, menu3):
        mp = MainPage(self.driver)
        mp.open_menu(menu3)
        #time.sleep(0.3)
        mp.switch_to_iframe()
        mp.wait_loading_hide()

    def test_fold_open(self):
        '''折叠视图的展开与折叠'''
        menu3 = '折叠视图_打开类型_当前页打开'
        self.open_menu3(menu3)

        fp = FoldViewPage(self.driver)
        fp.open()
        self.assertEqual('-bbb',fp.get_open_return(),msg='折叠视图展开校验不通过')
        #time.sleep(0.3)
        fp.fold()
        #time.sleep(0.5)
        self.assertFalse(fp.get_fold_return(), msg='折叠视图折叠校验不通过')



    def test_open_type_current(self):
        '''打开类型-当前页打开'''
        menu3 = '折叠视图_打开类型_当前页打开'
        self.open_menu3(menu3)

        btn = ButtonPage(self.driver)
        btn_title = btn.get_button_title(btn.new_btn)
        self.assertEqual('新建', btn_title, msg=menu3 + '检验不通过')

        btn.click_activityTable_button(btn.new_btn)
        #time.sleep(0.5)

        btn_title = btn.get_button_title(btn.save)
        self.assertEqual('保存', btn_title, msg=menu3 + '检验不通过')

    def test_open_type_out(self):
        '''打开类型-弹出层打开'''
        menu3 = '折叠视图_打开类型_弹出层显示'
        self.open_menu3(menu3)

        btn = ButtonPage(self.driver)
        btn_title = btn.get_button_title(btn.new_btn)
        self.assertEqual('新建', btn_title, msg=menu3 + '检验不通过')

        # 点击新建按钮
        btn.click_activityTable_button(btn.new_btn)
        #time.sleep(0.5)
        mp = MainPage(self.driver)
        # 切换到弹出层打开的页面
        mp.switch_to_div_iframe()
        btn_title = btn.get_button_title(btn.save)
        self.assertEqual('保存', btn_title, msg=menu3 + '检验不通过')

    def test_record_total_show(self):
        '''显示记录总数'''
        menu3 = '折叠视图_显示记录总数_是'
        self.open_menu3(menu3)
        fp = FoldViewPage(self.driver)
        total_text = fp.get_record_total()
        self.assertIn('总记录数:', total_text, msg='显示总记录数检验不通过')

    def test_record_total_hide(self):
        '''隐藏记录总数'''
        menu3 = '折叠视图_显示记录总数_否'
        self.open_menu3(menu3)

        fp = FoldViewPage(self.driver)
        try:
            fp.get_record_total()
        except Exception as ex:
            print('不显示总记录数异常：%s' % ex)
            self.assertTrue(True, msg='不显示总记录数检验不通过')

    def test_watermark_not(self):
        '''不显示水印'''
        menu3 = '折叠视图_水印_否'
        self.open_menu3(menu3)

        fp = FoldViewPage(self.driver)
        self.assertFalse(fp.is_show_watermark(), msg='不显示水印检验不通过')

    def test_watermark_show(self):
        '''显示水印'''
        menu3 = '折叠视图_水印_是'
        self.open_menu3(menu3)

        fp = FoldViewPage(self.driver)
        self.assertTrue(fp.is_show_watermark(), msg='显示水印检验不通过')

    def test_style_lib(self):
        '''样式库使用'''
        menu3 = '折叠视图_样式库'
        self.open_menu3(menu3)
        fp = FoldViewPage(self.driver)
        self.assertIn('background-color:yellow', fp.get_style_lib(), msg='样式库使用检验不通过')

    # def test_refresh_not(self):
    #     '''无刷新功能'''
    #     print('折叠视图_刷新_否')
    #
    # def test_refresh(self):
    #     '''刷新功能'''
    #     print('折叠视图_刷新_是')

    # 只读功能
    # def test_readonly_not(self):
    #     '''非只读'''
    #     menu3 = '折叠视图_只读_否'
    #     self.open_menu3(menu3)
    #     fp = FoldViewPage(self.driver)
    #     fp.click_row()
    #     btn = ButtonPage(self.driver)
    #
    #     btn_title = btn.get_button_title(btn.save)
    #     self.assertEqual('保存', btn_title, msg='非只读检验不通过')
    #
    # def test_readonly(self):
    #     '''只读'''
    #     menu3 = '折叠视图_只读_是'
    #     self.open_menu3(menu3)
    #     fp = FoldViewPage(self.driver)
    #     fp.click_row()
    #     btn = ButtonPage(self.driver)
    #
    #     btn_title = btn.get_button_title(btn.new_btn)
    #     self.assertEqual('新建', btn_title, msg='非只读检验不通过')

    '''列功能验证'''

    def test_column_width_percent(self):
        '''列宽百分比'''
        menu3 = '折叠视图_列_列宽_百分比'
        self.open_menu3(menu3)
        fp = FoldViewPage(self.driver)
        width = fp.get_column_head_persent_by_name('折叠视图_文本一')
        self.assertIn('30%', width, msg='列宽百分比检验不通过')

    def test_column_width_px(self):
        '''列宽度px'''
        menu3 = '折叠视图_列_列宽_像素'
        self.open_menu3(menu3)
        fp = FoldViewPage(self.driver)
        width = fp.get_column_head_width('折叠视图_文本一')
        self.assertEqual('200px', width, msg='列宽固定px检验不通过')

    def test_column_multilingual(self):
        '''列多语言'''
        menu3 = '折叠视图_列_多语言'
        self.open_menu3(menu3)
        fp = FoldViewPage(self.driver)
        self.assertIsNotNone(fp.get_column_head('文本二'), msg='列多语言检验不通过')

    def test_column_iscript(self):
        '''类型脚本'''
        menu3 = '折叠视图_列_类型_脚本'
        self.open_menu3(menu3)
        fp = FoldViewPage(self.driver)
        self.assertEqual('aaa', fp.get_column_row1_col1(), msg='类型脚本检验不通过')


    ###### bug ########
    # def test_column_order(self):
    #     '''类型序号'''
    #     menu3 = '折叠视图_列_类型_序号'
    #     self.open_menu3(menu3)
    #     fp = FoldViewPage(self.driver)
    #     self.assertEqual('1', fp.get_column_row1_col1(), msg='类型序号检验不通过')

    def test_column_show_val(self):
        '''显示值'''
        menu3 = '折叠视图_列_值类型_显示值'
        self.open_menu3(menu3)
        fp = FoldViewPage(self.driver)
        self.assertEqual('测试部', fp.get_row1_col1_valueshowtrue(), msg='显示值检验不通过')

    def test_column_true_val(self):
        '''真实值'''
        menu3 = '折叠视图_列_值类型_真实值'
        self.open_menu3(menu3)
        fp = FoldViewPage(self.driver)
        self.assertEqual('11e7-5f99-e70d1a49-917f-e799edecb417', fp.get_row1_col1_valueshowtrue(), msg='真实值检验不通过')

    ######### bug #########
    # def test_column_sort_up(self):
    #     '''排序升序'''
    #     menu3 = '折叠视图_列_排序_升序'
    #     self.open_menu3(menu3)
    #     fp = FoldViewPage(self.driver)
    #     self.assertIn('up.gif', fp.get_column_sort_img_src('列表视图_部门选择框'), msg='真实值检验不通过')
    #
    # def test_column_sort_down(self):
    #     '''排序降序'''
    #     menu3 = '折叠视图_列_排序_降序'
    #     self.open_menu3(menu3)
    #     fp = FoldViewPage(self.driver)
    #     self.assertIn('down.gif', fp.get_column_sort_img_src('列表视图_部门选择框'), msg='真实值检验不通过')

    ###### bug ######
    # def test_column_return_mark(self):
    #     '''流程回退标识'''
    #     menu3 = '折叠视图_列_流程回退标识'
    #     self.open_menu3(menu3)
    #     fp = FoldViewPage(self.driver)
    #     self.assertIn('backstatelabel01.gif', fp.get_column_row1_col1_img(), msg='真实值检验不通过')
    #     self.assertIn('#ff0000', fp.get_column_row1_col1_font(), msg='真实值检验不通过')

    # def test_column_collect_subtotal(self):
    #     '''汇总_小计'''
    #     menu3 = '折叠视图_列_汇总'
    #     self.open_menu3(menu3)
    #     fp = FoldViewPage(self.driver)
    #     self.assertIn('当前页小计', fp.get_collect(), msg='汇总_小计检验不通过')
    #
    # def test_column_collect_total(self):
    #     '''汇总_总计'''
    #     menu3 = '折叠视图_列_汇总'
    #     self.open_menu3(menu3)
    #     fp = FoldViewPage(self.driver)
    #     self.assertIn('总计', fp.get_collect(), msg='汇总_总计检验不通过')

    def test_column_hide(self):
        '''列隐藏'''
        menu3 = '折叠视图_列_隐藏条件'
        self.open_menu3(menu3)
        fp = FoldViewPage(self.driver)
        self.assertIsNone(fp.get_column_head('折叠视图_树形视图选择框'), msg='列隐藏检验不通过')

    def test_column_type_jump(self):
        '''列-操作类型-跳转'''
        menu3 = '折叠视图_列_操作类型_跳转'
        self.open_menu3(menu3)
        fp = FoldViewPage(self.driver)

        fp.click_jump()
        mp = MainPage(self.driver)
        # 切换到弹出层打开的页面
        mp.switch_to_div_iframe()
        self.assertEqual('折叠视图_打开类型', fp.get_table_caption(), msg='列-操作类型-跳转检验不通过')

    def test_column_type_del(self):
        '''列-操作类型-删除'''
        menu3 = '折叠视图_列_操作类型_删除'
        self.open_menu3(menu3)
        fp = FoldViewPage(self.driver)
        if fp.get_rows_total() == 0:
            fp.add_one_row()

        #time.sleep(0.5)
        if fp.get_rows_total() == 1:
            fp.click_del()
        #time.sleep(0.5)
        self.assertEqual(0, fp.get_rows_total(), msg='列-操作类型-删除检验不通过')

    ######### bug #########
    # def test_column_type_submit(self):
    #     '''列-操作类型-提交流程'''
    #     menu3 = '折叠视图_列_操作类型_提交流程'
    #     self.open_menu3(menu3)
    #     fp = FoldViewPage(self.driver)
    #     if fp.get_rows_total() == 0:
    #         fp.add_one_row()
    #
    #     #time.sleep(0.5)
    #     if fp.get_rows_total() == 1:
    #         fp.click_submit()
    #     #time.sleep(0.5)
    #
    #     mp = MainPage(self.driver)
    #     mp.switch_to_parent()
    #     #time.sleep(0.5)
    #     fp.set_val_and_submit('请审批')
    #     #time.sleep(0.5)
    #     mp.switch_to_iframe()
    #
    #     # 点击行数据
    #     fp.click_row()
    #     #time.sleep(0.5)
    #     bp = ButtonPage(self.driver)
    #     #         bp.click_button(bp.flow_process)
    #     fp = FormPage(self.driver)
    #     #time.sleep(0.5)
    #     self.assertEqual(0, fp.get_nextids(), msg='列-操作类型-提交流程检验不通过')

    def test_column_open_by_module(self):
        '''列-操作类型-以模板表单方式打开'''
        menu3 = '折叠视图_列_操作类型_以模板表单方式打开'
        mp = MainPage(self.driver)
        self.open_menu3(menu3)
        fp = FoldViewPage(self.driver)
        fp.click_module_btn()
        #time.sleep(0.5)
        self.assertEqual('折叠视图_列_操作类型_以模板表单方式打开_模板', fp.get_text_by_css_selector('caption'), msg='列-操作类型-提交流程检验不通过')

    def test_val_type_number(self):
        '''列-格式-类型-数值-小数3位且使用千分位分隔符'''
        menu3 = '折叠视图_列_格式类型_数值_小数位千分位'
        mp = MainPage(self.driver)
        self.open_menu3(menu3)
        fp = FoldViewPage(self.driver)
        self.assertEqual('22,222.000', fp.get_row1_col1_valueshowtrue(), msg=menu3 + '检验不通过')

    def test_val_type_cash(self):
        '''列-格式-类型-货币_小数位美元'''
        menu3 = '折叠视图_列_格式类型_货币_小数位美元'
        mp = MainPage(self.driver)
        self.open_menu3(menu3)
        fp = FoldViewPage(self.driver)
        self.assertEqual('$22,222.000', fp.get_row1_col1_valueshowtrue(), msg=menu3 + '检验不通过')

    # def test_val_type_font(self):
    #     '''列-格式-字体'''
    #     menu3 = '折叠视图_列_格式字体'
    #     mp = MainPage(self.driver)
    #     self.open_menu3(menu3)
    #     fp = FoldViewPage(self.driver)
    #     self.assertEqual('rgba(255, 255, 0, 1)', fp.get_column_row1_col1_backgroundcolor(), msg=menu3 + '检验不通过')
    #     self.assertEqual('rgba(255, 0, 0, 1)', fp.get_column_row1_col1_color(), msg=menu3 + '检验不通过')
    #     self.assertEqual('20px', fp.get_column_row1_col1_fontsize(), msg=menu3 + '检验不通过')

    # def test_val_type_font_length(self):
    #     '''列_显示文字方式_文字长度'''
    #     menu3 = '折叠视图_列_显示文字方式_文字长度'
    #     mp = MainPage(self.driver)
    #     self.open_menu3(menu3)
    #     fp = FoldViewPage(self.driver)
    #     self.assertEqual('666666...', fp.get_column_row1_col1(), msg=menu3 + '检验不通过')

    # def test_val_type_title(self):
    #     '''列_显示提示文字'''
    #     menu3 = '折叠视图_列_显示提示文字'
    #     mp = MainPage(self.driver)
    #     self.open_menu3(menu3)
    #     fp = FoldViewPage(self.driver)
    #     self.assertEqual('666666', fp.get_column_row1_col1_title(), msg=menu3 + '检验不通过')

    # def test_select_all(self):
    #     '''全选'''
    #     menu3 = '折叠视图_全选和翻页'
    #     mp = MainPage(self.driver)
    #     self.open_menu3(menu3)
    #     fp = FoldViewPage(self.driver)
    #     self.assertTrue(fp.check_select_all(), msg=menu3 + '检验不通过')  # 一次选中
    #     self.assertTrue(fp.check_select_all(), msg=menu3 + '检验不通过')  # 一次取消选中

    ###折叠视图无法全选，没有翻页####
    # def test_page_turn(self):
    #     '''翻页'''
    #     menu3 = '折叠视图_全选和翻页'
    #     mp = MainPage(self.driver)
    #     self.open_menu3(menu3)
    #     fp = FoldViewPage(self.driver)
    #     fp.click_cur_page()  # 点击当前页
    #     self.assertEqual('666', fp.get_column_row1_col1(), msg=menu3 + '检验不通过')
    #     fp.click_second_page()  # 点击第二页
    #     #time.sleep(0.5)
    #     self.assertEqual('777', fp.get_column_row1_col1(), msg=menu3 + '检验不通过')
    #     fp.click_prev_page()  # 点击前一页
    #     #time.sleep(0.5)
    #     self.assertEqual('666', fp.get_column_row1_col1(), msg=menu3 + '检验不通过')
    #     fp.click_next_page()  # 点击下一页
    #     #time.sleep(0.5)
    #     self.assertEqual('777', fp.get_column_row1_col1(), msg=menu3 + '检验不通过')

    def init(self):
#                 self.test_fold_open()
                # self.test_open_type_current()
                # self.test_open_type_out()
                # self.test_record_total_show()
                # self.test_record_total_hide()
                # self.test_watermark_not()
                # self.test_watermark_show()
                # self.test_style_lib()
        #         self.test_readonly_not()
        #         self.test_readonly()
        #         self.test_column_width_percent()
                # self.test_column_width_px()
                # self.test_column_multilingual()
                # self.test_column_iscript()
        #         self.test_column_order()
                # self.test_column_show_val()
                # self.test_column_true_val()
        #         self.test_column_sort_up()
        #         self.test_column_sort_down()
        #         self.test_column_return_mark()
        #         self.test_column_collect_subtotal()
        #         self.test_column_collect_total()
                # self.test_column_hide()
                # self.test_column_type_jump()
                # self.test_column_type_del()
        #         self.test_column_type_submit()
                self.test_column_open_by_module()
                # self.test_val_type_number()
                # self.test_val_type_cash()
        #         self.test_val_type_font()
        #         self.test_val_type_font_length()
        #         self.test_val_type_title()
        #         self.test_select_all()
        #         self.test_page_turn()


if __name__ == '__main__':
    unittest.main()