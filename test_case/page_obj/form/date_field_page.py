from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from .text_page import TextPage
from .text_page import TextPhonePage


class DateFieldPage(TextPage):
    '''日期选择框控件'''
    
    comp_name = ''
    driver = ''
    element = ''
    
    def __init__(self, driver, comp_name):
        '''类初始化执行'''
        self.driver = driver
        self.comp_name = comp_name
        self.element = self.get_component()
    
    def click_item(self):
        '''打开日期选择框'''
        self.element.click()
    
    def get_now_date(self,today):
        '''点击确认，获取当前日期的值'''
        self.element.click()
        #time.sleep(0.5)
        dateValue=self.find_elem('.bootstrap-datetimepicker-widget div[class="datepicker-days"] td[data-day="'+ today +'"]').click()
        #dateValue=WebDriverWait(self.driver,5,0.5).until(EC.presence_of_element_located((By.CSS_SELECTOR,'.bootstrap-datetimepicker-widget div[class="datepicker-days"]')))      
        return self.get_attr('value')
        
    def get_end_date_status(self,comp_name,given_date):
         '''获取结束时间的状态'''
        #因为页面刷新后，第二次打开 弹出窗，获取不到元素，需要重新获取
         self.driver.find_element_by_name(comp_name)
         #time.sleep(0.5)
         self.element.click()
         #根据css返回弹框的class属性
         datapicker=self.find_elem('.bootstrap-datetimepicker-widget div[class="datepicker-days"] td[data-day="'+ given_date +'"]')
         return datapicker.get_attribute('class')

        
class DatePhonePage(TextPhonePage):
    '''日期选择框控件'''

    comp_name = ''
    driver = ''
    element = ''

    def __init__(self, driver, comp_name):
        '''类初始化执行'''
        self.driver = driver
        self.comp_name = comp_name
        self.element = self.get_component()

    def click_date_button(self,name):
        '''日历选择框按钮'''
        lis = self.find_elems('.dwbw')
        for li in lis:
            if li.text == name:
                li.click()
                break
            else:
                print('not found element %s' %name)

    def get_now_date(self):
        '''获取当前日期'''
        lis = self.find_elems('.dwwc .dw-li.dw-v')   #获取所有的年月日
        date = []
        # 获取3个参数
        for li in lis:
            if li.get_attribute('aria-selected') == 'true':
                date.append(li.find_element_by_css_selector('.dw-i').text)
        return date

    def select_start_date(self):
        '''选择开始时间'''
        self.element.click()
        self.wait_elem_visible('div.dw-slideup')  # 等待日期选择框显示
        date = self.get_now_date()
        # 拼接字符串
        rdate = date[0] + '-' + date[1] + '-' + date[2]
        self.click_date_button('确定')
        self.wait_elem_disappear('div.dw-slideup')  # 等待日期选择框消失
        self.wait_Tabloading_show_then_hide()  # 等待loading消失
        return rdate

    def get_up_button(self):
        '''获取向上箭头'''
        lis = self.find_elems('div.mbsc-ic-arrow-up5')
        liss = []
        for li in lis:
            liss.append(li)
        return liss

    def is_ymd_reflash(self,num):
        '''判断小于开始时间的结束时间不可选'''
        self.element.click()
        self.wait_elem_visible('div.dw-slideup')  # 等待日期选择框显示
        liss = self.get_up_button()
        time.sleep(0.3) #必须，时间稳定，在获取的时候判断是否可点击是无效的
        liss[num].click()   # 根据年月日点击向上箭头
        date = self.get_now_date()
        return date[num]

        
        
           
        