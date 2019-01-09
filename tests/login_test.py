import pytest

from pages.login_page import *


def test_login_with_standard_user(start_browser):
    LoginPage(start_browser) \
        .open_page(URL.SAUCE) \
        .verify_title() \
        .login("standard_user", "secret_sauce")
    start_browser.quit()


@pytest.mark.skip(reason="Not Implemented")
def test_login_with_problem_user(start_browser):
    LoginPage(start_browser) \
        .open_page(URL.SAUCE) \
        .verify_title() \
        .login("problem_user", "secret_sauce")
    start_browser.quit()


@pytest.mark.skip(reason="Not Implemented")
def test_login_with_performance_glitch_user(start_browser):
    LoginPage(start_browser) \
        .open_page(URL.SAUCE) \
        .verify_title() \
        .login("performance_glitch_user", "secret_sauce")
    start_browser.quit()


def test_login_with_locked_out_user(start_browser):
    error_msg = "Epic sadface: Sorry, this user has been locked out."

    LoginPage(start_browser) \
        .open_page(URL.SAUCE) \
        .verify_title() \
        .invalid_login("locked_out_user", "secret_sauce", error_msg)
    start_browser.quit()


def test_login_with_invalid_user(start_browser):
    error_msg = "Epic sadface: Username and password do not match any user in this service"
    LoginPage(start_browser) \
        .open_page(URL.SAUCE) \
        .verify_title() \
        .invalid_login("invalid_user", "secret_sauce", error_msg)
    start_browser.quit()
