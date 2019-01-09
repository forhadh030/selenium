from utils.page import BasicPage
from utils.pom import callable_find_by as by


class CheckoutInfoPage(BasicPage):
    finish_btn = by(css_selector=".cart_checkout_link")

    def fill_out_info(self):
        pass

    def verify_subheader(self):
        pass

    def continue_with_order(self):
        pass

    def cancel_order(self):
        pass
