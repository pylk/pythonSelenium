import os,sys
sys.path.append('../../../../')
import unittest
import time
from test_case.running.html5.flow.flow_test import FlowTest
from test_case.page_obj.flow.flow_page import ProcessApproverPage
from test_case.page_obj.view.list_view_page import ListViewPage


class ProcessApproverTest(FlowTest):
    '''审批人设置'''
    
    menu1 = '流程'
    menu2 = '审批人设置'  # 主页打开菜单时使用
    menu3 = ''


    def lilingnew(self,name):
        """李玲新建单据"""
        comp = ProcessApproverPage(self.driver)
        # 点击新建进入表单
        comp.click_newbtn()
        # 录入请假原因
        if(comp.find_elem_visible('span[id="11e7-6619-cde06435-8f1a-bfe936d3ae2a_divid"]>textarea')==None):
            comp.wait_elem_visible('span[id="11e7-6619-cde06435-8f1a-bfe936d3ae2a_divid"]>textarea')
            time.sleep(1)
            comp.find_elem_visible('span[id="11e7-6619-cde06435-8f1a-bfe936d3ae2a_divid"]>textarea').send_keys(name)
        else:
            comp.find_elem_visible('span[id="11e7-6619-cde06435-8f1a-bfe936d3ae2a_divid"]>textarea').send_keys(name)
        # 点击提交按钮
        comp.click_flow_processbtn()
        # 点击指定审批人选择框
        comp.find_elem_is_clickable('span.flowToPerson>img').click()
        # 回到主文档，没有iframe
        self.driver.switch_to.default_content()
        # 切到指定审批人iframe
        comp.switchto_designatedapprover()
        comp.wait_elem_visible('.contentDiv.on') #等待审批人框显示
        # 勾选审批人伟强
        comp.find_elem_visible('#rightcontent>div>input[name="伟强"]+span').click()
        if(comp.find_elem('#rightcontent>div>input[name="伟强"]').is_selected()==False):
            for i in range(10):
                print('次数 %s' % i)
                comp.find_elem_visible('#rightcontent>div>input[name="伟强"]+span').click()
                if (comp.find_elem('#rightcontent>div>input[name="伟强"]').is_selected()):
                    break
        comp.wait_elem_visible('#selectedUserDiv>span[title="点击删除"]')
        #等待用户选中
        comp.find_elem_is_clickable('input#doReturn').click()
        # 等待确认后的灰色锁屏消失
        self.driver.switch_to.default_content()
        comp.wait_elem_disappear('#lock_screen_div>div') #等待确认后的灰色锁屏消失
        # 返回到表单所在的iframe
        comp.switch_to_formiframe()
        # 点击确认提交
        comp.submit()



    def test_approver_organization_case(self):
        '''流程审批人for组织形式'''
        name = "流程审批人设置_通过组织"
        #time.sleep(0.5)
        comp = ProcessApproverPage(self.driver)
        self.driver.switch_to_default_content()
        comp.close_message()
        comp.switch_to_formiframe()
        # 判断是否要删除记录
        lp = ListViewPage(self.driver)
        lp.judge_delete(name)
        #李玲新建单据#333333
        self.lilingnew(name)
        #再次打开记录获取流程状态处理人
        text = comp.openagain_to_getapprover(name)
        #断言
        self.assertIn('伟强',text,msg=name+"检验不通过")

    def test_approver_role_case(self):
        '''流程审批人for角色形式'''
        menu1 = '流程'
        menu2 = '审批人设置'  # 主页打开菜单时使用
        menu3 = ''
        name = "流程审批人设置_通过角色"
        comp = ProcessApproverPage(self.driver)
        # 判断是否要删除记录
        lp = ListViewPage(self.driver)
        lp.judge_delete(name)
        #李玲新建单据
        self.lilingnew(name)
        #退出切换账号，查看是否有提交按钮
        bb = comp.logoff_and_check_submitbtn('weiqiang', '123456',menu1,menu2,menu3,name)
        self.assertEqual("true", bb, msg=name + "检验不通过")
        #time.sleep(0.5)
        #提交后再次打开表单获取流程处理人
        text = comp.aftersumbit_getapprover(name)
        self.assertIn('张强', text, msg=name + "检验不通过")


    def test_approver_iscript_case(self):
        '''流程审批人for_iscript形式'''
        menu1 = '流程'
        menu2 = '审批人设置'  # 主页打开菜单时使用
        menu3 = ''
        name = "流程审批人设置_通过iscript形式"
        #time.sleep(0.5)
        comp = ProcessApproverPage(self.driver)
        # 判断是否要删除记录
        lp = ListViewPage(self.driver)
        lp.judge_delete(name)
        #李玲新建单据
        self.lilingnew(name)
        #退出当前登录，切换账号并打开菜单记录for视图
        comp.logoff_and_openrecord('weiqiang', '123456',menu1, menu2, menu3,name)
        comp.direct_sumit()  # 直接提交
        #退出切换账号，查看是否有提交按钮
        bb = comp.logoff_and_check_submitbtn('zhangqiang', '123456',menu1,menu2,menu3,name)
        self.assertEqual("true", bb, msg=name + "检验不通过")
        #time.sleep(0.5)
        #表单是否已归档
        bool = comp.is_filed_for_aftersumbit(name)
        self.assertIsNone(bool,msg=name + "检验不通过")




    def init(self):
#         self.test_approver_organization_case()
        self.test_approver_role_case()
#         self.test_approver_iscript_case()


if __name__ == '__main__':
    unittest.main()

