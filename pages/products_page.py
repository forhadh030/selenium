from pages.shopping_cart_page import ShoppingCartPage
from utils.page import BasicPage
from utils.pom import callable_find_by as by


class ProductsPage(BasicPage):
    products = by(css_selector=".product_label")
    add_to_cart_btn = by(css_selector=".pricebar > .add-to-cart-button", multiple=True)
    shopping_cart_icon = by(id_="shopping_cart_container")

    def add_item_to_cart(self):
        self.add_to_cart_btn()[0].click()
        self.shopping_cart_icon().click()
        return ShoppingCartPage(self.driver)

    def remove_item_from_cart(self):
        pass

    def verify_subheader(self):
        assert self.products().text == "Products"

    def add_random_item_to_cart(self):
        pass

    def filter_by_price(self):
        pass
