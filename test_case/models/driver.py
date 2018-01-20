from selenium.webdriver import Remote
from selenium import webdriver

# 启动浏览器驱动
def browser():
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications" : 2}
    chrome_options.add_experimental_option("prefs",prefs)   #禁用谷歌浏览器的通知框
#     chrome_options.add_argument("--disable-popup-blocking")    #设置谷歌浏览器允许弹出窗口
    driver = webdriver.Chrome(chrome_options=chrome_options)
#     driver = webdriver.Firefox()
    return driver

# phone皮肤启动浏览器驱动
def phone_browser():
    mobile_emulation = {"deviceName":"iPhone 6"}
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    driver = webdriver.Chrome(chrome_options = chrome_options)
    return driver
