import os,sys
sys.path.append('../../../../')
import unittest
import time
from test_case.running.html5.flow.flow_test import FlowTest
from test_case.page_obj.flow.flow_page import ProcessApproverPage
from test_case.page_obj.view.list_view_page import ListViewPage
from test_case.page_obj.main_page import MainPage
from test_case.page_obj.button_page import ButtonPage


class AdjustmentProcessTest(FlowTest):
    '''前台手动调整流程'''
    
    menu1 = '流程'
    menu2 = '基本信息'  # 主页打开菜单时使用
    menu3 = '前台手动调整流程'

    def test_adjustment_process_case(self):
        '''前台手动调整流程'''
        name = '前台手动调整流程'
        comp = ProcessApproverPage(self.driver)
        btn = ButtonPage(self.driver)
        #判断是否要删除记录
        lp = ListViewPage(self.driver)
        lp.judge_delete(name)
        #点击新建进入表单
        comp.click_newbtn()
        #录入请假原因
        #time.sleep(0.5)
        comp.input_reason(name)
        #点击保存并启动按钮
        comp.click_starprocessbtn()
        #time.sleep(0.5)
        self.assertTrue(btn.is_button_visiable('流程调整'),msg=name + "检验不通过")
        lp.wait_loading_hide()  # 等待视图加载
        #点击前台流程调整按钮
        comp.click_editFlowbtn()
        #回到主文档，没有iframe
        self.driver.switch_to.default_content()
        #获取弹出框的title
        text = comp.get_popuptitle()
        self.assertEqual("调整流程",text,msg=name + "检验不通过")
        mp = MainPage(self.driver)
        mp.switch_to_div_iframe()
        self.assertTrue(comp.is_embed_visit(),msg=name + "检验不通过")

    def init(self):
        self.test_adjustment_process_case()

if __name__ == '__main__':
    unittest.main()