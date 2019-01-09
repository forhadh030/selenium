from utils.page import BasicPage
from utils.pom import callable_find_by as by


class ItemPage(BasicPage):
    back_btn = by(css_selector="")

    def go_back_to_product(self):
        pass

    def add_item_to_cart(self):
        pass
