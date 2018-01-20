import unittest
import time
import os
import sys
sys.path.append('..')
from HTMLTestRunner import HTMLTestRunner
from test_case.models import function

from test_case.running.html5.test_login import LoginTest
from test_case.running.html5.test_main import MainTest
from test_case.running.html5.test_cross_report import CrossReportTest

'''表单'''
from test_case.running.html5.form.test_input_field import InputTest
from test_case.running.html5.form.test_textarea_field import TextareaTest
from test_case.running.html5.form.test_radio_field import RadioTest
from test_case.running.html5.form.test_checkbox_field import CheckboxTest
from test_case.running.html5.form.test_suggest_field import SuggestTest
from test_case.running.html5.form.test_qrcode_field import QrcodeTest
from test_case.running.html5.form.test_calculate_field import CalculateTest
from test_case.running.html5.form.test_map_field import MapTest
from test_case.running.html5.form.test_take_phone_field import TakephoneTest
from test_case.running.html5.form.test_survey_field import SurveyTest
from test_case.running.html5.form.test_word_field import WordTest
from test_case.running.html5.form.test_html_field import HtmlTest
from test_case.running.html5.form.test_date_field import DateFieldTest
from test_case.running.html5.form.test_flowhistory import FlowhistoryTest
from test_case.running.html5.form.test_flow_remind_history import FlowRemindHistoryTest
from test_case.running.html5.form.test_gps_field import GPSTest
from test_case.running.html5.form.test_record_field import RecordTest
from test_case.running.html5.form.test_form_function import FormTest
from test_case.running.html5.form.test_form_button import FormButtonTest
from test_case.running.html5.form.test_file_upload_field import FileUploadTest
from test_case.running.html5.form.test_component_button import ComponentButtonTest
from test_case.running.html5.form.test_picture_upload_field import PictureUploadTest
from test_case.running.html5.form.test_view_select_field import ViewSelectTest
from test_case.running.html5.form.test_tab_field import TabTest

'''视图'''
from test_case.running.html5.view.test_list_view import ListViewTest
from test_case.running.html5.view.test_view_button import ViewButtonTest
from test_case.running.html5.view.test_grid_view import GridViewTest
from test_case.running.html5.view.test_calendar_view import CalendarViewTest
from test_case.running.html5.view.test_fold_view import FoldViewTest


from test_case.running.html5.view.test_queryform_calendar_view import QueryFormCalendarViewTest
from test_case.running.html5.view.test_queryform_gantt_view import QueryFormGanttViewTest
from test_case.running.html5.view.test_queryform_list_view import QueryFormListViewTest

'''流程'''
from test_case.running.html5.flow.test_free_flow import FreeFlowTest
from test_case.running.html5.flow.test_edit_approver import EditApproverTest
from test_case.running.html5.flow.test_adjustment_process import AdjustmentProcessTest

'''手机端'''
from test_case.running.phone.form.test_qrcode import QrcodePhoneTest
from test_case.running.phone.form.test_radio import RadioPhoneTest
from test_case.running.phone.form.test_component_button import ComponentButtonPhoneTest
from test_case.running.phone.form.test_form_button import FormButtonPhoneTest
from test_case.running.phone.form.test_suggest_field import SuggestPhoneTest
from test_case.running.phone.form.test_html_field import HtmlPhoneTest
from test_case.running.phone.form.test_record_field import RecordPhoneTest
from test_case.running.phone.form.test_flowhistory import FlowhistoryPhoneTest
from test_case.running.phone.form.test_flow_remind_history import FlowRemindHistoryPhoneTest
from test_case.running.phone.form.test_survey_field import SurveyPhoneTest

from test_case.running.phone.view.test_list_view import ListViewPhoneTest
from test_case.running.phone.view.test_query_form import QueryFormPhoneTest
from test_case.running.phone.view.test_view_button import ViewButtonPhoneTest
from test_case.running.phone.test_main import MainPhoneTest

if __name__ =="__main__":
    testunit = unittest.TestSuite()
#     testunit.addTest(LoginTest('test_login'))    # 登录测试
    testunit.addTest(MainTest('init'))      # 主页测试
#     testunit.addTest(CrossReportTest('init'))

    '''表单'''
#     testunit.addTest(InputTest('init'))    # 单行文本控件测试
#     testunit.addTest(TextareaTest('init')) 
#     testunit.addTest(RadioTest('init'))
#     testunit.addTest(QrcodeTest('init'))
#     testunit.addTest(CalculateTest('init'))
#     testunit.addTest(MapTest('init'))
#     testunit.addTest(TakephoneTest('init'))
#     testunit.addTest(SurveyTest('init'))
#     testunit.addTest(WordTest('init'))
#     testunit.addTest(HtmlTest('init'))
#     testunit.addTest(FlowhistoryTest('init'))
#     testunit.addTest(FlowRemindHistoryTest('init'))
#     testunit.addTest(GPSTest('init'))
#     testunit.addTest(RecordTest('init'))
#     testunit.addTest(FormTest('init'))
#     testunit.addTest(GridViewTest('init'))
#     testunit.addTest(FormButtonTest('init'))
#     testunit.addTest(FileUploadTest('init'))
#     testunit.addTest(CheckboxTest('init'))
#     testunit.addTest(ComponentButtonTest('init'))
#     testunit.addTest(SuggestTest('init'))
#     testunit.addTest(DateFieldTest('init'))
#     testunit.addTest(PictureUploadTest('init'))
#     testunit.addTest(ViewSelectTest('init'))
#     testunit.addTest(TabTest('init'))

    '''视图'''
#     testunit.addTest(ViewButtonTest('init'))
#     testunit.addTest(ListViewTest('init'))    # 列表视图测试
#     testunit.addTest(CalendarViewTest('init'))
#     testunit.addTest(FoldViewTest('init'))


#     testunit.addTest(QueryFormCalendarViewTest('init'))
#     testunit.addTest(QueryFormGanttViewTest('init'))
#     testunit.addTest(QueryFormListViewTest('init'))
    
    '''流程'''
#     testunit.addTest(AdjustmentProcessTest('init'))
#     testunit.addTest(FreeFlowTest('init'))
    
    
    '''手机端'''
#     testunit.addTest(MainPhoneTest('init'))
    '''表单'''
#     testunit.addTest(QrcodePhoneTest('init'))
#     testunit.addTest(RadioPhoneTest('init'))
#     testunit.addTest(ComponentButtonPhoneTest('init'))
#     testunit.addTest(FormButtonPhoneTest('init'))
#     testunit.addTest(SuggestPhoneTest('init'))
#     testunit.addTest(HtmlPhoneTest('init'))
#     testunit.addTest(RecordPhoneTest('init'))
#     testunit.addTest(FlowhistoryPhoneTest('init'))
#     testunit.addTest(FlowRemindHistoryPhoneTest('init'))
#     testunit.addTest(SurveyPhoneTest('init'))
    
    
    '''视图'''
#     testunit.addTest(ListViewPhoneTest('init'))
#     testunit.addTest(ViewButtonPhoneTest('init'))
#     testunit.addTest(QueryFormPhoneTest('init'))

    
    test_report ="../report/"
    now = time.strftime("%Y-%m-%d %H_%M")
    filename = test_report + now + 'myapps测试报告.html'
    print("测试报告文件路径：%s" % filename)
    fp=open(filename,'wb')
#     runner = HTMLTestRunner(stream=fp, title='myapps测试报告', description='用例执行情况:')
    runner = unittest.TextTestRunner()
    runner.run(testunit)
    fp.close()
#     function.send_mail(filename)