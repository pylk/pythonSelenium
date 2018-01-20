import time
from test_case.running.html5.app_test import AppTest
from test_case.page_obj.main_page import MainPage


class ComponentTest(AppTest):
    
    def setUp(self):
        print('-------%s' %self)
        
        mp = MainPage(self.driver)
        mp.refresh_main()

        if self.menu1 != '':
            mp.open_menu(self.menu1)
        #time.sleep(0.2)
        
        if self.menu2 != '':
            mp.open_menu(self.menu2)
        #time.sleep(0.2)

        if self.menu3 != '':
            mp.open_menu(self.menu3)
        #time.sleep(0.2)

        mp.switch_to_iframe()
        mp.wait_loading_hide()
            
    def scroll_to(self, y):
        '''执行js脚本，操作滚动条滚动到离页面顶部y值的位置'''
        #time.sleep(0.5)
        script = 'var $con = $("#_contentTable");if($con.size()>0)$con.getNiceScroll(0).doScrollTop('+y+',10)' #滚动到控件可以看到后面的代码执行才不会报错
        self.driver.execute_script(script)
        time.sleep(0.3) #必须
