from utils.page import BasicPage
from utils.pom import callable_find_by as by


class CheckoutOverviewPage(BasicPage):
    overview_subheader = by(css_selector="#contents_wrapper > .subheader_label")

    def verify_overview_subheader(self):
        pass

    def cancel_order(self):
        pass

    def finish_order(self):
        pass
