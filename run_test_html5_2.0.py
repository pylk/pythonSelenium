import os
import sys
import time
import unittest
from HTMLTestRunner import HTMLTestRunner

from test_case.models import function


if __name__ == '__main__':
    test_report ="./report/"
    now = time.strftime("%Y-%m-%d %H_%M")
    filename = test_report + now + 'myapps测试报告.html'
    print("测试报告文件路径：%s" % filename)
    fp=open(filename,'wb')
    runner = HTMLTestRunner(stream=fp, title='2.0_myapps测试报告html5', description='用例执行情况:')
#     runner = unittest.TextTestRunner()
    discover = unittest.defaultTestLoader.discover("./test_case/running/html5", pattern='test_*.py')
    runner.run(discover)
    fp.close()
    function.send_mail(filename)