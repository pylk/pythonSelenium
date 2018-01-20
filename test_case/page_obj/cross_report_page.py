import time
import os
import sys
sys.path.append('../../../')
from test_case.page_obj.page import Page


class CrossReportPage(Page):
    '''交叉报表'''

    def check_type(self):
        '''检查交叉报表打开'''
        ty = self.find_elem('#__formItem')
        return ty.get_attribute('action')

    def check_summary(self):
        '''检查汇总列汇总总数'''
        maths = self.find_elems('.table-tr1 td:nth-child(3)')
        summs = self.find_elems('.table-tr1 td:nth-child(4)')
        total = self.find_elem('.tr-total td:nth-child(2)')
        x = []
        y = []
        count = 0
        tl = 0
        for math in maths:
            x.append(math.text)
        for summ in summs:
            y.append(summ.text)
            while(count < len(y)):
                tl = tl+int(summ.text)
                count = count+1
        # print(tl)
        return x == y and tl == int(total.text)

    def check_total(self):
        '''检查总计列总计总数'''
        maths = self.find_elems('.table-tr1 td:nth-child(3)')
        summs = self.find_elems('.table-tr1 td:nth-child(5)')
        total = self.find_elem('.tr-total td:nth-child(3)')
        x = []
        y = []
        count = 0
        tl = 0
        for math in maths:
            x.append(math.text)
        for summ in summs:
            y.append(summ.text)
            while(count < len(y)):
                tl = tl+int(summ.text)
                count = count+1
        # print(tl)
        return x == y and tl == int(total.text)



