# coding = utf-8
import unittest
from test_case.running.html5.flow import test_free_flow # 这里需要导入测试文件
import HTMLTestRunner_jpg
import time
from test_case.models import function
import os

testunit = unittest.TestSuite()
# 将测试用例加入到测试容器(套件)中
testunit.addTest(unittest.makeSuite(test_free_flow.FreeFlowTest))

# 取前面时间
cur_path = os.path.dirname(os.path.realpath(__file__))
now = time.strftime("%Y-%m-%M-%H_%M_%S", time.localtime(time.time()))
report_path = os.path.join(cur_path, "report")  # 报告存放路径
runner = HTMLTestRunner_jpg.HTMLTestRunner(title="可以装逼的测试报告",
                                            description="测试用例参考",
                                            stream=open(report_path+"\\result.html", "wb"),
                                            verbosity=2,
                                            retry=0)

# 执行测试用例
runner.run(testunit)

function.send_mail(report_path+"\\result.html")