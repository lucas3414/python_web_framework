import pytest
from selenium import webdriver

driver = None




@pytest.fixture(scope='class')
def setUpDownClass():
    print("==========开始执行测试===========")
    global driver
    driver = webdriver.Chrome()
    yield
    driver.quit()
    print("==========结束执行测试===========")


@pytest.fixture()
def setUp():
    print("app3")
