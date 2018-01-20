from selenium import webdriver  # 导入webdriver包

dr=webdriver.Chrome()     #调用谷歌浏览器
dr.maximize_window()  # 最大化浏览器

dr.get("http://bpm.ice.test.colourlife.com/admin/login.jsp")  # 通过get()方法，打开一个url站点
dr.find_element_by_css_selector('#loginform_username').send_keys('hanyongn')
dr.find_element_by_css_selector('#loginform_password').send_keys('zk170589215')
dr.find_element_by_css_selector('input[type="image"]').click()


dr.quit()  # 关闭并退出浏览器