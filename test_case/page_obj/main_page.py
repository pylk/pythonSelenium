import time
import sys

sys.path.append('../../')
from random import choice
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from test_case.page_obj.page import Page
from test_case.page_obj.page import PhonePage
from test_case.page_obj.button_page import ButtonPage


class MainPage(Page):
    '''主页测试'''

    def get_menu(self, text):
        menu = self.find_elem('#tabs_menu li > a[title="' + text + '"]')
        return menu


    def menu_scroll_to(self, y):
        '''滚动到菜单的指定位置'''
        script = '$("#wrapper>.sidebar").find(".menu").slimscroll({scrollTo: "' + y + '"})'
        self.driver.execute_script(script)

    def open_menu(self, text):
        print('主页打开链接：%s' % text)
        time.sleep(0.5)  # 菜单展开时有动态过渡效果，必须等待
        a = self.get_menu(text)
        if a == None:
            time.sleep(3)  # 程序运行久了有时候加载菜单会慢，休息3秒
            a = self.get_menu(text)

        self.scroll_to_target_element(a)
        a.click()


    def flowcenter_scroll_to(self, yy):
        script = 'var $con = $(".startflow-content-box");' \
                 'if($con.size()>0)$con.getNiceScroll(0).doScrollTop(' + yy + ',10)'
        # 滚动到控件可以看到后面的代码执行才不会报错
        self.driver.execute_script(script)

    def scroll_to_viewport_4_form(self, elem):
        '''执行js脚本，操作滚动条滚动到离页面顶部y值的位置'''
        try:
            win_size = self.find_elem('#startflow').size
            win_h = win_size['height']
            self.flowcenter_scroll_to('0')

            elem_y = elem.location['y']
            elem_h = elem.size['height']
            if elem_y != 0 and elem_h != 0:
                top_to = 0
                if elem_y + elem_h > win_h:  # 元素没有完全显示在界面中时
                    top_to = elem_y - 42 - 17
                    top_to = str(top_to)
                    self.flowcenter_scroll_to(top_to)
        except Exception as ex:
            print('page.scroll_to_viewport_4_form异常：%s' % ex)

    def refresh_main(self):
        print('刷新主页')

        self.driver.refresh()

    def switch_to_parent(self):
        '''退出表单至根页面 '''
        self.driver.switch_to.default_content()

    def switch_to_grid_iframe(self):
        '''切换到网格视图下的iframe'''
        # 在选项卡下，是嵌套在iframe下
        grid_iframe = self.find_elem('div.tabcontent>span>iframe')
        self.driver.switch_to.frame(grid_iframe)

    def switch_to_div_iframe(self):
        '''切换到弹出层内部--在最外层打开弹出层时'''
        self.switch_to_parent() #退出表单至根页面
        # 找到弹出层中的iframe并切换
        div_iframe = self.find_elem('div.aui_content > iframe')
        self.driver.switch_to.frame(div_iframe)
        # 再找到内部iframe并切换
        body_iframe = self.find_elem('body > iframe')
        if body_iframe!=None:
            self.driver.switch_to.frame(body_iframe)
        else:
            print('打开弹出层内的iframe异常：%s')

    def delete_all_data(self):
        '''清空所有数据'''
        bp = ButtonPage(self.driver)
        self.find_elem('.listDataThFirstTd').click()
        bp.click_button(bp.del_btn)
        self.click_alert_accept()
        self.wait_loading_hide()

    def over_widget_action(self,title):
        '''鼠标悬停在widget操作栏上'''
        targets = self.find_elems_visible('#portal div.itemHeader>span+span')
        for target in targets:
            if(target.text==title):
                ActionChains(self.driver).move_to_element(target).perform()

    def over_userbox(self):
        '''鼠标悬停在用户设置上'''
        # 鼠标悬停在用户设置头像上
        userbox = self.find_elem('.navbar-menu>.top-user>.user-box')
        ActionChains(self.driver).move_to_element(userbox).perform()

    def get_userbox_return_class(self):
        # 鼠标悬停在用户设置显示隐藏区域，class变成含有open
        userbox = self.find_elem('.navbar-menu>.top-user>.user-box')
        return userbox.get_attribute('class')

    def open_message_center(self):
        '''打开消息中心'''
        self.find_elem('.user-message>  a[title="消息中心"]').click()

    def check_message_number(self):
        '''检查用户设置显示数目与消息中心数目相等'''
        # 获取头像右上角数值
        headNum = self.find_elem('.user-box > span')
        # 获取消息中心右侧数值
        messageNum = self.find_elem('a[title="消息中心"]>span')
        # print('====%r' %headNum.text)
        # 比较两个值是否相等，返回
        return headNum.text == messageNum.text

    def get_message_center_return(self):
        # 获取消息中心打开页面中固定显示的元素
        message = self.find_elem_visible('.msg-menu-item.active > a')
        return message.text

    def open_user_setting(self):
        '''打开个人设置'''
        self.find_elem_is_clickable('.user-person-setting> a').click()

    def get_user_setting_return(self):
        # 获取个人设置打开页面中的固定元素
        setting = self.find_elem('#uBaseInfo')
        return setting.text

    def open_logout(self):
        '''注销'''
        self.find_elem('.user-logout> a').click()

    def get_user_logout_return(self):
        # 获取注销打开页面中的固定元素
        time.sleep(0.5) #必须
        cancle = self.find_elem('.modal-body')
        # print('cancle.text==%r' % cancle.text)
        return cancle.text

    def IsEnterpriseAdmin_return(self):
        '''校验企业管理员配置'''
        # 获取下拉菜单中是否含有“管理”
        isEA = self.find_elem('#manageDomain')
        return isEA.text

    def open_enterprise_admin(self):
        '''打开管理'''
        self.find_elem('#manageDomain').click()

    def get_EnterpriseAdmin_return(self):
        # 获取管理打开页面的固定元素
        oea = self.find_elem('#activityTable td')
        return oea.text

    def switch_nav_1(self):
        '''切换多页签'''
        self.find_elem('.navbar-tabs-ul> li:nth-child(2)').click()

    def switch_nav_2(self):
        time.sleep(0.5) #必须
        self.find_elem('.navbar-tabs-ul> li:nth-child(3)').click()

    def get_switchnav_1_return(self):
        sn1 = self.find_elem('.flowEnd')
        return sn1.text == '未完结的'

    def get_switchnav_2_return(self):
        sn2 = self.find_elem('#flowtitle')
        return sn2.get_attribute('placeholder') == '主题'

    def close_nav_by_select(self):
        '''根据当前打开关闭多页签'''
        # 获取所有多页签的内容
        navl = self.find_elems('.navbar-tabs-ul li')
        for nav in navl:
            if 'selected' in nav.get_attribute('class'):
                ActionChains(self.driver).move_to_element(nav).perform()
                time.sleep(0.5) #必须
                nav.find_element_by_css_selector('.navbar-tabs-item.selected .tab-btn-close').click()

    def close_current_nav(self):
        '''关闭当前打开的页签'''
        try:
            nav = self.find_elem('.navbar-tabs-ul > li.selected')
            ActionChains(self.driver).move_to_element(nav).perform()
            time.sleep(0.5) #必须
            nav.find_element_by_css_selector('.navbar-tabs-item.selected .tab-btn-close').click()
        except Exception as ex:
            print('关闭当前页签获取页签异常：%s' % ex)

    def nav_close_click(self):
        '''点击关闭多页签'''
        nc = self.find_elem('.navbar-tabs-ul> li:nth-child(2)')
        ActionChains(self.driver).move_to_element(nc).perform()
        time.sleep(0.5) #必须
        self.find_elem('.navbar-tabs-ul> li:nth-child(2)>a.tab-btn-close').click()

    def get_navclose_click_return(self):
        '''如果找到元素则返回flase'''
        if self.find_elem('#flowtitle')!=None:
            return False
        else:
            return True

    def is_nav_close_exist(self):
        '''鼠标悬浮多页签关闭出现'''
        nce = self.find_elem('.navbar-tabs-ul> li:nth-child(2)')
        ActionChains(self.driver).move_to_element(nce).perform()
        time.sleep(0.5) #必须

    def get_isnavclose_exist_return(self):
        '''获取关闭按钮'''
        try:
            self.find_elem('.navbar-tabs-ul> li:nth-child(2)>a.tab-btn-close')
            return True
        except Exception as ex:
            print('获取关闭按钮异常:%s' % ex)
            return False

    def get_nav_preview_return(self):
        navs = self.find_elems('.navbar-tabs-ul>li')
        # print('len(navs)=%r' %len(navs))
        np = self.find_elem('#navbar-tabs-preview a span')
        # print('preview = %r' % int(np.text))
        npc = self.find_elems('.tabs-preview-panel>li')
        # print('preview list = %r' %len(npc))
        if len(navs) == int(np.text) and int(np.text) == len(npc):
            return True
        else:
            return False

    def open_preview(self):
        '''打开多页签预览'''
        self.switch_to_parent()
        self.find_elem_is_clickable('#navbar-tabs-preview').click()


    def get_open_preview_return(self):
        op1 = self.find_elem('.slimScrollDiv > ul > li:nth-child(1)')
        op2 = self.find_elem('.slimScrollDiv > ul > li:nth-child(2)')
        return op1.text == '主页' and '发起新建' in op2.text

    def nav_closs_all(self):
        '''关闭全部窗口'''
        self.find_elem_is_clickable('.nav-closeAll-btn').click()

    def get_nav_clossall_return(self):
        nc = self.find_elem_visible('#tabs_flowcenter h5')
        return nc.text

    def click_preview_page(self):
        '''打开一个缩略图'''
        self.find_elem_is_clickable('.tabs-preview-panel>li:nth-child(2)').click()

    def nav_closs_one(self):
        '''关闭一个缩略图'''
        self.find_elem_is_clickable('#tabsPreview .active.animatedFast.zoomIn > span').click()

    def widget_summary(self):
        '''摘要'''
        ws = self.find_elem_visible('.widget-summary >.itemHeader > span:nth-child(2)',timeout=10)
        return ws.text

    def restore_configure(self):
        '''还原配置'''
        self.find_elem_visible('#header span.configImg').click() #点击设置按钮
        self.find_elem_visible('td.single>a:nth-child(2)').click() #点击重置按钮
        time.sleep(1)

    def widget_view_icon(self):
        '''打开视图_图标'''
        self.fast_entry('视图_icon')

    def get_view_icon_return(self):
        vi = self.find_elem_visible('.table-head td:nth-child(2)')
        return vi.text

    def widget_view(self):
        '''打开视图'''
        time.sleep(0.5) #必须
        wv = self.find_elem('.widget-view >.itemHeader > span:nth-child(2)')
        wvc = self.find_elem('.itemContent tbody td:nth-child(1)')
        if (wv.text == '视图' and wvc.text == '文本一'):
            return True
        else:
            return False

    def fast_entry_font(self):
        '''打开widget_快速入口'''
        time.sleep(0.5) #必须
        self.find_elem_is_clickable('.widgetItem.link').click()

    def get_fastentry_font_return(self):
        time.sleep(0.5) #必须
        fe = self.find_elem_visible('#u1 > a:nth-child(1)')
        return fe.text

    def fast_entry(self, name):
        '''打开快速入口方法'''
        # 取整个快速入口的列表
        feis = self.find_elems('.icon_p.ui-sortable>a')
        for names in feis:
            # 如果存在与传入参数相等的名称，则点击并退出循环
            if (names.text == name):
                names.click()
                break

    def fast_entry_img(self):
        '''打开widget_快速入口_图片'''
        self.fast_entry('快速入口_icon')

    def ageing_report(self):
        '''打开widget_时效报表'''
        self.fast_entry('时效报表_icon')

    def get_ageing_report_return(self):
        ar = self.find_elem('#summaryReport tr:nth-child(1) .commFont')
        return ar.text

    def img_report(self):
        '''打开widget_图形报表'''
        self.fast_entry('图形报表_icon')

    def get_img_report_return(self):
        ar = self.find_elem('#oReport > embed')
        return '.swf' in ar.get_attribute('src')

    def link_contect_icon(self):
        '''打开链接内容_图标'''
        self.fast_entry('链接内容_icon')

    def get_linkcotect_icon_return(self):
        lci = self.find_elem_visible('#_formHtml > p:nth-child(1)')
        return lci.text

    def widget_calculate_script(self):
        '''计算脚本值'''
        # 拿到所有widget_div
        lis = self.find_elems('.groupItem.ui-sortable-handle')
        for li in lis:
            # 找第一个div里面的span值判断
            tl = li.find_element_by_css_selector('.itemHeader>span:nth-child(2)')
            if (tl.text == '计算脚本'):
                # 找第二个div里面的a点击
                self.scroll_to_target_element(li)
                li.find_element_by_css_selector('.itemContent a').click()
                break

    def click_homepage_setting(self):
        '''点击打开收起主页设置'''
        self.find_elem_is_clickable('.configImg').click()
        self.wait_elem_visible('.single')

    def get_hpset_return(self):
        '''返回主页设置列表是否不可见，是则返回Ture,否则返回FALSE'''
        return self.is_elem_invisibility('.form-list')


    def homepage_icon_link_set(self):
        '''homepage 图标链接设置'''
        ilss = self.find_elems('.form-list tr:nth-child(2) li')
        # 从一个列表中产生一个随机值  from random import choice
        rc = choice(ilss).find_element_by_css_selector('a')
        rc.click()
        # print('======%r' %rc.text)
        time.sleep(0.5) #必须
        # 取所有快速入口的名称
        feis = self.find_elems('.icon_p.ui-sortable>a')
        for names in feis:
            self.scroll_to_target_element(names)
            return names.text == rc.text

    def homepage_module_set(self):
        '''homepage 模块设置'''
        ms = self.find_elems('.form-list tr:nth-child(3) li')
        rc = choice(ms).find_element_by_css_selector('a')
        rc.click()
        time.sleep(0.5) #必须
        # 取所有widget的名称
        wlis = self.find_elems('.itemHeader > span:nth-child(2)')
        for names in wlis:
            self.scroll_to_target_element(names)
            return names.text == rc.text

    def check_widget_iscript_hight(self):
        '''检查计算脚本的高度'''
        time.sleep(0.5) #必须
        lis = self.find_elems('.groupItem.ui-sortable-handle')
        for li in lis:
            tl = li.find_element_by_css_selector('.itemHeader>span:nth-child(2)')
            if (tl.text == '计算脚本-高度'):
                div = li.find_element_by_css_selector('.itemContent div')
                # 获取div的大小
                sz = div.size
                # print(sz)
                # 获取div的style的height的值
                sth = div.value_of_css_property('height')
                # print(sth)
                # 获取返回大小字典的键值对，如果没有则显示not found
                # print(sz.get('height','not found'))
                # 键值对获取height的只为int，转换成str做判断
                return str(sz.get('height', 'not found')) in sth

    def widget_linkcontect_imgicon(self,text):
        '''检查链接内容图片图标'''
        time.sleep(0.5) #必须
        lis = self.find_elems_visible('.itemHeader>span+span')
        for li in lis:
            if li.text != text:
                continue
            else:
                return True
        return False

    def only_widget_by_name(self,name):
        #设置主页只有name widget
        time.sleep(0.5)  # 必须
        # 获取所有widget打开设置
        wigs = self.find_elems('.form-list tr:nth-child(3) li')
        for wig in wigs:
            if wig.text != name:
                # 把name以外的widget关闭
                wig.click()
        # 切换布局
        # 点击布局 1
        self.find_elem_is_clickable('.layout-list li:nth-child(1)').click()
        # 点击保存
        self.click_save_setting()
        self.wait_elem_disappear('.single')

    def widget_weather_change_city(self):
        '''天气预报转换城市'''
        self.only_widget_by_name('天气预报')
        # 点击刷新
        rout = self.find_elem('.itemHeader')
        ActionChains(self.driver).move_to_element(rout).perform()
        rout.find_element_by_css_selector('.action>a:nth-child(1)').click()
        # 点击切换按钮
        self.find_elem_is_clickable('.weather-city-change').click()
        # 下拉框中的城市列表
        city = self.find_elems('.prov option')
        # 点击展开下拉框
        self.find_elem_is_clickable('select.prov').click()
        for cc in city:
            if (cc.text == '石家庄'):
                cc.click()
#                 print(cc.text)
                # 点击确定切换
                self.find_elem_is_clickable('#weather-city-btn').click()
                ncn = self.find_elem('.weather-city-name')
                result = ncn.text
                # 点击打开homepage设置
                self.click_homepage_setting()
                # 点击重置
                self.click_reset_setting()
                return result == '石家庄'

    def widget_operation(self):
        '''widget 刷新/折叠/展开/关闭 操作'''
        self.delete_all_data() #清空视图记录
        self.find_elem('#activityTable .btn-primary').click() #点击新建按钮
        self.driver.find_element_by_name('文本一').send_keys('testing111')  #给文本框输入值
        self.find_elem('#act .btn-success').click()  #点击保存按钮
        self.switch_to_parent()
        self.find_elem('.navbar-tabs-panel li:nth-child(1)').click()  #点击主页标签
        self.switch_to_iframe()
        lis = self.find_elems('.groupItem.ui-sortable-handle')  #获取所有的widget
        for li in lis:
            tl = li.find_element_by_css_selector('.itemHeader>span:nth-child(2)')
            if (tl.text == '视图'):
                # 悬浮在视图的标题栏显示操作按钮
                rout = li.find_element_by_css_selector('.itemHeader')
                ActionChains(self.driver).move_to_element(rout).perform()
                rout.find_element_by_css_selector('.action>a:nth-child(1)').click()
                vr = li.find_element_by_css_selector('.itemContent td:nth-child(1) div:nth-child(1)')
                reflesh = vr.text == 'testing111'
                rout.find_element_by_css_selector('.action>a:nth-child(2)').click()
                fold = vr.text == 'testing111'
                rout.find_element_by_css_selector('.action>a:nth-child(3)').click()
                op = vr.text == 'testing111'
                rout.find_element_by_css_selector('.action>a:nth-child(4)').click()
                for li in lis:
                    tl = li.find_element_by_css_selector('.itemHeader>span:nth-child(2)')
                    close = tl.text == '视图'
                    return reflesh == True and fold == False and op == True and close == False

    def click_save_setting(self):
        '''点击保存配置按钮'''
        self.find_elem('.form-list tr:nth-child(4) .single a:nth-child(1)').click()

    def click_reset_setting(self):
        '''点击重置配置按钮'''
        self.find_elem('.form-list tr:nth-child(4) .single a:nth-child(2)').click()

    def click_cancel_setting(self):
        '''点击取消操作按钮'''
        self.find_elem('.form-list tr:nth-child(4) .single a:nth-child(3)').click()

    def click_the_text_icon(self, text):
        '''点击传入文本的icon图标'''
        ilss = self.find_elems('.form-list tr:nth-child(2) li')  # 获取所有图标链接设置的选项
        for il in ilss:
            cl = il.find_element_by_css_selector('a')
            if (cl.text == text):
                cl.click()
                break

    def is_text_in_icons(self, text):
        '''快速入口图标中是否包含传入的这个文本图标'''

        fas = self.find_elems('#portal_i>a')
        x = []
        for name in fas:
            x.append(name.text)
        return text in x

    def homepage_setting_layout(self):
        '''切换homepage布局设置'''
        lys = self.find_elems('.layout-list li')
        for ly in lys:
            if (ly.text == '1'):
                ly.click()
                time.sleep(5)
                if(self.is_element_in_dom("#portal>.w00")):
                    return True
                else:
                    return False
                # divl = self.find_elem('#portal_l')
                # divr = self.find_elem('#portal_m')
                # print('%s'%divl.size.get('width', 'not found'))
                # print('%s'%divr.size.get('width', 'not found'))
                # return divl.size.get('width', 'not found')/ divr.size.get('width', 'not found') == 2

    def div_is_close(self):
        '''弹出层是否关闭'''
        self.switch_to_parent()
        elem = self.find_elem('.aui_state_focus')
        if elem == None:
            return True
        else:
            return False

    def div_getshare_message(self):
        '''获取表单保存等操作后返回的提示信息'''
        msg = self.find_elem('#transparent_message ').text
        return msg

    def click_flowcenter(self):
        '''点击流程中心'''
        #time.sleep(0.5)
        self.find_elem_is_clickable('#tabs_flowcenter .nav-header').click()
        self.wait_elem_visible('#flowMeun>li[data-title="仪表分析"] span') #等待流程中心面板展开

    def check_flowcenter(self):
        # 获取流程中心展开列表的第一项
        cf = self.find_elem('#flowMeun > li:nth-child(1)')
        return cf.text

    def open_new_built(self):
        '''打开发起新建'''
        self.find_elem_is_clickable('#flowMeun > li[data-title="发起新建"] span').click()
        self.switch_to_iframe()
        self.wait_elem_visible('input[placeholder="请输入搜索内容"]')

    def get_new_built_return(self):
        # 获取发起新建打开页面的固定元素
        nb = self.find_elem('#startflow-search')
        return nb.get_attribute('placeholder')

    def flowcenter_ergodic(self, list):
        # 遍历流程中心-发起新建的所有表单 打开3次
        count = 0
        isopen = []
        flag = True
        for nb in list:
            if count < 3:
                nba = nb.find_element_by_css_selector('a')
                self.scroll_to_target_element(nba) #滚动到对应的菜单
                nb.click() #点击菜单
                self.switch_to_parent() #返回到底层iframe
                self.switch_to_iframe() #切换到打开的iframe页面
                    # 检查页面是否正常打开
                if self.find_elem('#toAll')!=None: # #toAll表单div定位器
                    isopen.append(flag)
                else:
                    print('遍历流程中心-发起新建的所有表单异常:%s')
                    flag = False
                    isopen.append(flag)
                self.switch_to_parent()
                # 关闭当前打开的页签
                self.close_nav_by_select()
                self.switch_to_iframe()
                count = count + 1
        return 'False' in isopen

    def check_new_built(self):
        '''流程中心-发起新建-列表遍历打开'''
        # 获取新建中的所有菜单
        nblist = self.find_elems('.menu-li.visible')
        # 遍历打开关闭列表表单
        self.flowcenter_ergodic(nblist)

    def switch_new_built_icon(self):
        '''流程中心-发起新建-图标遍历打开'''
        # 从列表显示切换到图标显示
        self.find_elem('.btn-startflow:nth-child(2)').click()
        time.sleep(0.5) #必须
        # 获取所有新建中的图标
        icon_list = self.find_elems('.menu-li-icon')
        # 遍历打开关闭图标表单
        self.flowcenter_ergodic(icon_list)

    def close_righttop_message(self):
        # 检查有没有消息提示，如有关闭，如没有直接print(不在iframe中)
        try:
            message_close = self.find_elem('.message-popup-close')
            message_close.click()
            #time.sleep(0.2)
        except Exception as ex:
            print('关闭消息提示异常:%s' % ex)

    def new_built_search(self):
        '''流程中心-发起新建-搜索'''
        self.find_elem_visible('button[data-view="list"]').click()
        time.sleep(1)
        # 搜索框输入
        self.find_elem_visible('#startflow-search').send_keys('复选框')
        # 回车触发搜索
        self.wait_elem_invisibility('.menu-nolink') #等待菜单列头消失
        time.sleep(5)
        tf = []
        # 获取所有状态为可见的li
        check_seach = self.find_elems_visible('li.menu-li.visible')
        if(len(check_seach)==1 and check_seach[0].text=='复选框'):
            return True
        else:
            return False

    def open_todo_list(self):
        '''打开我的代办'''
        self.find_elem_is_clickable('#flowMeun > li[data-title="我的待办"] span').click()
        self.wait_Tabloading_show_then_hide()

    def get_todo_list_return(self):
        # 获取我的待办打开页面的固定元素
        tl = self.find_elem('#flowtitle')
        return tl.get_attribute('placeholder')

    def Is_number_Int(self, num):
        # 判断数值是否为正整数
        return isinstance(int(num), int)

    def check_todolist_number(self):
        '''流程中心-我的待办-数值显示'''
        # 获取我的待办中数值
        nums = self.find_elems('#flowAccordion .sum')
        tf = []
        for num in nums:
            # 非数值的字符转化int返回为False
            tf.append(self.Is_number_Int(num.text))
        # print(tf)
        return 'False' in tf

    def switch_todo_list(self):
        '''流程中心-我的待办-切换待办'''
        # 获取我的待办列表
        stls = self.find_elems('#flowAccordion li')
        # 存放遍历的id
        x = []
        # 存放返回的结果
        result = []
        # 循环比较后两个唯一的id，相等就是没有切换成功
        for stl in stls:
            # 点击切换我的待办
            time.sleep(0.5) #必须
            self.wait_loading_hide()
            stl.click()
            tr = self.find_elem('.tbody_tr')
            # 获取第一列的唯一id
            x.append(tr.get_attribute('id'))
            # 当数组长度大于2，就把前面的删除，确保数组长度只为2
            if len(x) > 2:
                del x[0]
                # print(x)
            elif len(x) == 2:
                result.append(x[0] == x[1])
        return 'False' in result

    def todolist_open_close(self):
        '''流程中心-我的待办-打开关闭'''
        # 点击第一条待办
        self.find_elem_is_clickable('#flowCenterTable .tbody tr').click()
        self.switch_to_parent()
        self.switch_to_iframe()
        # 判断是否含有流程历史
        if self.find_elem('#flow-panel .flow-history')!=None:
            tf1 = True
        else:
            tf1 = False
        self.switch_to_parent()
        # 关闭打开的待办
        self.close_nav_by_select()
        self.switch_to_iframe()
        # 判断是否含有处理时间
        if self.find_elem('#flowCenterTable .tbody tr:nth-child(1) td:nth-child(3)')!=None:
            tf2 = True
        else:
            tf2 = False
        # 打开和关闭都是true
        return tf1 == tf2

    def todolist_search(self):
        '''流程中心-我的待办-搜索'''
        # 点击添加
        self.find_elem('#selectUser').click()
        self.switch_to_div_iframe()
        time.sleep(0.5) #必须
        # 点击员工
        self.find_elem('div.list_div[title="员工"]').click()
        time.sleep(0.5) #必须
        # 点击选择员工
        self.find_elem('.list_div_click').click()
        time.sleep(0.5) #必须
        # 点击确定
        self.find_elem('#doReturn').click()
        self.switch_to_parent()
        # 关闭右上角通知
        self.close_righttop_message()
        self.switch_to_iframe()
        time.sleep(0.5) #必须
        # 点击搜索按钮
        self.find_elem('.btn-search').click()
        # 获取过滤后当前列表下的所有
        tdls = self.find_elems('.dept_name > span:nth-child(2)')
        tf2l = []
        # 判断是否含有不是李玲的
        for tdl in tdls:
            if (tdl.text == '李玲'):
                tf2l.append('True')
            else:
                tf2l.append('False')
                break
        tf2 = 'False' in tf2l
        # 点击清除按钮清除联系人
        self.find_elem('#clearUser').click()
        # 判断搜索框内选择的文字是否已被清除
        if (self.find_elem('#initiator_text').get_attribute('title') != '李玲'):
            tf3 = True
        else:
            tf3 = False
        # 在主题搜素框中输入“主题”搜索
        self.find_elem('#flowtitle').send_keys('主题')
        # 用Enter键代替点击搜索
        self.find_elem('#flowtitle').send_keys(Keys.ENTER)
        rl = self.find_elem('#content-space .text-center')
        if rl.text == '没有查询到数据':
            tf1 = True
        else:
            tf1 = False
        return tf1 == True and tf2 == False and tf3 == True

    def click_search(self):
        # 点击搜索按钮
        self.find_elem_is_clickable('.btn-search').click()
        self.wait_Tabloading_show_then_hide()

    def select_user(self):
        '''选择用户'''
        # 点击添加
        self.find_elem_is_clickable('#selectUser').click()  # 点击添加按钮
        self.switch_to_div_iframe()  # 切换到弹出层页面
        time.sleep(0.5) #必须
        # 点击员工
        self.find_elem_is_clickable('div.list_div[title="员工"]').click()  # 点击员工
        time.sleep(0.5) #必须
        # 点击选择员工
        self.find_elem_is_clickable('.list_div_click').click()  # 点击李玲
        time.sleep(0.5) #必须
        self.find_elem_is_clickable('#doReturn').click()  # 点击确定

    def get_flowCenten_noAvatar(self):
        '''获取流程中心列表的数据的流程处理人'''
        return self.find_elems('#flowCenter-tbody .noAvatar')

    def is_noAvatar(self,noAvatar_name):
        '''判断当前获取的所有记录的流程处理人都包含noAvatar_name'''
        noAvatars = self.get_flowCenten_noAvatar()
        flag = True
        for noAvatar in noAvatars:
            if noAvatar_name not in noAvatar.text:
                flag = False
                break
            else:
                continue
        return flag

    def is_text_center_invisibility(self):
        '''判断流程中心的没有数据提示是否不可见，是返回Ture,否返回False'''
        return self.is_elem_invisibility('.text-center')


    def open_handle_track(self):
        '''打开经办跟踪'''
        self.find_elem_is_clickable('#flowMeun>li[data-title="经办跟踪"] span').click()
        self.wait_loading_hide()

    def get_handle_track_return(self):
        # 获取经办跟踪固定元素
        ht = self.find_elem('.flowEnd')
        return ht.text

    def check_handle_track_number(self):
        '''流程中心-经办跟踪-数值显示'''
        # 检查前10个的数值是否正常显示
        nums = self.find_elems('#flowAccordion .sum')
        tf = []
        count = 0
        for num in nums:
            if (count < 10):
                tf.append(self.Is_number_Int(num.text))
                count = count + 1
            else:
                break
        # print(tf)
        return 'False' in tf

    def switch_handle_track(self):
        '''流程中心-经办跟踪-切换经办'''
        # 切换前十个经办跟踪
        stls = self.find_elems('#flowAccordion li')
        x = []
        result = []
        count = 0
        for stl in stls:
            if (count < 10):
                self.wait_loading_hide()
                stl.click()
                tr = self.find_elem('.tbody_tr')
                # 获取第一列的唯一id
                x.append(tr.get_attribute('id'))
                # 当数组长度大于2，就把前面的删除，确保数组长度只为2
                if len(x) > 2:
                    del x[0]
                    # print(x)
                elif len(x) == 2:
                    result.append(x[0] == x[1])
                count = count + 1
        return 'False' in result

    def unfinished_handle_track(self):
        '''经办跟踪-未完结的'''
        # 点击打开未完结的开关
        self.find_elem_is_clickable('.switchIcon').click()
        # 获取前8个检查状态
        states = self.find_elems('#flowCenter-tbody .status')
        arr = []
        count = 0
        for state in states:
            if count < 8:
                arr.append(state.text)
                count = count + 1
            else:
                break
        # print(arr)
        return '归档' in arr

    def flip_handle_track(self):
        '''经办跟踪-我发起的'''
        # 点击勾选我发起的选项
        self.find_elem_is_clickable('#myStartBtn').click()
        # 检查列表中的发起人姓名是否是李玲
        htls = self.find_elems('.dept_name > span:nth-child(2)')
        count = 0
        tfs = []
        for htl in htls:
            if count < 9:
                if (htl.text == '李玲'):
                    tfs.append('True')
                else:
                    tfs.append('False')
                    break
                count = count + 1
            else:
                break
        return 'False' in tfs

    def open_meter_analyse(self):
        '''打开仪表分析'''
        self.find_elem_is_clickable('#flowMeun>li[data-title="仪表分析"] span').click()

    def get_meter_analyse_return(self):
        # 获取仪表分析页面的固定元素
        ma = self.find_elem('#item > div:nth-child(1)')
        return ma.text


class MainPhonePage(PhonePage):
    '''手机端主页测试类'''

    def return_to_homepage(self):
        '''返回主页'''
        script = "location.hash = '#homePage'"
        self.driver.execute_script(script)
        self.driver.refresh()
        self.wait_Tabloading_show_then_hide()

    def made_nav_hide(self):
        '''将导航图标隐藏'''
        js = "$('.phone-main-nav-panel .if-phone-plus').css('display', 'none')"
        self.driver.execute_script(js)


    def get_nav(self):
        '''获取导航菜单'''
        try:
            return self.find_elem_visible('.phone-main-nav-trigger .if-phone-plus')
        except Exception as ex:
            print('获取切换页面的菜单异常%s' %ex)
#             time.sleep(0.5)
#             return self.find_elem_visible('.phone-main-nav-trigger .if-phone-plus')

    def switch_to_menu_page(self):
        '''切换到菜单页面'''
        self.wait_Tabloading_show_then_hide()
#         time.sleep(0.5) #必须，首页加载的loading不可靠
#         nav = self.get_nav()
#         nav.click()
        self.find_elem_is_clickable('.phone-main-nav-trigger .if-phone-plus').click()
        time.sleep(0.5) #必须,等待菜单向上展开
        self.find_elem_is_clickable('.phone-main-nav > li[title="menu"]').click()
        self.is_nav_not_visible()
        self.wait_Tabloading_show_then_hide()

    def switch_to_flow_page(self):
        '''切换到流程面板页面'''
        self.wait_Tabloading_show_then_hide()
        time.sleep(0.5) #必须，首页加载的loading不可靠
        nav = self.get_nav()
        nav.click()
        time.sleep(0.5) #必须
        self.find_elem('.phone-main-nav > li[title="flowCenter"]').click()
        self.is_nav_not_visible()
        self.wait_Tabloading_show_then_hide()

    def switch_flow_center_byname(self, name):
        '''根据名称切换流程中心页面'''
        navs = self.find_elems('.weui_navbar_item')
        for nav in navs:
            if nav.find_element_by_css_selector('.navbar-title').text == name:
                nav.click()
                break

    def switch_to_home_page(self):
        '''切换到主页页面'''
        nav = self.get_nav()
        nav.click()
        self.find_elem('.phone-main-nav > li[title="homePage"]').click()
        self.is_nav_not_visible()
        self.wait_Tabloading_show_then_hide()

    def get_menu(self, title):
        '''获取菜单'''
        return self.find_elem('.app_List span[title="' + title + '"]')

    def open_menu(self, title):
        '''打开菜单'''
#         if title != '':
#             menu = self.get_menu(title)
#             self.wait_menu_stop_move(menu)  # 等待菜单停止滑动
#             self.scroll_to_target_element(menu)  # 元素移动到用户可见的界面内
#             self.find_elem_is_clickable('.app_List span[title="' + title + '"]').click()
        if title != '':
            menu = self.get_menu(title)    
            self.wait_elem_visible('.app_List span[title="' + title + '"]')
            self.scroll_to_target_element(menu)
            self.find_elem_is_clickable('.app_List span[title="' + title + '"]').click()

    def open_menus(self, menu1, menu2, menu3):
        '''打开各级菜单'''
#         if self.find_elem('div.phone-main-nav-modal.fade-in')!=None:
#             self.find_elem_is_clickable('.iconfont.if-phone-close').click()
#             self.wait_elem_show_then_hide('div.phone-main-nav-modal.fade-in')
#             if menu1 != "":
#                 self.open_menu(menu1)
#             if menu2 != "":
#                 self.open_menu(menu2)
#             if menu3 != "":
#                 self.open_menu(menu3)
#             #self.made_nav_hide()
#             self.wait_Tabloading_show_then_hide()
#         else:
#             if menu1 != "":
#                 self.open_menu(menu1)
#             if menu2 != "":
#                 self.open_menu(menu2)
#             if menu3 != "":
#                 self.open_menu(menu3)
#             self.made_nav_hide()
#             self.wait_Tabloading_show_then_hide()
#         self.wait_elem_show_then_hide('div.phone-main-nav-modal.fade-in')
        if menu1 != "":
            self.open_menu(menu1)
        if menu2 != "":
            self.open_menu(menu2)
        if menu3 != "":
            self.open_menu(menu3)
        self.made_nav_hide()
        self.wait_Tabloading_show_then_hide()

    def wait_menu_stop_move(self, elem):
        '''等待菜单停止滑动
                    展开二级和三级菜单时有向下滑动展开的效果，浏览器运行慢时，在未完全展开就进行了点击，因为被遮挡而导致报错
        '''

        try:
            if elem is not None:
                y1 = elem.location['y']
                #time.sleep(0.2)
                y2 = elem.location['y']
                print('y1=%s' %y1)
                print('y2=%s' %y2)
                if y1 == y2:
#                     return True
                    pass
                else:
#                     return self.wait_menu_stop_move(elem)
                    self.wait_menu_stop_move(elem)
            else:
                print('菜单元素为None')
                return False
        except Exception as ex:
            print('判断菜单是否正在移动异常%s' % ex)
            return False

    def click_processing_first_data(self):
        '''点击 流程-经办 第一条数据'''
        self.find_element('#processing .pending-content li').click()
        self.wait_Tabloading_show_then_hide()

    def click_pending_first_data(self):
        '''点击 流程-待办 第一条数据'''
        self.find_element('#pending .pending-content li').click()
        self.wait_Tabloading_show_then_hide()

    def click_finished_first_data(self):
        '''点击 流程-历史 第一条数据'''
        self.find_element('#finished #ui-content li').click()
        self.wait_Tabloading_show_then_hide()

    def click_mainpage_handle(self):
        '''点击 主页-经办跟踪'''
        mhs = self.find_elements('.widget-workflow-slide a')
        for mh in mhs:
            if mh.get_attribute('aria-controls') == 'processing':
                mh.click()
                break

    def get_switch_nav_return(self):
        '''返回切换 主页-我的待办和经办跟踪 结果'''
        td = self.find_element('#sysFlowTab_pending li').text  # 主页-我的待办第一条数据
        self.click_mainpage_handle()
        hd = self.find_element('#sysFlowTab_processing li').text  # 主页-经办跟踪第一条数据
        return td != hd

    def click_todo_first_data(self):
        '''点击 主页-我的待办 第一条数据'''
        self.find_element('#sysFlowTab_pending li').click()

    def click_handle_first_data(self):
        '''点击 主页-经办跟踪 第一条数据'''
        self.click_mainpage_handle()
        self.find_element('#sysFlowTab_processing li').click()

    def click_todo_handle_more(self):
        '''点击 主页-我的待办/经办跟踪-更多'''
        target = self.find_element('div.active .bottom-menu')
        self.scroll_to_target_element(target)
        target.click()
