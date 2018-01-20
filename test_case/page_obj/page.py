import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC


class SuperPage(object):
    '''pc和phone共同继承的page超类'''

    def __init__(self, driver):
        self.driver = driver

    #基础方法开始
    def window_scroll_to(self, yy):
        script = 'window.scrollTo(0,' + yy + ')'  # 滚动到控件可以看到后面的代码执行才不会报错
        self.driver.execute_script(script)
#         #time.sleep(0.3)

    def click_elem_by_js(self,locator):
        '''通过js点击元素'''
        elem = self.find_elem(locator)
        self.driver.execute_script("arguments[0].click();",elem)

    def hide_elem_by_jq(self,locator):
        '''通过jq将元素隐藏'''
        script = '$("'+locator+'").hide()'
        self.driver.execute_script(script)
        self.wait_elem_disappear(locator)

    def show_elem_by_jq(self,locator):
        '''通过jq将元素显示'''
        script = '$("'+locator+'").show()'
        self.driver.execute_script(script)
        self.wait_elem_visible(locator)

    def remove_locator(self,locator):
        '''js移除元素'''
        script = '$("'+locator+'").remove()'  # 从dom移除元素
        self.driver.execute_script(script)

    def find_elem(self, locator, timeout=5):
        '''判断5s内，定位的元素是否存在dom结构里。存在则返回元素，不存在则返回None'''
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, locator)))
        except:
            return None


    def find_elems(self, locator, timeout=5):
        '''判断5s内，定位的一组元素是否存在dom结构里。存在则返回元素列表，不存在则返回None'''
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, locator)))
        except:
            return None


    def find_elem_visible(self, locator, timeout=10):
        '''判断5s内，定位的元素是否存在dom结构里并且可见。存在则返回元素，不存在则返回None'''
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
        except:
            return None

    def find_elems_visible(self, locator, timeout=5):
        '''判断5s内，定位的元素是否存在dom结构里并且可见。存在则返回元素，不存在则返回None'''
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_all_elements_located((By.CSS_SELECTOR, locator)))
        except:
            return None


    def find_elem_is_clickable(self, locator,timeout=5):
        '''判断5s内，定位的元素是否可见并且可以点击。存在则返回元素，不存在则返回None'''
        try:
            return WebDriverWait(self.driver,timeout).until(EC.element_to_be_clickable((By.CSS_SELECTOR, locator)))
        except:
            return None


    def is_element_visible(self, locator, timeout=3,):
        '''判断元素是否可见，可见Ture or 不可见False'''
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
            return True
        except:
            return False

    def is_element_in_dom(self, locator, timeout=5):
        '''判断5s内，定位的元素是否存在dom结构里。存在则返回Ture，不存在则返回False'''
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, locator)))
            return True
        except:
            return False

    def wait_elem_visible(self, locator, timeout=5):
        # 一直等待某元素可见，默认超时3秒只做等待动作不返回值
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
        except TimeoutException as ex:
            print('wait_elem_visible 异常：%s 获取 %s 超时' % (ex, locator))

    def wait_elem_disappear(self, locator, timeout=3):
        # 一直等待某个元素消失，默认超时3秒只做等待动作不返回值
        try:
            WebDriverWait(self.driver, timeout).until_not(
                EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
        except TimeoutException as ex:
            print('wait_elem_visible 异常：%s 获取 %s 超时' % (ex, locator))

    def is_alert_exist(self):
        '''判断页面上是否存在alert,如果有就切换到alert并返回alert的内容'''
        try:
            instance = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
            print('存在警告框')
            return instance.text
        except:
            return False

    def is_alert_present(self):
        '''判断页面上是否存在alert,如果有就返回Ture,否则返回False'''
        try:
            WebDriverWait(self.driver, 5).until(EC.alert_is_present())
            return True
        except:
            return False


    def scroll_to_target_element(self, element):
        '''传入元素，滚动到目标元素的位置'''
        try:
            self.driver.execute_script("arguments[0].scrollIntoView();", element)
        except:
            time.sleep(0.5)
            self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def is_and_switch_to_iframe(self, locator, timeout=3):
        '''判断是否存在iframe,存在则切进去，不返回值'''
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, locator)))
        except TimeoutException:
            print('无法切到 %s ifarme' % locator)

    def is_text_in_element(self, locator,text):
        '''判断某个元素中的text是否 包含 了预期的字符串'''
        return EC.text_to_be_present_in_element((By.CSS_SELECTOR, locator),text)

    def wait_elem_remove_dom(self, locator, timeout=3):
        '''等待元素从dom中移除，常用于判页面是否已刷新'''
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.staleness_of((By.CSS_SELECTOR, locator)))
        except TimeoutException:
            print('无法切到 %s ifarme' % locator)

    def is_elem_invisibility(self, locator, timeout=3):
        '''判断元素是否不可见，不可见返回Ture, 可见返回False------常用于判断元素是否隐藏'''
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.invisibility_of_element_located((By.CSS_SELECTOR, locator)))
            return True
        except TimeoutException:
            return False

    def wait_elem_invisibility(self, locator, timeout=3):
        '''等待元素不可见，但仍存在于dom'''
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.invisibility_of_element_located((By.CSS_SELECTOR, locator)))
        except TimeoutException:
            print('元素一直可见')

    #基础方法结束

    def wait_alert_show(self):
        '''等待alert出现，不返回值'''
        WebDriverWait(self.driver, 5).until(EC.alert_is_present())

    def wait_alert_dispaly(self):
        '''等待aler消失，不返回值'''
        WebDriverWait(self.driver,2).until_not(EC.alert_is_present())

    def wait_elem_in_dom(self, locator, timeout=5):
        '''等待元素生成，已存在DOM'''
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, locator)))
        except TimeoutException:
            print('find_elem获取 %s 元素超时' % locator)

    def is_nav_not_visible(self):
        '''等待导航消失'''
        self.wait_elem_disappear('div.phone-main-nav-modal.fade-in.is-visible')
        self.wait_elem_disappear('div.phone-main-nav-modal.is-visible.fade-out')

    def accept_alert(self):
        '''接受alert'''
        instance = WebDriverWait(self.driver, 5).until(EC.alert_is_present())
        instance.accept()

    def accept_alert_for_teardown(self):
        '''teardown生命周期判断是否存在alert并且接受alert'''
        try:
            instance = WebDriverWait(self.driver, 1).until(EC.alert_is_present())
            instance.accept()
        except:
            print('没有警告框')

    def wait_msg_show_then_hide(self):
        '''等待 消息弹框 页面消失'''
        self.wait_elem_show_then_hide('#msg')

    def wait_elem_show_then_hide(self, locator):
        '''等待元素显示然后隐藏'''
        self.wait_elem_visible(locator,timeout=2)
        self.wait_elem_disappear(locator,timeout=10)

    def click_alert_accept(self):
        '''点击弹出框的确认'''
        self.accept_alert()
        #Alert(self.driver).accept()

    def click_alert_dismiss(self):
        '''点击弹出框的取消'''
        Alert(self.driver).dismiss()

    def alert_send_keys(self, keys):
        '''在确认框中输入值'''
        Alert(self.driver).send_keys(keys)

    def get_alert_text(self):
        '''点击弹出框的取消'''
        return Alert(self.driver).text

    def get_text_by_css_selector(self, selector):
        '''找到并返回元素的text'''
        try:
            text = self.driver.find_element_by_css_selector(selector).text
            return text
        except:
            return '找不到该元素的text'

    def switch_to_the_iframe(self, iframe):
        '''切换到指定的iframe页面'''
        self.driver.switch_to.frame(iframe)
#         #time.sleep(0.5)
        self.wait_Tabloading_show_then_hide()

# 基本层

class Page(SuperPage):
    '''页面基础类，用于所有页面的继承'''

    def hide_activity_box(self):
        '''隐藏表单操做按钮栏'''
        self.hide_elem_by_jq('div.activity-box')
        self.hide_elem_by_jq('div#activity-box-space')

    def switch_to_iframe(self):
        '''切换到打开的iframe页面'''
        iframeMenu = self.find_elem("div.tab-pane.active>iframe")
        try:
            self.driver.switch_to.frame(iframeMenu)
        except Exception as ex:
            print('获取iframe异常：%s' %ex)
        self.wait_loading_hide()


    def from_scroll_to(self, yy):
        self.wait_elem_in_dom('.nicescroll-cursors')
        script = 'var $con = $("#_contentTable");if($con.size()>0)$con.getNiceScroll(0).doScrollTop(' + yy + ',10)'  # 滚动到控件可以看到后面的代码执行才不会报错
        self.driver.execute_script(script)
        self.wait_loading_hide()

    def scroll_to_viewport_4_form(self, elem):
        '''执行js脚本，操作滚动条滚动到离页面顶部y值的位置'''
        try:
            win_size = self.find_elem('#container').size
            win_h = win_size['height']
            self.from_scroll_to('0')

            elem_y = elem.location['y']
            elem_h = elem.size['height']
            if elem_y != 0 and elem_h != 0:  # 不可见的元素不做定位处理，需要手动定位
                top_to = 0
                if elem_y + elem_h > win_h:  # 元素没有完全显示在界面中时
                    top_to = elem_y - 55 - 20  # 减掉操作栏的高度55，再减掉20
                    top_to = str(top_to)
                    self.from_scroll_to(top_to)
        except Exception as ex:
            print('page.scroll_to_viewport_4_form异常：%s' % ex)

    def get_attr(self, name):
        '''根据属性名获取控件属性值'''
        if self.element is not None:
            return self.element.get_attribute(name)
        else:
            print('page-->get_attr,NoneType没有属性')

    def find_element_by_css_selector(self, selector):
        '''找到并返回元素'''
        try:
            return WebDriverWait(self.driver, timeout=3).until(EC.presence_of_element_located((By.CSS_SELECTOR, selector)))
        except Exception as ex:
            print('获取元素异常：%s' % ex)
            return 'none'

    def get_msg(self):
        '''获取表单保存等操作后返回的提示信息'''
        try:
            msg_element = self.find_elem_visible('#toast-container .toast-message')
            msg = msg_element.text
            script = '$("#toast-container").remove()'  # 移除消息dom
            self.driver.execute_script(script)
            return msg
        except:
            return None

    def is_test_in_msg(self,text):
        '''判断msg中的text是否 包含 了预期的字符串'''
        bool = self.is_text_in_element('#toast-container .toast-message',text)
        script = '$("#toast-container").remove()'  # 移除消息dom
        self.driver.execute_script(script)
        return bool

    def is_msg_visiable(self):
        '''msg是否可见'''
        return self.is_element_visible('#toast-container .toast-message',timeout=8)

    def get_element_by_text(self, text):
        '''通过文本值获取元素对象'''
        return self.driver.find_element_by_link_text(text)

    def switch_to_another_window(self):
        '''切换到打开的新窗口'''
        cur_window = self.driver.current_window_handle
        all_windows = self.driver.window_handles
        
        if len(all_windows) == 1:   #必须有，新打开的窗口可能来不及统计在内
            time.sleep(0.5)
            all_windows = self.driver.window_handles
            
        for handle in all_windows:
            if handle != cur_window:
                self.driver.switch_to.window(handle)

    def close_currentwindow(self):
        '''关闭当前焦点所在的窗口并切回到当前'''
        self.driver.close()
        self.switch_to_current_window()

    def switch_to_Popup(self):
        '''切换到弹出框iframe'''
        # 回到主文档，没有iframe
        self.driver.switch_to.default_content()
        div_iframe = self.find_elem('div.aui_loading+iframe')
        self.driver.switch_to.frame(div_iframe)

    def switch_to_current_window(self):
        '''切换回当前窗口'''
        all_windows = self.driver.window_handles
        self.driver.switch_to.window(all_windows[0])

    def show_when_hide(self, text):
        '''隐藏时是否有显示值'''
        elems = self.find_elems('span')
        for elem in elems:
            text1 = elem.text
            if text1 == text:
                return True
        return False

    def show_when_print(self, text):
        '''打印隐藏时是否有显示值'''
        elems = self.find_elems('p')
        for elem in elems:
            text1 = elem.text
            if text1 == text:
                return True
        return False

    def wait_lock_screen_div_not_visible(self):
        '''等待弹出框的锁屏div不显示
                在弹出层关闭操作后使用，以确定弹出层完全隐藏，避免做其他操作时被遮挡
        '''
        self.wait_elem_disappear('#lock_screen_div')

    def wait_refresh_loading_back_show_then_hide(self):
        '''等待 刷新数据加载中 页面消失'''
        self.wait_elem_show_then_hide('#refresh-loadingDivBack')

    def wait_Tabloading_show_then_hide(self):
        '''H5等待表单 数据加载中 页面消失'''
        self.wait_elem_visible('#loadingMask',timeout=3)
        self.wait_elem_disappear('#loadingMask',timeout=10)
        # b = self.is_element_visible('#loadingMask')
        # print('8888   %s'%b)
        # if(b):
        #     self.wait_elem_disappear('#loadingMask')


    def wait_loading_hide(self):
        '''等待loading消失,统一的loading'''
        self.wait_elem_visible('#loadingMask',timeout=3)
        self.wait_elem_disappear('#loadingMask',timeout=10)
        # b = self.is_element_visible('#loadingMask')
        # print('8888   %s'%b)
        # if(b):
        #     self.wait_elem_disappear('#loadingMask')



class PhonePage(SuperPage):
    
    def get_msg(self):
        '''获取表单保存等操作后返回的提示信息'''
        self.wait_elem_visible('#msg .msgSub')
        msg = self.find_elem('#msg .msgSub')
        return msg.text

    def get_attr(self, name):
        '''根据属性名获取控件属性值'''
        if self.element is not None:
            return self.element.get_attribute(name)
        else:
            print('page-->get_attr,NoneType没有属性')

    def find_element(self, locator):
        '''寻找元素,返回元素'''
        # 仅替代form.bd.cur中的find_element_by_XXXX
        locator = "form.bd.cur " + locator
        return self.find_elem(locator)

    def find_elements(self, locator):
        '''寻找元素，返回列表'''
        # 仅替代form.bd.cur中的find_elements_by_XXXX
        # 判断是否至少有一个元素在页面中可见，如果定位到就返回列表
        locator = "form.bd.cur " + locator
        return self.find_elems(locator)

    def is_loading_not_visible(self, timeout=10):
        '''判断 数据加载中 页面是否存在'''
        try:
            WebDriverWait(self.driver, timeout).until_not(
                EC.visibility_of_element_located((By.CSS_SELECTOR, '.weui_toast')))
            return True
        except TimeoutException:
            return False

    def is_msg_not_visible(self, timeout=10):
        '''判断按钮点击弹出消息页面是否存在'''
        try:
            WebDriverWait(self.driver, timeout).until_not(
                EC.visibility_of_element_located((By.CSS_SELECTOR, '#msg')))
            return True
        except TimeoutException:
            return False

    def msg_visible(self):
        '''判断某个元素在是否存在于dom或不可见,如果可见返回False,不可见返回这个元素'''
        return WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located((By.CSS_SELECTOR, '#msg')))

    def select_user_by_name_for_form(self,name):
        '''根据名字选择用户'''
#         #time.sleep(0.5)
        #切换到用户选择框iframe
        self.driver.switch_to.default_content()
        user_iframe = self.find_elem('div.content>iframe')
        self.driver.switch_to_frame(user_iframe)
        self.wait_elem_show_then_hide('.weui_mask_transparent')
        self.find_elem('div.weui_cells>div.weui_cell>label[data-name="'+name+'"]>div.weui_cell_hd').click()
        self.find_elem('.weui_btn.weui_btn_primary').click()
        self.driver.switch_to.default_content()

    def wait_Tabloading_show_then_hide(self):
        '''Phone等待表单 数据加载中 页面消失'''
        try:
            self.wait_elem_show_then_hide('#loadingToast')
        except:
            print('等待loding消失时出错，可能是页面正在切换，handler被销毁')

    def wait_loading_hide(self):
        '''等待loading消失,统一的loading'''
        try:
            self.wait_elem_show_then_hide('#loadingToast')
        except:
            print('等待loding消失时出错，可能是页面正在切换，handler被销毁')
            
    def find_element_is_clickable(self, locator,timeout=5):
        '''判断5s内，定位的元素是否可见并且可以点击。存在则返回元素，不存在则返回None'''
        locator = "form.bd.cur " + locator
        try:
            return WebDriverWait(self.driver,timeout).until(EC.element_to_be_clickable((By.CSS_SELECTOR, locator)))
        except TimeoutException:
            print('find_elem_is_clickable获取 %s 元素超时' % locator)
