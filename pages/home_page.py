from pages.base_page import BasePage
from web_driver_bindings.web_driver_binding import WebDriverBinding

"""
1) import webdriver binding
2) create HomePage class, to verify that Home Page and Log out elements 
present on page. In __init__ we tie HomePage to WebDriverBinding class
3) create HomePageSteps, to click on Logout element from HomePage
class. We tie HomePageSteps to the HomePage class
"""

class HomePage(BasePage):
    def __init__(self):
        self.binding = WebDriverBinding()


    def web_page_title(self):
        return self.binding.find_by_xpath("//div/h3[contains(text(), 'Home Page')]")


    def get_provider_portal_link(self):
        return self.binding.find_by_xpath("//a[@href='/portal']")


class HomePageSteps:
    def __init__(self):
        self.home_page = HomePage()




