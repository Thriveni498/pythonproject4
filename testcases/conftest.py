import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


@pytest.fixture()
def setup(browser):
    print(browser)
    if browser == 'chrome':
        print("launch chrome browser")
        service_obj = Service("C:/Users/Admin/Desktop/chrome driver/chromedriver.exe")
        driver = webdriver.Chrome(service=service_obj)
        #driver.implicitly_wait(10)
    else:
        service_obj = Service("C:/Users/Admin/Desktop/chrome driver/chromedriver.exe")
        driver = webdriver.Firefox(service=service_obj)

    return driver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
# this will return browser value to setup method
def browser(request):
    return request.config.getoption("--browser")


##### html report##########

# def pytest_configure(config):
#     config._metadata['Project Name'] = 'pythonproject4'
#     config._metadata['Module Name'] = 'customers'
#     config._metadata['Tester'] = 'Thriveni'
#
# @pytest.mark.optionalhook
# def pytest_metadata(metadata):
#     metadata.pop("JAVA_HOME", None)
#     metadata.pop("plugins", None)


