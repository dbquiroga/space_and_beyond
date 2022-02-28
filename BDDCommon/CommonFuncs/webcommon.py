"""
Module containing common function used in several tests.
Functions that are not test or feature specific.
"""
import random
import string
from selenium import webdriver


def go_to(url, browser_type=None):
    """
    Function to start instance of the specified browser and navigate to the specified url.

    :param url: the url to navigate to
    :param browser_type: the type of browser to start (Default is Firefox)

    :return: driver: browser instance
    """
    if not browser_type:
        # create instance of Chrome driver the browser type is not specified
        browser = webdriver.Chrome()
    elif browser_type.lower() == 'firefox':
        # create instance of the Firefox driver
        browser = webdriver.Firefox()
    else:
        raise Exception(f"The browser type '{browser_type}' is not supported")

    # clean the url and go to the url
    url = url.strip()
    browser.get(url)

    return browser

def assert_current_url(context, expected_url):
    """
    Function to get the current url and assert it is same as the expected url.
    :param context:
    :param expected_url:
    """

    # get the current url
    current_url = context.browser.current_url

    if not expected_url.startswith('http') and not expected_url.startswith('https'):
        print(expected_url)
        expected_url = 'https://' + expected_url
        
    assert current_url == expected_url, "The current url is not as expected." \
                                        f" Actual: {current_url}, Expected: {expected_url}"

    print("The page url is as expected.")