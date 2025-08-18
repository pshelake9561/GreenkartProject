import os.path
from fileinput import filename
from lib2to3.pgen2 import driver

import allure
import pytest
import pytest_html
from selenium import webdriver
from selenium.webdriver.common.by import By

from utilities.config_reader import ConfigReader


def pytest_addoption(parser):
    parser.addoption("--browser_name", action="store", default="chrome", help="browser selection")
    parser.addoption("--env", action="store", default="QA", help="Environment to run tests against")


@pytest.fixture
def setup(request):
    browser_name = request.config.getoption("browser_name")
    #base_url = request.config.getoption("base_url")
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--start-maximized")
    edge_options = webdriver.EdgeOptions()
    edge_options.add_argument("--start-maximized")
    firefox_options = webdriver.FirefoxOptions()
    firefox_options.add_argument("--start-maximized")
    if browser_name == "chrome":
        driver = webdriver.Chrome(options=chrome_options)
    elif browser_name == "edge":
        driver = webdriver.Edge(options=edge_options)
    elif browser_name == 'firefox':
        driver = webdriver.Firefox(options=firefox_options)
    driver.implicitly_wait(5)
    #driver.get(base_url)
    yield driver
    driver.quit()


@pytest.fixture(scope='session')
def config_env(request):
    env = request.config.getoption("--env")
    return ConfigReader(env)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # Execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # We only want to take screenshot on test failure
    if rep.when == "call" and rep.failed:
        setup = item.funcargs.get("setup")  # Get driver from test

        if setup:
            # Capture screenshot as base64
            screenshot = setup.get_screenshot_as_base64()

            # Attach it to the HTML report
            extra = getattr(rep, 'extra', [])
            html = (
                '<div><img src="data:image/png;base64,{}" alt="screenshot" '
                'style="width:600px;height:300px;" '
                'onclick="window.open(this.src)" align="right"/></div>'
            ).format(screenshot)
            extra.append(pytest_html.extras.html(html))
            rep.extra = extra


@pytest.fixture(scope="class")
def scope_class():
    print("This is pre condition")
    yield
    print("This is post condition")

