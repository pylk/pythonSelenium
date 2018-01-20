import os,sys
sys.path.append('../../../')
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time
from test_case.page_obj.form.text_page import TextPhonePage
from test_case.page_obj.form.text_page import TextPage
from test_case.page_obj.main_page import MainPage


class UserSelectPage(TextPage):
    '''用户选择框控件'''
    
    comp_name = ''
    driver = ''
    element = ''
    
    def __init__(self, driver, comp_name):
        '''类初始化执行'''
        self.driver = driver
        self.comp_name = comp_name
        self.element = self.get_component()
        self.dialog = self.find_elem('textarea[name="'+self.comp_name+'"]+span[title="选择用户"]')

    def select_user_byrole_noiframe(self,title,username):
        '''通过角色,用户名选择用户，不需切换到iframe'''
        self.find_elem_is_clickable('.leftContent>div>div[title="'+title+'"]').click()
        self.find_elem_is_clickable( '.right_content>div[title="'+username+'"]').click()
        self.find_elem_is_clickable('input[value="确认"]').click()


    def click_add_user_buttion(self):
        '''打开 用户选择框，切换到对应的iframe'''
        self.hide_activity_box()#隐藏表单操作按钮栏
        self.find_elem_is_clickable('textarea[name="'+self.comp_name+'"]+span[title="选择用户"]').click()
        mainpage = MainPage(self.driver)        
        mainpage.switch_to_div_iframe()
        self.wait_elem_visible('.crossULdivleft') #等待至用户选择框可见

    def select_user_byroles(self):
        '''从角色中获取用户'''
        mainpage = MainPage(self.driver) 
        self.click_add_user_buttion() #点击 用户选择框按钮
        self.find_elem_is_clickable('li#byroles').click()
        #time.sleep(0.5)
        self.find_elem_is_clickable('div.list_div[title="测试主管"]').click()
        #time.sleep(0.5)
        userlists = self.find_elems('input.list_div_click')
        returntype = ''
        if userlists:
            for userone in userlists:
                returntype = userone.get_attribute('type')
                userone.click()
        self.driver.find_element_by_id("doReturn").click()
        mainpage.switch_to_parent()
        mainpage.switch_to_iframe()
        return returntype

    def add_page_user_byroles(self):
        '''添加本页所有'''
        mainpage = MainPage(self.driver) 
        self.click_add_user_buttion()
        self.find_elem_is_clickable('li#byroles').click() #点击角色选项
        self.find_elem_is_clickable('div.list_div[title="测试主管"]').click() #点击测试主管角色
        self.find_elem_is_clickable('input#addAll').click() #点击添加本页所有
        self.find_elem_is_clickable("#doReturn").click() #点击确定按钮
        mainpage.switch_to_parent()
        mainpage.switch_to_iframe()

    def remove_all_user_byroles(self):
        '''移除所有用户'''
        mainpage = MainPage(self.driver) 
        self.click_add_user_buttion()
        self.find_elem_is_clickable('li#byroles').click() #点击角色选项
        self.find_elem_is_clickable('div.list_div[title="测试主管"]').click()
        self.find_elem_is_clickable("#doReturn").click()
        mainpage.switch_to_parent()
        mainpage.switch_to_iframe()


    def select_user_bydept(self):
        '''从部门中获取用户'''
        mainpage = MainPage(self.driver) 
        self.click_add_user_buttion()
        self.find_elem_is_clickable('li#bydept').click()
        self.find_elem_is_clickable('li[name="自动化测试用例系统企业域"]>ins').click()
        #time.sleep(0.5)
        self.find_elem_is_clickable('li[name="测试部"]>ins+a').click()
        #time.sleep(0.5)
        userlists = self.find_elems('input.list_div_click')
        #time.sleep(0.5)
        returntype = ''
        if userlists:
            for userone in userlists:
                returntype = userone.get_attribute('type')
                userone.click()
        self.driver.find_element_by_id("doReturn").click()
        mainpage.switch_to_parent()
        mainpage.switch_to_iframe()
        return returntype


    def select_user_byonline(self):
        '''从在线用户中获取用户'''
        mainpage = MainPage(self.driver) 
        self.click_add_user_buttion()
        self.find_elem('li#byonline').click()
        try:
            #time.sleep(0.5)
            userlists = self.find_elems('input.list_div_click')
            returntype = ''
            if userlists:
                for userone in userlists:
                    returntype = userone.get_attribute('type') 
                    userone.click()
                    break
            self.driver.find_element_by_id("doReturn").click()
            mainpage.switch_to_parent()
            mainpage.switch_to_iframe()            
            return returntype   
        except Exception as ex:
             print('获取控件异常：%s' %ex)     

    def select_user_bycontancts(self):
        '''从通讯录中获取用户'''
        mainpage = MainPage(self.driver) 
        self.click_add_user_buttion() #点击用户选择框
        self.find_elem_is_clickable('li#bycontancts').click()
        self.find_elem_is_clickable('div#all').click()
        userlists = self.find_elems('input.list_div_click')
        #time.sleep(0.5)
        if userlists:
            for userone in userlists:
                userone.click()
        self.driver.find_element_by_id("doReturn").click() #点击
        #切回所在iframe
        mainpage.switch_to_parent()
        mainpage.switch_to_iframe()


    def select_user_bysearch(self):
        '''从查询中获取用户'''
        mainpage = MainPage(self.driver) 
        self.click_add_user_buttion() #打开 用户选择框
        self.find_elem_is_clickable('li#bysearch').click() #点击用户选择框查询选择项
        self.find_elem_visible('#SHvalue').send_keys("liling") #在查询栏输入liling
        self.find_elem_is_clickable('input.searchPerson').click() #点击查询按钮
        time.sleep(1)   #等待用户加载完成
        userlists = self.find_elems('input.list_div_click') #获取所有查询出来的用户
        returntype = ''
        if userlists!=None:
            for userone in userlists:
                returntype = userone.get_attribute('type') #获取每一个查询出来的用户的type
                userone.click() #勾选用户
            self.find_elem_is_clickable("#doReturn").click() #点击确定按钮
            mainpage.switch_to_parent()
            mainpage.switch_to_iframe()            
            return returntype
        else:
            return None



class UserSelectPhonePage (TextPhonePage):
    '''手机端用户选择框page'''

    comp_name = ''
    driver = ''
    element = ''

    def __init__(self, driver,comp_name):
        '''类初始化执行'''
        self.driver = driver
        self.comp_name = comp_name
        self.element = self.get_component()

    def set_val(self,val):
        '''给用户选择框设值'''
        self.click_adduser_btn(self.comp_name)
        self.find_elem('input.weui_search_input').send_keys(val)
        time.sleep(0.5)
        lis = self.find_elems('label>div.weui_cell_hd')
        for li in lis:
                li.click()
        self.find_elem_is_clickable('.weui_btn.weui_btn_primary').click()  # 点击确定
        self.driver.switch_to.default_content()




    def switch_to_select_user_frame(self):
        '''切换到用户选择框iframe'''
        self.driver.switch_to.default_content()
        user_iframe = self.find_elem('div.content>iframe')
        self.driver.switch_to_frame(user_iframe)
        self.wait_elem_show_then_hide('.weui_mask_transparent')

    def select_user_by_name(self,name):
        '''根据名字选择用户'''
        self.switch_to_select_user_frame() #切换到用户选择框iframe
        self.wait_loading_hide()
        self.find_elem_is_clickable('div.weui_cells>div.weui_cell>label[data-name="'+name+'"]>div.weui_cell_hd').click()
        self.find_elem_is_clickable('.weui_btn.weui_btn_primary').click() #点击确定
        self.driver.switch_to.default_content()

    def add_user_by_name(self,userlist):
        '''根据名字选择用户'''
        for li in userlist:
            self.find_elem_is_clickable('label[data-name="'+li+'"]>div.weui_cell_hd').click()
        self.find_elem_is_clickable('.weui_btn.weui_btn_primary').click() #点击确定
        self.driver.switch_to.default_content()

    def click_adduser_btn(self,compname):
        '''点击添加用户处并切到iframe'''
        self.find_elem_is_clickable('input[name="'+compname+'"]+input+span[title="选择"]').click()
        self.switch_to_select_user_frame()

    def get_all_noAvatar_name(self):
        '''获取用户选择框的所有用户名'''
        self.switch_to_select_user_frame()  # 切换到用户选择框iframe
        noAvatars = self.find_elem('.noAvatar').text
        lis = list(noAvatars)
        print(lis)
        new_lis = []
        lenth = len(lis)
        for i in range(0, lenth, 2):
            new_lis.append(lis[i] + lis[i + 1])
        return new_lis

    def get_user_elem(self,compname):
        '''获取用户选择框控件元素'''
        tree_elem = 'input[name="'+compname+'"]+span[title="请选择"]'
        return tree_elem

    def is_comp_readonly(self,compname):
        '''判断用户选择框控件是否只读'''
        try:
            WebDriverWait(self.driver,3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.get_user_elem(compname))))
            return False
        except TimeoutException:
            print('获取 %s 超时' %compname)
            return True

    def is_comp_hide(self,compname):
        '''判断用户选择框控件是否隐藏'''
        try:
            WebDriverWait(self.driver, timeout=3).until_not(
                EC.visibility_of_element_located((By.CSS_SELECTOR, self.get_user_elem(compname))))
            return True
        except TimeoutException:
            print('获取 %s 超时' %compname)
            return False

    def get_select_users(self,compname):
        '''正常情况下获取已选的用户'''
        val = self.find_element('input[name="'+compname+'"]+input').get_attribute("value")
        return val

    def get_select_users_readonly(self,compname):
        '''只读情况下获取已选的用户'''
        target = self.find_element('div#'+compname+'_show')
        self.scroll_to_target_element(target)
        val = target.text
        return val

    def switch_dept_user_select_page(self):
        '''切换部门用户选择页面'''
        self.find_elem_is_clickable('div[data-showtype="dept"]').click()
        self.wait_Tabloading_show_then_hide()
        self.find_elem_is_clickable('div.weui_cell_bd.weui_cell_primary').click() #点击顶级部门
        self.wait_Tabloading_show_then_hide()

    def switch_role_user_select_page(self,rolename):
        '''切换到具体职务用户选择页面'''
        self.find_elem_is_clickable('div[data-showtype="role"]').click()
        self.wait_Tabloading_show_then_hide()
        self.find_elem_is_clickable('div.weui_cell_bd.weui_cell_primary').click() #点击顶级部门
        self.wait_Tabloading_show_then_hide()
        self.find_elem_is_clickable('div.weui_cells a.weui_cell[data-name="'+rolename+'"]').click()

    def add_user(self,userlist):
        '''根据名字选择用户'''
        for li in userlist:
            self.find_elem_is_clickable('label[data-name="'+li+'"]>div.weui_cell_hd').click()

    def click_clearall_btn(self):
        '''点击清空按钮'''
        self.find_elem('.weui_btn.weui_btn_plain_warn')
        self.driver.switch_to.default_content()



