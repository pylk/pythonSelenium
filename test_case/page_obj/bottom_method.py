#coding=utf-8
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support import expected_conditions as EC


class Bottom_Method(object):
    '''底层方法封装'''

    def __init__(self, driver):
        self.driver = driver

    def find_elem_in_dom(self, locator, timeout=5):
        '''判断5s内，定位的元素是否存在dom结构里。存在则返回元素，不存在则返回None'''
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, locator)))
        except TimeoutException:
            print('find_elem_in_dom获取 %s 元素超时' % locator)
            return None

    def find_elems_in_dom(self, locator, timeout=5):
        '''判断5s内，定位的一组元素是否存在dom结构里。存在则返回元素列表，不存在则返回None'''
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_all_elements_located((By.CSS_SELECTOR, locator)))
        except TimeoutException:
            print('find_elems_in_dom获取 %s 元素组超时' % locator)
            return None

    def find_elem_is_visible(self, locator, timeout=5):
        '''判断5s内，定位的元素是否存在dom结构里并且可见。存在则返回元素，不存在则返回None'''
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
        except TimeoutException:
            print('find_elem_is_visible获取 %s 元素超时' % locator)
            return None

    def find_elems_is_visible(self, locator, timeout=5):
        '''判断5s内，定位的元素是否存在dom结构里并且可见。存在则返回元素，不存在则返回None'''
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_all_elements_located((By.CSS_SELECTOR, locator)))
        except TimeoutException:
            print('find_elems_is_visible获取 %s 元素组超时' % locator)
            return None

    def find_elem_is_clickable(self, locator, timeout=5):
        '''判断5s内，定位的元素是否可见并且可以点击。存在则返回元素，不存在则返回None'''
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.element_to_be_clickable((By.CSS_SELECTOR, locator)))
        except TimeoutException:
            print('find_elem_is_clickable获取 %s 元素超时' % locator)
            return None

    def wait_elem_is_visible(self, locator, timeout=5):
        '''5秒内，定位的元素可见，只做等待动作不返回值'''
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
        except TimeoutException:
            print('5秒内 %s 元素仍为可见' % locator)

    def wait_elem_is_display(self, locator, timeout=5):
        '''5秒内，定位的元素消失，只做等待动作不返回值'''
        try:
            WebDriverWait(self.driver, timeout).until_not(
                EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
        except TimeoutException:
            print('5秒内 %s 元素仍未消失' % locator)

    def find_alert(self, locator, timeout=3):
        '''判断3秒内，是否有alert出现，有则返回alert,没有则返回None'''
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.alert_is_present())
        except TimeoutException:
            print('3秒内没有alert出现')
            return None

    def is_and_switch_to_iframe(self, locator, timeout=3):
        '''判断是否存在iframe,存在则切进去，不返回值'''
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, locator)))
        except TimeoutException:
            print('无法切到 %s ifarme' % locator)

    def scroll_to_visiable_element(self, locator):
        '''传入元素，滚动到可见的目标元素的位置'''
        element = self.find_elem_is_visible(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)



