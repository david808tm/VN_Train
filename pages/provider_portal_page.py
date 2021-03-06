from pages.base_page import BasePage
from web_driver_bindings.web_driver_binding import WebDriverBinding
# link to webdriver binding in the beginning

class SearchPanelElement(BasePage):

    def __init__(self):
        super(SearchPanelElement, self).__init__()

    def get_last_name(self):
        return self.binding.find_by_id("LastName")

    def get_first_name(self):
        return self.binding.find_by_id("FirstName")

    def get_date_of_birth(self):
        return self.binding.find_by_id("BirthDate")

    def get_search_button(self):
        return self.binding.find_by_xpath("//button[@ng-click='doSearch()']")


class SearchPanelSteps():
    def __init__(self):
        self.search_panel_element = SearchPanelElement()

    def search(self, last_name, first_name, date_of_birth = None, mrn = None):
        self.search_panel_element.get_last_name().send_keys(last_name)
        self.search_panel_element.get_first_name().send_keys(first_name)
        if (date_of_birth):
            self.search_panel_element.get_date_of_birth().send_keys(date_of_birth)
        self.search_panel_element.get_search_button().click()


class SearchResultsTable():
    def __init__(self):
        super(SearchResultsTable, self).__init__()
        self.web_table = self.binding.find_by_class("ui-grid-contents-wrapper")

    def find_row_by_patient(self,last_name, first_name, date_of_birth = None, mrn = None):
        self.






