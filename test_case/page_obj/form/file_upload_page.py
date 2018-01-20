import os,sys
sys.path.append('../../../')
import time
from test_case.page_obj.form.form_page import FormPage
from test_case.page_obj.form.form_page import FormPhonePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class FileUploadSuperPage(object):
    '''手机端与PC端上传控件的共同方法'''

    def getcomp(self,name):
        '''根据控件名称获取控件'''
        a = self.find_elem('input[name="'+name+'"]')
        return a

    def getcompatrr(self,name,atrr):
        '''获取控件的属性'''
        a = self.find_elem('span[name="' + name + '"]').get_attribute(atrr)
        return a

    def file_upload(self,name,file_path):
        '''点击进入文件上传'''
        
        self.wait_loading_hide()
        self.click_fileupload_btn(name) #点击对应的上传控件的添加按钮
        #切到文件上传所在的iframe
        self.switch_to_fileupload_iframe()
        self.wait_filePicker_visiable()
        self.find_elem_visible("input[name="'file'"]").send_keys(file_path) #上传文件
        text = self.adjustalertexistence() #判断是否存在alert
        if(text==False):
            #点击开始上传
            self.complete_to_upload()
            #time.sleep(0.5)
            return "上传完成"
        else:
            self.reback_to_form()
            return text

    def picture_upload(self, name, file_path):
        '''点击进入图片上传'''
        
        self.wait_loading_hide()
        self.click_pictureupload_btn(name) #点击图片上传按钮
        self.switch_to_fileupload_iframe()
        self.wait_filePicker_visiable()
        self.driver.find_element_by_name("file").send_keys(file_path)
        text = self.adjustalertexistence()
        if text == False:
            # 点击开始上传
            self.find_elem('div.uploadBtn.state-ready').click()
            self.wait_elem_visible('div.btn.btn-default.state-ok', timeout=10)
            self.find_elem('div.btn.btn-default.state-ok').click()
            self.driver.switch_to.default_content()
            self.wait_elem_disappear('#lock_screen_div>div')  # 等待确认后的灰色锁屏消失
            self.formiframe()
            return "上传完成"
        else:
            self.driver.switch_to.default_content()
            self.close_aui()
            self.formiframe()
            return text

    def get_preview_title(self):
        '''获取预览界面标题'''
        return self.find_elem('span.preview-header-name').text

    def adjustalertexistence(self):
        '''判断有没有alert,有就返回alert的text，没有就返回False'''
        try:
            a = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
            text = a.text
            a.accept()
            return text
        except Exception as e:
            return False

    def is_comp_readonly(self,compname):
        '''判断控件是否只读'''
        try:
            WebDriverWait(self.driver,3).until(EC.element_to_be_clickable((By.CSS_SELECTOR, self.get_addbtn(compname))))
            return False
        except TimeoutException:
            print('find_elem获取 %s 元素超时')
            return True

    def is_comp_readonly(self, compname):
        '''判断图片上传控件是否只读'''
        try:
            WebDriverWait(self.driver, 3).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, self.get_uploadbtn(compname))))
            return False
        except TimeoutException:
            print('find_elem获取 %s 元素超时')
            return True




class FileUploadPage(FormPage,FileUploadSuperPage):


    def __init__(self,driver):
        self.driver = driver

    #点击方法

    def click_fiest_item_down(self,compname):
        '''点击上传控件的第一个上传文件的下移按钮'''
        self.find_elem_visible('span[name="'+compname+'"]+div.upload-box .hidepic>div.item:nth-child(1)>div.sort>a.down').click()

    def click_state_ok_btn(self):
        '''点击上传面板的确定按钮'''
        self.find_elem_visible('div.btn.btn-default.state-ok', timeout=15).click()  # 点击确定按钮

    def click_fileupload_btn(self,compname):
        '''点击文件上传按钮'''
        self.find_elem_visible('span[name="'+compname+'"]+div .btnAdd').click() # 点击文件上传按钮

    def click_pictureupload_btn(self,compname):
        '''点击图片上传按钮'''
        self.find_elem_visible('span[name="' + compname + '"]+div.upload-box>.upload-pic-box>.uploadinput').click()

    def close_aui(self):
        '''点击关闭上传面板界面'''
        self.find_elem_visible('a.aui_close').click()

    #等待方法

    def wait_filePicker_visiable(self):
        '''等待上传控件的选择文件按钮可见'''
        self.wait_elem_visible('#filePicker>.webuploader-pick')
    #获取元素方法

    def get_addbtn(self,compname):
        '''获取控件的添加文件元素'''
        addbtn = 'span[name=' + compname + ']+div.upload-box>div:nth-child(2)>div.btn'
        return addbtn

    #返回值方法

    def get_first_item_text(self,compname):
        '''上传控件的第一个上传文件的text'''
        return self.find_elem('span[name="'+compname+'"]+div.upload-box .hidepic>div.item:nth-child(1)>a.fieldName>span.fieldTitle').text

    def get_limitSize_text(self):
        '''获取上传界面的限制条件'''
        return self.find_elem('div.limitSize>span').text

    def getlimitSize(self,name):
        '''获取文件上传的限制条件'''
        self.click_fileupload_btn(name)
        #time.sleep(0.5)
        self.switch_to_fileupload_iframe()
        #time.sleep(0.5)
        text = self.get_limitSize_text() #获取上传界面的限制条件
        self.driver.switch_to.default_content()
        self.close_aui() #点击关闭上传面板界面
        self.formiframe()
        return text

    def get_picture_limitSize(self,name):
        '''获取图片上传的限制条件'''
        self.find_elem('span[name="' + name + '"]+div.upload-box>div>div.uploadinput>span').click()
        #time.sleep(0.5)
        self.switch_to_fileupload_iframe()
        #time.sleep(0.5)
        text = self.get_limitSize_text() #获取上传界面的限制条件
        self.driver.switch_to.default_content()
        self.close_aui() #点击关闭上传面板界面
        self.formiframe()
        return text

    #动作组合方法

    def complete_to_upload(self):
        '''完成上传动作'''
        self.find_elem_is_clickable('div.uploadBtn.state-ready').click() #点击开始上传按钮
        self.click_state_ok_btn()  # 点击确定按钮
        self.wait_elem_disappear('.aui_title') #等待文件上传框消失
        self.wait_lock_screen_div_not_visible() #等待锁屏div不显示
        self.formiframe()

    def reback_to_form(self):
        '''从上传界面切回表单'''
        self.driver.switch_to.default_content()
        self.close_aui()
        self.formiframe()

    def switch_to_fileupload_iframe(self):
        # 切到文件上传所在的iframePc端
        self.driver.switch_to.default_content()
        div_iframe = self.find_elem('div.aui_loading+iframe')
        self.driver.switch_to.frame(div_iframe)

    def open_picture(self,name,filepath):
        '''检查上传的图片是否可以点击打开'''
        try:
            self.find_elem_is_clickable('span[name="图片上传控件_限制大小"]+div.upload-box div[data-name="小于50KB.jpg"]>div>a').click()
            return True
        except Exception as e:
            return False

    def formiframe(self):
        '''返回表单iframe'''
        iframeMenu = self.find_elem("div.tab-pane.active>iframe")
        self.driver.switch_to.frame(iframeMenu)

    def scroll_to_file_upload_btn(self, compname):
        '''滚动到对应的控件按钮位置'''
        self.hide_elem_by_jq('div.activity-box')
        self.hide_elem_by_jq('div#activity-box-space')
        target_element = self.find_elem('span[name="' + compname + '"]+div .btnAdd')
        self.scroll_to_target_element(target_element)

    def scroll_to_pic_upload_btn(self, compname):
        '''滚动到对应的控件按钮位置'''
        target_element = self.find_elem('span[name="' + compname + '"]+div.upload-box>.upload-pic-box')
        self.scroll_to_target_element(target_element)

    #断言获取值

    def check_existence(self,name):
        '''判断文件上传控件是否存在---存在返回True,不存在返回False'''
        return self.is_element_visible('span[name="'+name+'"]+div .btnAdd')

    def upload_btn_is_invisibility(self,name):
        '''判断文件上传控件是否不可见---不可见返回True,可见返回False'''
        return self.is_elem_invisibility('span[name="' + name + '"]+div.btnAdd')

    def check_pic_box_existence(self,name):
        '''判断图片上传控件是否存在---存在返回True,不存在返回False'''
        return self.is_element_visible('span[name="'+name+'"]+div.upload-box>.upload-pic-box')

    def pic_upload_btn_is_invisibility(self,name):
        '''判断图片上传控件是否不可见---不可见返回True,可见返回False'''
        return self.is_elem_invisibility('span[name="' + name + '"]+div.upload-box>.upload-pic-box')


class FileUploadPhonePage(FormPhonePage,FileUploadSuperPage):
    '''手机端上传控件'''

    def __init__(self,driver):
        self.driver = driver

    def wait_filePicker_visiable(self):
        '''等待上传控件的选择文件按钮可见'''
        self.wait_elem_visible('#filePicker>.webuploader-pick')

    def get_addbtn(self,compname):
        '''获取控件的添加文件元素'''
        addbtn = 'input[name='+compname+']+div.upload-box div.fileBtn.btnAdd'
        return addbtn

    def get_uploadbtn(self,compname):
        '''获取控件的添加图片元素'''
        addbtn = 'input[name='+compname+']+div.flexright>div>a.btn-upload'
        return addbtn

    def check_existence(self,name):
        '''判断文件上传控件是否存在'''
        try:
            WebDriverWait(self.driver, timeout=3).until_not(
                EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[name="'+name+'"]+div.upload-box.formfield-wrap.flexbox')))
            return False
        except Exception as e:
            return True

    def is_picturecomp_hide(self,name):
        '''判断图片上传控件是否可见'''
        try:
            WebDriverWait(self.driver, timeout=3).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, 'input[name="'+name+'"]+div.flexright>div>a.btn-upload')))
            return True
        except:
            return False

    def click_state_ok_btn(self):
        '''手机端点击上传面板的确定按钮'''
        self.wait_elem_visible('div.btn.btn-default.state-ok[onclick="returnResult()"]', timeout=10)
        self.find_elem('div.btn.btn-default.state-ok[onclick="returnResult()"]').click()  # 点击确定按钮

    def click_fileupload_btn(self,name):
        '''点击文件上传按钮'''
        self.find_elem_is_clickable('input[name='+name+']+div.upload-box div.fileBtn.btnAdd')
        self.find_elem("input[name='"+name+"']+div.upload-box div.fileBtn.btnAdd").click()  # 点击文件上传按钮

    def click_pictureupload_btn(self,compname):
        '''点击图片上传按钮'''
        self.find_elem_is_clickable('input[name='+compname+']+div.flexright a.btn-upload')
        self.find_elem('input[name='+compname+']+div.flexright a.btn-upload').click()

    def switch_to_fileupload_iframe(self):
        # 切到文件上传所在的iframe 手机端
        self.driver.switch_to.default_content()
        div_iframe = self.find_elem('div.content>iframe')
        self.driver.switch_to.frame(div_iframe)

    def close_aui(self):
        '''点击关闭上传面板界面'''
        self.find_elem('span.icon.icon-left-nav.pull-left').click()

    def reback_to_form(self):
        '''从上传界面切回表单'''
        self.driver.switch_to.default_content()
        self.close_aui()

    def complete_to_upload(self):
        '''手机端完成上传动作'''
        self.find_elem_is_clickable('div.uploadBtn.state-ready').click()
        self.click_state_ok_btn()  # 点击确定按钮

    def open_file_to_preview(self,fielname):
        '''手机端根据文件名打开文件'''
        self.find_elem('span[data-showname="'+fielname+'"]').click()






