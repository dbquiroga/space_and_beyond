from behave import *
from BDDCommon.CommonFuncs import webcommon
from BDDCommon.CommonConfigs import urlconfig


@given('I go to the site "{site}"')
def go_to_url(context, site):
    url = urlconfig.URLCONFIG.get(site)

    print(f"Navigating to the site: {url}")

    context.browser = webcommon.go_to(url)

@then('I should be on "{site}"')
def verify_current_url(context, site):
    url = urlconfig.URLCONFIG.get(site)
    webcommon.assert_current_url(context, url)
