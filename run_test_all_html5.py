import os
import sys
import time
import unittest
from HTMLTestRunner import HTMLTestRunner
import HTMLTestRunner_jpg
import os

from test_case.models import function


if __name__ == '__main__':
    #test_report ="./report/"
    cur_path = os.path.dirname(os.path.realpath(__file__))
    report_path = os.path.join(cur_path, "report")  # 报告存放路径
    now = time.strftime("%Y-%m-%d %H_%M")
    filename = report_path+"\\result.html"
    print("测试报告文件路径：%s" % filename)
    fp=open(report_path+"\\result.html", "wb")
    runner = HTMLTestRunner_jpg.HTMLTestRunner(stream=fp, title='myapps测试报告html5', description='用例执行情况:',verbosity=2,
                                            retry=0)
    discover = unittest.defaultTestLoader.discover("./test_case/running/html5/", pattern='test_*.py')
    runner.run(discover)
    fp.close()
    function.send_mail(filename)