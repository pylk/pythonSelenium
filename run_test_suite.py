# coding = utf-8
import unittest
from test_case.running.html5.view import test_queryform_calendar_view# 这里需要导入测试文件
from test_case.running.html5.view import test_queryform_gantt_view# 这里需要导入测试文件
from test_case.running.html5.view import test_queryform_list_view
from test_case.running.html5.view import test_queryform_tree_view #这里需要导入测试文件
from test_case.running.html5.flow import test_free_flow # 这里需要导入测试文件
from test_case.running.html5.flow import test_process_approver # 这里需要导入测试文件
from test_case.running.html5.flow import test_cc_for_role # 这里需要导入测试文件
from test_case.running.html5.flow import test_default_check # 这里需要导入测试文件
from test_case.running.html5.form import test_form_button
from test_case.running.html5 import test_main

import HTMLTestRunner
import time
from test_case.models import function

testunit = unittest.TestSuite()
# 将测试用例加入到测试容器(套件)中
# testunit.addTest(unittest.makeSuite(test_queryform_calendar_view.QueryFormCalendarViewTest))
# testunit.addTest(unittest.makeSuite(test_queryform_gantt_view.QueryFormGanttViewTest))
# testunit.addTest(unittest.makeSuite(test_queryform_list_view.QueryFormListViewTest))
# testunit.addTest(unittest.makeSuite(test_queryform_tree_view.QueryFormTreeViewTest))
# testunit.addTest(unittest.makeSuite(test_free_flow.FreeFlowTest))
# testunit.addTest(unittest.makeSuite(test_process_approver.ProcessApproverTest))
# testunit.addTest(unittest.makeSuite(test_form_button.FormButtonTest))
testunit.addTest(unittest.makeSuite(test_main.MainTest))


# 取前面时间
now = time.strftime("%Y-%m-%M-%H_%M_%S", time.localtime(time.time()))
filename = r"测试套件".format(now)
print(filename)
fp = open(filename, 'wb')

runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='myapps2.0调试用例套件测试报告', description='测试执行情况')

# 执行测试用例
runner.run(testunit)
fp.close()
function.send_mail(filename)