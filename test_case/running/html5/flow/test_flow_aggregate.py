import os,sys
sys.path.append('../../../../')
import unittest
import time
from test_case.running.html5.flow.flow_test import FlowTest
from test_case.page_obj.flow.flow_page import ProcessApproverPage
from test_case.page_obj.view.list_view_page import ListViewPage

class Flow_aggregate(FlowTest):
    """流程测试集合"""
    menu1 = '流程'
    menu2 = ""
    menu3 = ""


    def test_adjustment_process_case(self):
        '''前台手动调整流程'''
        name = '前台手动调整流程'
        comp = ProcessApproverPage(self.driver)
        #判断是否要删除记录
        lp = ListViewPage(self.driver)
        lp.judge_delete(name)
        #点击新建进入表单
        comp.click_newbtn()
        #录入请假原因
        comp.input_reason(name)
        #点击保存并启动按钮
        comp.click_starprocessbtn()
        #点击前台流程调整按钮
        comp.click_editFlowbtn()
        #回到主文档，没有iframe
        self.driver.switch_to.default_content()
        #获取弹出框的title
        text = comp.get_popuptitle()
        self.assertEqual("调整流程",text,msg=name + "检验不通过")
        self.assertTrue(comp.is_embed_visit(),msg=name + "检验不通过")