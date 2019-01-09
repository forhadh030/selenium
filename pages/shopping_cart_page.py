from utils.page import BasicPage
from utils.pom import callable_find_by as by


class ShoppingCartPage(BasicPage):
    checkout_btn = by(css_selector=".cart_checkout_link")

    def checkout_item(self):
        pass

    def change_quantity(self):
        pass

    def continue_shopping(self):
        pass

    def remove_item(self):
        pass

    def verify_item(self):
        pass

    def verify_price(self):
        pass
