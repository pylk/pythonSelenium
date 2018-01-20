import os, sys
sys.path.append('../../../../')
import unittest
from test_case.page_obj.form.view_select_page import ViewSelectPhonePage
from test_case.running.phone.form.component_test import ComponentPhoneTest
from test_case.page_obj.form.input_page import InputPhonePage
from test_case.page_obj.main_page import MainPhonePage

class ViewSelectPhoneTest(ComponentPhoneTest):
    '''视图选择框测试'''

    menu1 = '表单'
    menu2 = '表单控件'
    menu3 = '视图选择框'  # 主页打开菜单时使用

    def test_type_case(self):
        '''类型'''
        compname = '视图选择框_说明文字'
        comp = ViewSelectPhonePage(self.driver)
        target_element = comp.getcomp(compname)
        type = target_element.get_attribute("type")
        self.assertEqual(type, "button", msg='视图选择框类型检验不通过')

    def test_view_name_case(self):
        '''视图选择框_说明文字'''
        compname = '视图选择框_说明文字'
        comp = ViewSelectPhonePage(self.driver)
        target_element = comp.getcomp(compname)
        type = target_element.get_attribute("title")
        self.assertEqual(type, "说明文字：自动化测试", msg='视图选择框_说明文字检验不通过')

    def test_mapped_case(self):
        '''默认模式映射'''
        compname = '视图选择框_说明文字'
        comp = ViewSelectPhonePage(self.driver)
        comp.setvalue(compname,['选择框1'])
        inputtext1 = comp.get_inputtext_value('真实值')
        self.assertEqual(inputtext1,'1',msg='视图选择框映射模式不生效')
        inputtext2 = comp.get_inputtext_value('显示值')
        self.assertEqual(inputtext2,'选择框1',msg='视图选择框映射模式不生效')

    def test_mosaic_case(self):
        '''拼接模式映射'''
        compname = '视图选择框_拼接模式'
        comp = ViewSelectPhonePage(self.driver)
        comp.setvalue_for_mosaic(compname,['选择框1','2'])
        inputtext1 = comp.get_inputtext_value('真实值')
        self.assertEqual(inputtext1,'选择框1;2',msg='视图选择框_拼接模式不生效')

    def test_mosaic_clear_case(self):
        '''拼接模式清除操作'''
        compname = '视图选择框_拼接模式'
        comp = ViewSelectPhonePage(self.driver)
        comp.setvalue_for_mosaic(compname, ['选择框1', '2'])
        inputtext1 = comp.get_inputtext_value('真实值')
        self.assertEqual(inputtext1, '选择框1;2', msg='视图选择框_拼接模式不生效')
        comp.clear_value_for_mosaic(compname, ['选择框3', '4'])
        inputtext2 = comp.get_inputtext_value('真实值')
        self.assertEqual(inputtext2, '', msg='拼接模式清除操作不生效')

    def test_multiterm_case(self):
        '''多项选择模式映射'''
        compname = '视图选择框_多项选择'
        comp = ViewSelectPhonePage(self.driver)
        comp.setvalue_for_multiterm(compname,['2','4'])
        inputtext1 = comp.get_inputtext_value('真实值')
        self.assertEqual(inputtext1,'1;3',msg='视图选择框_多项选择不生效')

    def test_multiterm_remove_case(self):
        '''多项选择模式清除已选项'''
        compname = '视图选择框_多项选择'
        comp = ViewSelectPhonePage(self.driver)
        comp.setvalue_for_multiterm(compname,['2','4'])
        inputtext1 = comp.get_inputtext_value('真实值')
        self.assertEqual(inputtext1,'1;3',msg='视图选择框_多项选择不生效')
        comp.clear_value_for_multiterm(compname, ['3', '5'])
        inputtext2 = comp.get_inputtext_value('真实值')
        self.assertEqual(inputtext2, '1;3', msg='视图选择框_多项选择清除操作不生效')

    def test_recalculation_case(self):
        '''重计算'''
        compname = '视图选择框_重计算'
        comp = ViewSelectPhonePage(self.driver)
        self.assertTrue(comp.is_comp_hide(compname),msg='视图选择框模板bug')
        textInput = InputPhonePage(self.driver,'真实值')
        textInput.send_keys_trigger_refresh('隐藏')
        self.assertFalse(comp.is_comp_hide(compname), msg='视图选择框重计算不生效')

    def test_show_when_hide_case(self):
        '''隐藏时显示值'''
        compname = '视图选择框隐藏时显示值'
        comp = ViewSelectPhonePage(self.driver)
        self.assertIn('控件已隐藏', comp.get_curpage_span(), msg=compname+'检验不通过')

    def test_display_case(self):
        """条件只读"""
        compname = '视图选择框_只读条件'
        comp = ViewSelectPhonePage(self.driver)
        self.assertTrue(comp.is_comp_readonly(compname), msg=compname+'检验不通过')

    def test_confirm_case(self):
        """确定条件为false"""
        compname = '视图选择框_确定条件'
        comp = ViewSelectPhonePage(self.driver)
        comp.select_val(compname, ['2'])
        self.assertIn(comp.is_alert_exist(), "确定条件出错，请联系后台管理员", msg=compname + "检验不通过")
        comp.accept_alert()
        comp.close_viewTab()

    def test_afterconfirm_case(self):
        """确定后执行脚本"""
        compname = '视图选择框_确定后执行脚本'
        comp = ViewSelectPhonePage(self.driver)
        comp.select_val(compname, ['2'])
        inputtext1 = comp.get_inputtext_value('真实值')
        self.assertEqual(inputtext1, '2', msg='视图选择框_确定后执行脚本不生效')

    def tearDown(self):
        mp = MainPhonePage(self.driver)
        if mp.find_elem('.icon.icon-left-nav.pull-left')!=None:
            mp.find_elem_is_clickable('.icon.icon-left-nav.pull-left').click()
            mp.wait_Tabloading_show_then_hide()
            mp.return_to_homepage()
        else:
            if mp.is_loading_not_visible() == True:
                if mp.is_msg_not_visible() == True:
                    mp.return_to_homepage()


    def init(self):
#         self.test_type_case()
#         self.test_mosaic_clear_case()
#         self.test_display_case()
        self.test_afterconfirm_case()

if __name__ == '__main__':
    unittest.main()




