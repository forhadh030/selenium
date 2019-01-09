import pytest

from pages.login_page import *


def test_product(start_browser):
    LoginPage(start_browser) \
        .open_page(URL.SAUCE) \
        .verify_title() \
        .login("standard_user", "secret_sauce") \
        .verify_subheader()
    start_browser.quit()


@pytest.mark.skip(reason="Not Implemented")
def test_product_with_problem_user(start_browser):
    LoginPage(start_browser) \
        .open_page(URL.SAUCE) \
        .verify_title() \
        .login("problem_user", "secret_sauce")


@pytest.mark.skip(reason="Not Implemented")
def test_product_with_performance_glitch_user(start_browser):
    LoginPage(start_browser) \
        .open_page(URL.SAUCE) \
        .verify_title() \
        .login("performance_glitch_user", "secret_sauce")
