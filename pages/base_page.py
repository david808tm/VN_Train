from web_driver_bindings.web_driver_binding import WebDriverBinding


class BasePage:
    def __init__(self):
        self.binding = WebDriverBinding()

    def click_on_logout_link(self):
        logout_link = self.binding.find_by_partial_link_text("Logout")
        logout_link.click()


