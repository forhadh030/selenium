import pytest

from pages.login_page import *


@pytest.mark.skip(reason="Not Implemented")
def test_item(start_browser):
    LoginPage(start_browser) \
        .open_page(URL.SAUCE) \
        .verify_title() \
        .login("standard_user", "secret_sauce")


@pytest.mark.skip(reason="Not Implemented")
def test_item_with_problem_user(start_browser):
    LoginPage(start_browser) \
        .open_page(URL.SAUCE) \
        .verify_title() \
        .login("problem_user", "secret_sauce")


@pytest.mark.skip(reason="Not Implemented")
def test_item_with_performance_glitch_user(start_browser):
    LoginPage(start_browser) \
        .open_page(URL.SAUCE) \
        .verify_title() \
        .login("performance_glitch_user", "secret_sauce")
