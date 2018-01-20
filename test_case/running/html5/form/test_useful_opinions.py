import time
import os
import sys
sys.path.append('../../../../')
from test_case.page_obj.flow.flow_page import ProcessApproverPage
from test_case.running.html5.form.component_test import ComponentTest


class UsefulopinionsTest(ComponentTest):
    '''常用意见测试'''

    menu1 = '流程'
    menu2 = '基本信息'
    menu3 = '流程基本信息_名称'  # 主页打开菜单时使用

    def test_use_usefulopinions_case(self):
        '''常用意见选用'''
        name = '常用意见选用'
        comp = ProcessApproverPage(self.driver)
        comp.wait_loading_hide()    #等待视图页面加载完成
        comp.click_newbtn()
        comp.wait_loading_hide()    #等待表单页面加载完成
        comp.click_flow_processbtn()
        #点击展开常用意见
        comp.open_usefulopinionsboard()
        #判断是否已存在相同的意见
        comp.judgedel_usefulopinions("常用意见选用")
        #点击常用意见的值
        comp.select__usefulopinions("批准")
        time.sleep(0.5) #必须，等待交互完成
        #获取意见面板的内容
        text = comp.get_usefulopinionsval()
        self.assertEqual('批准',text,msg=name+"检测不通过")
        #获取意见面板的字数
        count = comp.get_usefulopinions_count()
        self.assertEqual('2',count,msg=name+"检测不通过")

    def test_add_usefulopinions_case(self):
        '''新增常用意见'''
        name = '新增常用意见'
        title = '很好允许通过'
        comp = ProcessApproverPage(self.driver)
        comp.wait_loading_hide()    #等待视图页面加载完成
        comp.click_newbtn()
        comp.wait_loading_hide()    #等待表单页面加载完成
        #time.sleep(0.5)
        comp.click_flow_processbtn()
        #点击展开常用意见
        comp.open_usefulopinionsboard()
        #判断是否已存在相同的意见
        comp.judgedel_usefulopinions(title)
        #点击添加常用意见
        comp.add_usefulopinions(title)
        time.sleep(0.5) #必须，等待交互完成
        #点击常用意见的值
        comp.select__usefulopinions(title)
        time.sleep(5) #必须，等待交互完成
        text = comp.get_usefulopinionsval()
        self.assertEqual('很好允许通过', text, msg=name + "检测不通过")
        count = comp.get_usefulopinions_count()
        self.assertEqual('6', count, msg=name + "检测不通过")


    def overcount(self):
        '''审批意见超出'''
        name = '审批意见超出'
        title = '很好允许通过'
        comp = ProcessApproverPage(self.driver)
        comp.wait_loading_hide()    #等待视图页面加载完成
        comp.click_newbtn()
        comp.wait_loading_hide()    #等待表单页面加载完成
        comp.click_flow_processbtn()
        i = 0
        while i <24:
            comp.find_elem('textarea[name="_attitude"]').send_keys(title)
            i +=1
        count = comp.get_usefulopinions_count()
        self.assertEqual('140', count, msg=name + "检测不通过")

    def init(self):
#         self.test_add_usefulopinions_case()
        self.test_use_usefulopinions_case()


