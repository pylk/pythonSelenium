import time
from test_case.page_obj.page import Page
from test_case.page_obj.page import PhonePage
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException



class ButtonPage(Page):
    
    new_btn = '2' #新建
    del_btn = '3' #删除
    clear_btn = '18'  #清除所有数据
    import_view = '1' #载入视图
    batch_submit = '20'   #批量提交
    batch_signature = '29'    #批量签章
    excel_export = '16'   #导入Excel
    excel_import = '27'   #导出Excel
    file_download = '26'  #表单和视图都有
    view_page_print = '36'    #视图打印
    jump_to = '43'    #跳转-表单和视图都有
    
    user_defined = '13'   #自定义
    save = '34'   #保存
    save_start = '4'  #保存并启动流程
    save_return = '11'    #保存并返回
    save_new = '42'   #保存并新建
    save_draft = '19' #保存草稿
    save_copy = '21'  #保存并复制
    flow_process = '5'    #流程处理
    flow_start = '33' #流程启动
    to_return = '10'  #返回
    submit_star_flow = '10' #提交_发起流程
    close_window = '8'    #关闭窗口
    form_page_print = '14'    #网页打印
    form_page_print_history = '15'    #网页打印（带流程历史）
    user_defined_print = '30' #自定义打印
    place_on_file = '45'  #归档
    pdf_export = '25' #pdf导出
    jinge_signature = '28'    #金格电子签章
    share_to = '37'   #分享
    signature = '46'  #签章
    
    type='2'
    
    gridview_save='保存' #网格视图保存按钮
    gridview_cancel='取消所有'  #网格视图取消所有
    
    def __init__(self, driver):
        self.driver = driver

    def get_button(self, num):
        '''获取表单和视图按钮
                根据num值判断按钮的类型
        container可以获取到文本区的按钮控件，activityTable是获取操作栏按钮
        '''
        return self.find_elem_is_clickable('#container a[class~="'+num+'"], #activityTable a[class~="'+num+'"]')

    def get_button_by_type_title(self, num, title):
        '''获取表单和视图按钮
                根据num值判断按钮的类型
        '''
        try:
            return self.find_elem_is_clickable('#container a[class~="'+num+'"][title="'+title+'"], #activityTable a[class~="'+num+'"][title="'+title+'"]')
        except Exception as ex:
            print('获取按钮异常：%s' %ex)
            return 'none'


    
    def get_tab_list_button(self, num):
        try:
            '''获取选项卡下视图按钮'''
            return self.find_elem_is_clickable('#acttable a[class~="'+num+'"]')
        except Exception as ex:
            print('获取控件异常：%s' %ex)
            return '' 
        
    def get_tab_list_button_by_title(self, title):
        try:
            '''获取选项卡下视图按钮'''
            return self.find_elem('#acttable a[title="'+title+'"]').title
        except Exception as ex:
            print('获取控件异常：%s' %ex)
            return ''
         
    def get_gridview_button(self, num):
        '''获取网格视图按钮，根据num值判断按钮的类型
        '''
        try:
            return self.find_elem('#gridview-container a[class~="'+num+'"]')
        except Exception as ex:
            print('获取控件异常：%s' %ex)
            return ''
         
    def get_gridview_defaultbutton(self, title):
        '''获取网格视图按钮，根据num值判断按钮的类型
        '''
        try:
            return self.find_elem('#gridview-container a[title="'+title+'"]')
        except Exception as ex:
            print('获取控件异常：%s' %ex)
            return ''
            
    def click_gridview_button(self, num):
        '''网格视图 根据num值判断按钮的类型'''
        self.get_gridview_button(num).click()

    def click_gridview_defaultbutton(self, title):
        '''网格视图 根据num值判断按钮的类型'''
        self.get_gridview_defaultbutton(title).click()
    
    def click_button(self, num):
        '''表单和视图按钮点击
                根据num值判断按钮的类型
        '''
        # , #activityTable a[class~="' + num + '"]
        target = self.find_elem_visible('#container a[class~="' + num + '"]')
        if(target==None):
            for i in range(10):
                print('视图按钮为NONE次数 %s'%i)
                a = self.find_elem_visible('#container a[class~="' + num + '"]')
                if(a!=None):
                    a.click()
        else:
            target.click()

    def click_activityTable_button(self, num):
        '''表单和视图按钮点击
                根据num值判断按钮的类型
        '''
        # , #activityTable a[class~="' + num + '"]
        target = self.find_elem_visible('#activityTable a[class~="' + num + '"]')
        if(target==None):
            for i in range(10):
                print('视图按钮为NONE次数 %s'%i)
                a = self.find_elem_visible('#activityTable a[class~="' + num + '"]')
                if(a!=None):
                    a.click()
        else:
            target.click()



    def click_default_btn(self,name):
        '''根据名称点击自定义按钮'''
        return self.find_elem_is_clickable('a[title="'+ name +'"]').click()

    def click_button_by_type_title(self, btn_num, title):
        '''表单和视图按钮点击
                根据num值判断按钮的类型
        '''
        try:
            self.get_button_by_type_title(btn_num, title).click()
            self.wait_Tabloading_show_then_hide()
        except Exception as ex:
            print('点击按钮异常：%s' %ex)

    def click_tab_list_button(self, num):
        '''表单和视图按钮点击
                根据num值判断按钮的类型
        '''
        self.get_tab_list_button(num).click()  
          
    def get_button_title(self, num):
        return self.get_button(num).get_attribute('title')
    
    def appoint_flow(self):
        '''在启动流程界面指定流程并确定'''
        #选择流程
        select = self.find_elem_is_clickable('select[name="selectFlow"]')
        select.click()
        self.find_elem_is_clickable('option:nth-child(2)').click()
        #勾选提交至节点
        #time.sleep(0.5)
        self.find_elem_is_clickable('#nodelist input[name="_nextids"]').click()
        #点击确认按钮
        self.find_elem_is_clickable('input[name="confirm"]').click()
        #time.sleep(0.2)
    
    def click_confirm_submit(self):
        '''点击确定提交按钮'''
        self.find_elem_is_clickable('[name="btn_act_committo"]').click()
    
    def get_history(self):
        try:
            return self.find_elem('[name="_history"]')
        except Exception as ex:
            print('获取打印流程历史异常%s' %ex)
            return 'none'
        
    def get_caption_text(self):
        '''获取页面的caption元素值'''
        #a = self.find_elem('caption')
        text = self.find_elem_visible('caption').text
        return text
    
    def select_user(self):
        '''选择用户'''
        self.find_elem_visible('.leftContent>div>div[title="员工"]').click()
        self.wait_elem_visible('.list_div list_div_head+#righttitle') #等待对应的角色内容可见
        self.find_elem_visible('input#addAll').click()
        self.find_elem_visible('#doReturn').click()

    def select_userbyrolename(self,rolename):
        '''通过角色名选择用户'''
        self.find_elem_visible('#leftcontent div[title="'+rolename+'"]').click()
        #time.sleep(0.5)
        self.find_elem_visible('input#addAll').click()
        #time.sleep(0.5)
        self.find_elem_visible('#doReturn').click()
    
    def to_share(self):
        '''分享操作'''
        self.find_elem_is_clickable('[name="email"]').click()
        self.find_elem_is_clickable('#receiverid + input').click()
        
    def click_send(self):
        '''点击发送'''
        self.wait_elem_visible('.button-cmd>.btn_mid>a.sendicon')
        self.find_elem_is_clickable('.button-cmd>.btn_mid>a.sendicon').click()
    
    def click_close(self):
        '''点击关闭窗口'''
        self.find_elem_is_clickable('.button-cmd>.btn_mid>a.exiticon').click()
    
    def select_signature(self):
        '''选择签章'''
        panel = self.find_elem('#_contentTable > .toolPanel')
        panel.click()
        panel.find_element_by_css_selector('#sign_select').click()
        panel.find_element_by_css_selector('#sign_select option:nth-child(2)').click()
        panel.find_element_by_css_selector('.sign_btn').click()
        
    def confirm_signature(self):
        '''确定签章'''
        action = self.find_elem_visible('#_contentTable > .sign > a.ok').click()

    def open_and_switch_to_self_print_page(self):
        '''打开并切换到自定义打印页面'''
        bp = ButtonPage(self.driver)
        bp.click_button(bp.user_defined_print)
        bp.wait_loading_hide()
        #time.sleep(0.1)
        self.switch_to_another_window()
    
    def get_msg_share_page(self):
        return self.find_elem_visible('#msg .msgSub').text

    def is_button_visiable(self,button_name):
        '''输入按钮名，判断按钮是否可见'''
        return self.is_element_visible('a.btn[title="'+button_name+'"]')


class ButtonPhonePage(PhonePage):

    def __init__(self, driver):
        self.driver = driver

    def get_button(self, name):
        try:
            return self.find_element('.btn-block[title="'+name+'"]')
        except Exception as ex:
            print('获取按钮异常:%s' % ex)

    def click_iframe_button(self,name):
         '''点击ifarme里面的buttonm'''
         self.find_elem_is_clickable('.btn-block[title="'+name+'"]').click()


    def click_button(self,name):
        '''操作按钮'''
        self.wait_Tabloading_show_then_hide() #等待loading页面消失
        self.find_elem_is_clickable('.bd.cur .btn-block[title="'+name+'"]').click()

    def click_flowpanel_button(self,name):
        '''流程面板的底部操作按钮'''
        lis = self.find_elems_visible('#div_button_place  .btn-block')
        for li in lis:
            if li.text == name:
                li.click()
                break

    def is_button_exist(self,name):
        """根据名称判断是否存在对应操作按钮"""
        btn = self.get_button(name)
        return btn != None
