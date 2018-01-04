from selenium import webdriver

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait

from selenium.webdriver.support.ui import Select

from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By

import unittest

import logging

from web_driver_bindings.web_driver_binding import WebDriverBinding

"""
1 - import all modules
2 - find Username, Password and Submit. Why return?
3 - define actions for test steps LoginPageSteps, send_keys, click etc. 
4 - finally, close page
"""


class LoginPage():

    def __init__(self):
        self.binding = WebDriverBinding()
        self.binding.open_page("https://iehie-train.verinovum.com/#/login")

    def findUserNameField(self):
        return self.binding.find_by_id("userName")

    def findPasswordField(self):
        return self.binding.find_by_id("password")

    def findButton(self):
        return self.binding.find_by_id("submit")

    def get_bindings(self):
        return self.binding

class LoginPageSteps():

    def __init__(self):
        self.login_page = LoginPage()

    def login(self, username, password):
        self.login_page.findUserNameField().send_keys(username)
        self.login_page.findPasswordField().send_keys(password)
        self.login_page.findButton().click()

    def close_page(self):
        self.login_page.get_bindings().close_page()
