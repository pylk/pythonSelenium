from selenium import webdriver
import unittest
import os
import sys
import time
from test_case.models.driver import phone_browser
from test_case.running.phone.app_test import AppPhoneTest
from test_case.page_obj.main_page import MainPhonePage
from test_case.page_obj.login_page import LoginPage


class ViewPhoneTest(AppPhoneTest):
    
    def setUp(self):
        mp = MainPhonePage(self.driver)
        mp.wait_Tabloading_show_then_hide()
        mp.switch_to_menu_page()
        
