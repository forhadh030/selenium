import pytest
from selenium import webdriver

from config.const import Const


@pytest.fixture(scope='function', params=[Const.browser])
def start_browser(request):
    name = request.config.getoption("--browser") or request.param

    try:
        if name == "firefox" or name == "Firefox" or name == "ff":
            print("start browser name :Firefox")
            driver = webdriver.Firefox()
            return driver
        elif name == "chrome" or name == "Chrome":
            print("start browser name :Chrome")
            driver = webdriver.Chrome()
            return driver
        elif name == "ie" or name == "Ie":
            print("start browser name :Ie")
            driver = webdriver.Ie()
            return driver
        elif name == "phantomjs" or name == "Phantomjs":
            print("start browser name :phantomjs")
            driver = webdriver.PhantomJS()
            return driver
        else:
            print("Not found this browser,You can use 'firefox', 'chrome', 'ie' or 'phantomjs'")
    except Exception as msg:
        print("Couldn't start browser：%s" % str(msg))


def pytest_addoption(parser):
    parser.addoption("-B", "--browser",
                     action="store",
                     help=f"Browser")
