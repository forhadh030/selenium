from config.const import URL
from pages.products_page import ProductsPage
from utils.page import *
from utils.pom import callable_find_by as by


class LoginPage(BasicPage):
    user_name = by(id_="user-name")
    password = by(id_="password")
    login_btn = by(css_selector=".login-button")
    error_msg = by(css_selector="h3[data-test=error]")

    def login(self, user_name, passwd):
        self.input_text(self.user_name, user_name)
        self.input_text(self.password, passwd)
        self.click_element(self.login_btn)
        return ProductsPage(self.driver)

    def invalid_login(self, user_name, passwd, msg):
        self.input_text(self.user_name, user_name)
        self.input_text(self.password, passwd)
        self.click_element(self.login_btn)
        print(self.error_msg().text, msg)
        return ProductsPage(self.driver)

    def verify_title(self):
        assert self.driver.current_url == URL.SAUCE
        return self
