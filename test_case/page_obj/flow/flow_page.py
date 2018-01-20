import os, sys

sys.path.append('../../../')
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
import time
from test_case.page_obj.page import Page
from test_case.page_obj.page import PhonePage
from test_case.page_obj.main_page import MainPage
from test_case.page_obj.button_page import ButtonPage
from test_case.page_obj.button_page import ButtonPhonePage
# 引入鼠标操作类
from selenium.webdriver.common.action_chains import ActionChains
# 引入登陆操作类
from test_case.page_obj.login_page import LoginPage



class SuperFlowPage(object):
    """ProcessApproverPage和PhoneFlowPage的共同方法"""

    def input_reason(self, name):
        # 录入请假原因
        self.find_elem_visible('textarea[name="请假原因"]').send_keys(name)


class ProcessApproverPage(Page, SuperFlowPage):
    """流程审批人设置测试"""
    driver = ''

    def launch_a_flowform(self, name):
        # 发起一张流程表单
        '''name是菜单名也是请假原因'''
        # 点击新建进入表单
        self.click_newbtn()
        # 录入请假原因
        self.input_reason(name)
        # 点击提交按钮
        self.click_flow_processbtn()
        # 点击确认提交
        self.submit()

    def openagain_to_getapprover(self, name):
        # 再次打开录入的记录获取流程状态处理人
        self.openagain_record(name)
        self.wait_loading_hide()
        # 获取流程状态的处理人
        text = self.get_approver()
        return text

    def switch_account(self, username, password, ):
        # 切换账号登陆
        po = LoginPage(self.driver)
        po.user_login(username, password)

    def open_m(self, menu1, menu2, menu3):
        # 用于切换账号后打开菜单
        mp = MainPage(self.driver)
        if menu1 != '':
            mp.open_menu(menu1)
        if menu2 != '':
            mp.open_menu(menu2)
        if menu3 != '':
            mp.open_menu(menu3)
        self.wait_loading_hide() #等待loading加载完
        mp.switch_to_iframe()

    def is_submit_existed(self, name):
        # 判断提交按钮是否存在
        # 再次打开相应记录
        self.openagain_record(name)
        #time.sleep(0.5)
        # 判断有无提交按钮
        btn = ButtonPage(self.driver)
        if btn.is_button_visiable('提交'):
            return "true"
        else:
            return "false"

        # bb = self.is_elementPresent()
        # return bb

    def close_message(self):
        '''关闭'''
        try:
            #time.sleep(0.2)
            message_close = self.find_elem('.message-popup-close')
            message_close.click()
            #time.sleep(0.2)
        except Exception as ex:
            print('关闭异常:%s' % ex)

    def is_filed_for_openagin(self, name):
        # '''表单是否已归档'''
        # 再次打开相应记录
        self.openagain_record(name)
        #time.sleep(0.5)
        # 判段是否已归档
        bool = self.find_elem('div#flow-panel>div.flow-status').get_attribute('display')
        return bool

    def is_filed(self):
        '''表单是否已归档'''
        bool = self.find_elem('div#flow-panel>div.flow-status').get_attribute('display')
        return bool

    def direct_sumit(self):
        # 直接提交
        # 点击提交按钮
        self.click_flow_processbtn()
        # 点击确认提交
        self.submit()

    def is_filed_for_aftersumbit(self, recordname):
        '''提交后判断流程是否已归档'''
        self.direct_sumit()
        bool = self.is_filed_for_openagin(recordname)
        return bool

    def logoff_and_openrecord(self, username, password, menu1, menu2, menu3, recordname):
        '''退出当前登录，切换账号并打开菜单记录for视图'''
        self.goback()
        self.switch_account(username, password)
        #time.sleep(0.3)
        self.close_message()
        # 打开菜单
        self.open_m(menu1, menu2, menu3)
        #time.sleep(0.5)
        self.openagain_record(recordname)

    def logoff_and_openmenu(self, username, password, menu1, menu2, menu3):
        '''退出当前登录，切换账号并打开菜单记录for表单'''
        self.goback()
        self.switch_account(username, password)
        self.close_message()
        # 打开菜单
        self.open_m(menu1, menu2, menu3)
        #time.sleep(0.5)

    def click_newbtn(self):
        '''点击新建按钮'''
        #time.sleep(0.5)
        btn = ButtonPage(self.driver)
        btn.click_button(btn.new_btn)
        self.wait_loading_hide() #等待loading加载完

    def click_rebackbtn(self):
        '''点击返回按钮'''
        btn = ButtonPage(self.driver)
        btn.click_button(btn.to_return)
        btn.wait_loading_hide() #表单中
        btn.wait_loading_hide() #视图中
        #time.sleep(0.1)

    def click_submit_star_flowbtn(self):
        '''点击提交_发起流程按钮'''
        btn = ButtonPage(self.driver)
        btn.click_button(btn.submit_star_flow)
        self.wait_elem_visible('#flowHtmlText')  # 等待提交面板展开

    def click_flow_processbtn(self):
        '''点击提交按钮'''
        btn = ButtonPage(self.driver)
        btn.click_button(btn.flow_process)
        self.wait_elem_visible('#flowHtmlText')  # 等待提交面板展开

    def click_starprocessbtn(self):
        '''点击保存并启动流程按钮'''
        btn = ButtonPage(self.driver)
        btn.click_button(btn.save_start)
        btn.wait_loading_hide()


    def click_savebtn(self):
        '''点击保存按钮'''
        btn = ButtonPage(self.driver)
        #time.sleep(0.5)
        btn.click_button(btn.save)
        btn.wait_loading_hide()
        #time.sleep(0.1)

    def switchto_designatedapprover(self):
        """切到指定审批人iframe"""
        div_iframe = self.find_elem('div.aui_loading+iframe')
        self.driver.switch_to.frame(div_iframe)

    def switch_to_formiframe(self):
        """返回到表单所在的iframe"""
        iframeMenu = self.find_elem("div.tab-pane.active>iframe")
        self.driver.switch_to.frame(iframeMenu)

    def logout(self):
        """退出登录"""
        above = self.find_elem('div.user-box>img')
        ActionChains(self.driver).move_to_element(above).perform()
        self.find_elem_is_clickable('ul.dropdown-menu>li.user-logout').click() #点击注销选择项
        self.find_elem_is_clickable('div.modal-content button.btn.btn-primary').click() #点击确定按钮

    def goback(self):
        """退出登录"""
        # 回到主文档，没有iframe
        self.driver.switch_to.default_content()
        # 退出登陆
        self.logout()

    def go_messagecenter_toclear(self):
        """进入消息中心清空工作事项通知"""
        # 回到主文档，没有iframe
        self.driver.switch_to.default_content()
        above = self.find_elem('div.user-box>img')
        ActionChains(self.driver).move_to_element(above).perform()
        #time.sleep(0.5)
        self.find_elem_visible('ul.dropdown-menu>li.user-message').click()
        # 进入消息中心的iframe
        self.driver.switch_to.frame(self.find_elem('div#message > iframe'))
        # 点击工作事项
        self.find_elem_visible('.list a[data-type="remind"]').click()
        # 点击标记已读
        if(self.find_elem_visible('.remind-btns')==None):
            for i in range(10):
                print('点击次数 %s'%i)
                self.find_elem_visible('.list a[data-type="remind"]').click()
                if(self.find_elem_visible('.remind-btns')!=None):
                    self.find_elem_visible('.remind-btns').click()
        else:
            self.find_elem_visible('.remind-btns').click()
        time.sleep(1)   #必须，等待页面刷新

    def get_messagecenter_totalRowPanel(self):
        '''获取消息中心的工作事项记录数'''
        elems = self.find_elems('.tab-pane>ul>li')
        if elems == None:
            return 0
        else:
            return len(elems)

    def go_messagecenter(self):
        """进入消息中心"""
        # 回到主文档，没有iframe
        self.driver.switch_to.default_content()
        above = self.find_elem('div.user-box>img')
        ActionChains(self.driver).move_to_element(above).perform()
        #time.sleep(0.5)
        self.find_elem('ul.dropdown-menu>li.user-message').click()
        #time.sleep(0.5)
        # 进入消息中心的iframe
        self.driver.switch_to.frame(self.find_elem('div#message > iframe'))
        # 点击工作事项
        self.find_elem('div.list li:nth-child(2)>a').click()

    def logoff_and_check_submitbtn(self, username, password, menu1, menu2, menu3, recordname):
        '''退出切换账号，查看是否有提交按钮'''
        self.goback()
        self.switch_account(username, password)
        self.close_message()
        self.open_m(menu1, menu2, menu3)
        # 再次打开相应记录查看是否有提交按钮
        bb = self.is_submit_existed(recordname)
        return bb

    def aftersumbit_getapprover(self, recordname):
        '''提交后再次打开表单获取流程处理人'''
        self.direct_sumit() #直接提交
        self.wait_loading_hide()
        #time.sleep(0.1)
        # 再次打开相应记录获取流程状态的处理人
        text2 = self.openagain_to_getapprover(recordname)
        #time.sleep(0.5)
        return text2

    def close_tab(self, name):
        """根据页签名关闭页签"""
        # 回到主文档，没有iframe
        self.driver.switch_to.default_content()
        #time.sleep(0.5)
        above = self.driver.find_element_by_link_text(name)
        ActionChains(self.driver).move_to_element(above).perform()
        #time.sleep(0.5)
        self.driver.find_element_by_link_text(name).click()
        #time.sleep(0.5)
        self.find_elem('li.navbar-tabs-item.selected a:nth-child(2)').click()

    def submit(self):
        """确定提交"""
        self.find_elem_is_clickable('div#div_button_place > button').click()
        self.wait_loading_hide() #等待loading消失

    def openagain_record(self, name):
        '''再次打开记录'''
        self.wait_loading_hide()  # 等待loading消失
        self.find_elem_is_clickable('td.listDataTrTd>a[title="'+name+'"]').click()
        self.wait_Tabloading_show_then_hide() #等待表单加载


    def get_approver(self):
        # 获取流程状态的处理人
        self.wait_loading_hide()  # 等待loading消失
        textlist = []
        target = self.find_elem_visible('div#flow-panel>div.flow-status')
        if(target==None):
            for i in range(10):
                print('等待次数 %s'%i)
                self.wait_elem_visible('div#flow-panel>div.flow-status')
                target2 = self.find_elem_visible('div#flow-panel>div.flow-status')
                if(target2!=None):
                    target2.click() #点击当前流程状态图标
        else:
            target.click()  # 点击当前流程状态图标
        list = self.find_elems_visible('span.flow-name>div.noAvatar')
        for li in list:
            textlist.append(li.text)
        return textlist

    def is_elementPresent(self):
        """判断有无提交按钮"""
        btn = ButtonPage(self.driver)
        if btn.is_button_visiable('提交'):
            return "true"
        else:
            return "false"

    def is_btn_existed(self, id):
        '''根据按钮的id检查是否存在此按钮'''
        try:
            self.find_elem('a[id="' + id + '"]')
            return True
        except Exception as e:
            return False

    def click_fallbackbtn(self):
        """点击流程回退按钮"""
        self.find_elem('a#act_flow_back').click()
        self.wait_loading_hide()
        #time.sleep(0.1)
        self.find_elem('button[name="btn_act_returnto"]').click()
        self.wait_loading_hide()

    def click_hangbtn(self):
        """点击挂起按钮"""
        self.find_elem('a#act_flow_retracement').click()
        self.wait_loading_hide()
        #time.sleep(0.1)

    def click_retracementbtn(self):
        """点击恢复按钮"""
        self.find_elem('a#act_flow_retracement').click()
        self.wait_loading_hide()
        #time.sleep(0.1)

    def click_retreatbtn(self):
        '''点击回撤按钮'''
        self.find_elem('a#act_flow_retracement').click()
        self.wait_loading_hide()
        #time.sleep(0.1)

    def click_button_by_id(self, id):
        '''根据按钮id点击按钮'''
        self.find_elem('a[id="' + id + '"]').click()
        self.wait_loading_hide()
        #time.sleep(0.1)

    def judge_delete(self, name):
        """判断是否已存在记录有则删除"""
        s = self.find_elems( 'td.listDataTrTd>a[title="' + name + '"]')
        if len(s) >= 1:
            print("记录已存在，需要删除")
            self.find_elem('td.listDataThFirstTd > input[type="checkbox"]').click()
            btn = ButtonPage(self.driver)
            btn.click_button(btn.del_btn)
            self.driver.switch_to_alert().accept()
            #time.sleep(0.5)
        else:
            print("记录不存在，不需要删除")

    def click_terminationbtn(self):
        """点击终止流程"""
        self.find_elem('a#act_flow_termination').click()
        # 回到主文档，没有iframe
        self.driver.switch_to.default_content()
        self.find_elem('div.aui_main > div > div:nth-child(2) > textarea').send_keys("终止流程")
        #time.sleep(0.5)
        self.find_elem_visible('div.aui_buttons > button.aui_state_highlight').click() #点击终止流程确定按钮
        self.switch_to_formiframe()

    def select_approver(self, title):
        """根据角色名添加审批人"""
        self.find_elem_visible('a#act_flow_editAuditor').click()
        # 回到主文档，没有iframe
        self.driver.switch_to.default_content()
        # 切到指定审批人iframe
        comp = ProcessApproverPage(self.driver)
        comp.switchto_designatedapprover()
        self.find_elem_visible('div.leftContent>div div[title="' + title + '"]').click()
        self.find_elem_visible('input#addAll').click()
        self.find_elem_visible('div>input#doReturn').click()
        comp.switch_to_formiframe()

    def select_user_by_rolename(self, title):
        '''根据角色名选择用户'''
        # 点击指定审批人选择框
        self.find_elem_visible('span.copyToPerson>img').click()
        # 回到主文档，没有iframe
        self.driver.switch_to.default_content()
        # 切到指定审批人iframe
        comp = ProcessApproverPage(self.driver)
        comp.switchto_designatedapprover()
        self.find_elem_visible('div.leftContent>div div[title="' + title + '"]').click()
        self.find_elem_visible('input#addAll').click()
        self.find_elem_visible('div>input#doReturn').click()
        self.driver.switch_to.default_content()
        self.wait_elem_disappear('#lock_screen_div>div') #等待确认后的灰色锁屏消失

    def get_messagecentercontent(self):
        '''获取消息中心的工作事项内容'''
        self.go_messagecenter()
        text = self.find_elem('div.remind-list-content>a').text
        return text

    def send_reminder(self, content):
        '''发起催办'''
        self.click_button_by_id("act_flow_reminder")
        self.find_elem('section.flow-reminder-panel-attitude>textarea').clear()
        self.find_elem('section.flow-reminder-panel-attitude>textarea').send_keys(content)
        #time.sleep(0.5)
        self.find_elem_is_clickable('div.button-css.flow-reminder-panel-footer>a.btn').click()

    def open_usefulopinionsboard(self):
        # 点击展开常用意见
        self.find_elem_is_clickable('span#fieldset_remark_usual>i.fa').click()

    def select__usefulopinions(self, name):
        # 点击常用意见的值
        self.find_elem_visible('section#commonOpinions>ul>li>a[title="' + name + '"]').click()

    def judgedel_usefulopinions(self, name):
        # 根据内容判断常用意见是否存在
        if self.find_elem('section#commonOpinions>ul>li>a[title="' + name + '"]')!=None:
            print("存在相同的意见，需要删除")
            self.del_usefulopinions(name)
        else:
            print("不存在相同意见，不需要删除")

    def click_editFlowbtn(self):
        '''点击前台流程调整按钮'''
        self.find_elem_visible('a#act_flow_editFlow').click()

    def get_popuptitle(self):
        '''获取弹出框的title'''
        text = self.find_elem_visible('div.aui_header > span.aui_title').text
        return text

    def is_embed_visit(self):
        '''判断embed是否可见'''
        time.sleep(3)   #等待flash渲染完成
        return self.is_element_visible('#WorkFlowDiagram > embed')


    def get_usefulopinionsval(self):
        # 获取意见面板的内容
        text = self.find_elem_visible('textarea[name="_attitude"]').get_attribute('value')
        return text

    def get_usefulopinions_count(self):
        # 获取意见面板的字数
        count = self.find_elem_visible('div#textarea_counter>span.count').text
        return count

    def add_usefulopinions(self, content):
        # 点击添加新常用意见
        self.find_elem_is_clickable('div.addBtn>i.fa').click()
        self.find_elem_visible('section#commonOpinions>ul>div.edit>input').send_keys(content)
        self.find_elem_is_clickable('section#commonOpinions>ul>div.edit>span.save').click()
        self.wait_loading_hide()
        #time.sleep(0.5)

    def del_usefulopinions(self, content):
        # 根据内容删除常用意见
        # 点击编辑常用意见
        self.find_elem_is_clickable('div.editBtn>i.fa').click()
        self.find_elem_is_clickable(
            'section#commonOpinions>ul>li>a[title="' + content + '"]+a.editSub+a.del').click()
        #time.sleep(0.5)
        self.find_elem_is_clickable('section#commonOpinions>ul>div.edit>span.cancel').click()

    def select_user(self,title):
        '''自由流程选择用户'''

        # 点击打开审批人选择界面
        self.find_elem_visible('.flow-submit__user-avatar').click()
        # 切出iframe
        mp = MainPage(self.driver)
        mp.switch_to_parent()
        # 切换到选择审批人的iframe
        self.switchto_designatedapprover()
        self.wait_elem_visible('#lock_screen_div')
        # 选择审批人
        self.find_elem_visible('div.leftContent>div div[title="' + title + '"]').click()
        self.find_elem_visible('input.list_div_click').click()
        self.find_elem_visible('div>input#doReturn').click()
        # 等待确认后的灰色锁屏消失
        self.driver.switch_to.default_content()
        self.wait_elem_disappear('#lock_screen_div>div') #等待确认后的灰色锁屏消失
        # 返回到表单所在的iframe
        self.switch_to_formiframe()


    def is_flow_end(self):
        '''自由流程是否已经结束'''
        return self.find_elem('div#flow-panel>div.flow-status span').get_attribute('aria-hidden')

    def click_messagecenter_freeflow(self):
        '''点击在消息中心的自由流程'''
        if '自由流程' in self.get_messagecentercontent():
            self.find_elem_visible('div.remind-list-content>a').click()

    def click_backoff_btn(self):
        '''点击回退按钮'''
        # 切出iframe
        self.driver.switch_to.default_content()
        # 切到当前打开的页面
        self.switch_to_formiframe()
        self.find_elem_is_clickable('a#act_flow_backOff').click()
        self.wait_elem_visible('#flowHtmlText') #等待提交面板展开



    def select_backoffuesr_by_name(self,title):
        #选择回退审批人
        target = self.find_elem_visible('#rightcontent>.list_div>input[name="' + title + '"]+span')
        if(target==None):
            for i in range(10):
                print('target==None次数 %s' %i)
                target2 = self.find_elem_visible('#rightcontent>.list_div>input[name="' + title + '"]+span')
                if(target2!=None):
                    target2.click()
                    if(self.find_elem('#rightcontent>.list_div>input[name="' + title + '"]').is_selected()):
                        break
        else:
            for i in range(10):
                print('选中次数 %s' % i)
                target.click()
                if (self.find_elem('#rightcontent>.list_div>input[name="' + title + '"]').is_selected()):
                    break
        self.wait_elem_visible('#rightcontent>.list_div>input[name="' + title + '"]')

    def backoff_select_approver(self,title):
        '''回退选择审批人'''
        # 点击打开审批人选择界面
        self.find_elem_visible('.flow-submit__user-avatar').click() #点击选择添加流程审批人+号
        # 切出iframe
        mp = MainPage(self.driver)
        mp.switch_to_parent()
        # 切入选择用户iframe
        self.switchto_designatedapprover() #切到指定审批人iframe
        self.wait_elem_visible('#rightcontent>.list_div') #等待审批人框展开
        self.select_backoffuesr_by_name(title)#选择审批人
        self.find_elem_visible('#doReturn').click()
        # 等待确认后的灰色锁屏消失
        self.driver.switch_to.default_content()
        self.wait_elem_disappear('#lock_screen_div>div') #等待确认后的灰色锁屏消失
        # 返回到表单所在的iframe
        self.switch_to_formiframe()

    def click_end_flow(self):
        '''点击结束流程'''
        target = self.find_elem_visible('#act_flow_complete')
        if(target==None):
            for i in range(10):
                print('等待秒数 %s'%i)
                self.wait_elem_visible('#act_flow_complete',timeout=1)
                target2 = self.find_elem_visible('#act_flow_complete')
                if(target2!=None):
                    target2.click()
                    break
        else:
            target.click()
        self.wait_elem_visible('#flowHtmlText')  # 等待提交面板展开

    def is_flow_actbutton_exist(self, name):
        '''判断流程按钮是否还存在   存在返回-Ture  不存在返回-False'''
        btn = ButtonPage(self.driver)
        return btn.is_button_visiable(name)

class FlowPhonePage(PhonePage, SuperFlowPage):
    '''手机端流程处理page'''

    def click_flow_more(self):
        '''点击更多获取流程历史'''
        self.find_elem_visible('span.td.more').click()

    def get_flow_history_useopinions(self):
        '''获取流程历史中的审批意见'''
        result = self.find_elem('.talk-box div:nth-child(2)')
        return result.text

    def is_flow_end(self):
        '''判断流程是否已经结束'''
        name = '归档'
        lis = self.find_elements('.start-node-name')
        for li in lis:
            if li.text == name:
                return True
        return False

    def flow_sumit(self):
        '''手机端点击流程面板的提交'''
        self.wait_flow_node_show()
        bt = ButtonPhonePage(self.driver)
        bt.click_flowpanel_button('提交')

    def wait_confirmPanel_visible(self):
        """等待终止流程警告框可见"""
        self.wait_elem_visible('.confirmPanel.animated.bounceIn')

    def sendkey_in_confirmPanel_textarea(self, title):
        """往终止流程警告框输入原因"""
        self.find_elem('#confirmPanel > div.contenter > p > textarea').send_keys(title)  # 输入终止原因
        self.find_elem_visible('#confirmPanel > div.foot > a.btn.pull-right.btn-link.red.btn-delete').click()  # 点击确定
        self.wait_Tabloading_show_then_hide()

    def get_cur_flow_state(self):
        """判断流程状态"""
        text = self.find_elem('#flowhis_modal_content > div.leave-list:nth-child(1) div.state').text  # 获取当前的流程状态
        print('state' + text)
        lists = text.split('流转')
        state = lists[1]
        return state

    def wait_flow_node_show(self):
        '''等待提交面板的流程节点显示'''
        self.wait_elem_visible('#flow-submit__node-box > div > label')

    def click_flow_submit_user_avatar(self):
        """点击选择流程审批人"""
        self.wait_flow_node_show()  # 等待提交面板的流程节点显示
        self.find_elem_visible('.flow-submit__user-select').click()  # 点击选择流程审批人

    def click_flow_copyTo(self):
        """点击选择抄送人"""
        self.wait_flow_node_show()  # 等待提交面板的流程节点显示
        self.find_elem_visible('.flow-submit__user-avatar.flow-submit__user-select').click()  # 点击选择抄送人

    def is_flow_copyTo_exsit(self):
       """是否存在抄送按钮"""
       try:
           self.find_elem('.weui-cells.weui-cells_checkbox.flow-submit__copyTo')
           return True
       except:
           return False

    def get_curnode_user(self):
        """获取当前 节点审批人"""
        self.wait_Tabloading_show_then_hide()
        box = self.find_elems('.flowhis_panel_hisnode span.face-box')
        return box[-1].text   # 当前节点审批人

    def get_nodes_checked_stable(self):
        '''获取所有流程节点的单选框状态'''
        test_elements_attr_list = []
        nodes = self.find_elems('.weui-check')
        for node in nodes:
            if node.is_selected() == True:
                test_elements_attr_list.append(True)
            elif node.is_selected() == False:
                test_elements_attr_list.append(False)
        return test_elements_attr_list

    def is_flowReminderDiv_visiable(self):
        '''是否弹出催办框'''
        try:
            WebDriverWait (self.driver, timeout=3).until (
                EC.visibility_of_element_located ((By.CSS_SELECTOR, '.flowReminderDiv')))
        except Exception as ex:
            print('弹出催办框 异常：%s' % ex)

    def get_flowReminder_title(self):
        '''判断催办框是否正常显示'''
        self.is_flowReminderDiv_visiable()
        return self.find_elem('#flowReminderDiv strong').text

    def sendkey_for_flowReminder(self,content):
        '''输入催办内容点击确定'''
        self.find_elem('.flowReminder_content').send_keys(content)
        self.find_elem_visible('#flowReminderDiv a.weui_btn_dialog.primary.flowReminder_submit').click()
        self.wait_Tabloading_show_then_hide()





