import pytest, os
from time import sleep
from selenium import webdriver
from TestDatas.GobalDatas import gobal_datas as GD
from TestDatas.LoginDatas.login_datas import success_data as LD
from PageObjects.LoginPage.login_page import LoginPage
from PageObjects.UserPage.user_page import UserPage
from Common.plugs.basepage import BasePage
from Common.plugs.get_log import Log
from Common.plugs.get_config import r_config

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
conf_dir = os.path.join(BASE_DIR, 'Common/config/config.ini').replace('/', '\\')
log_dir = r_config(conf_dir, "log", "log_path")
logger = Log(log_dir)
driver = None


@pytest.fixture(scope='class')
def setUpDownClass():
    logger.info("==========开始执行测试用例集===========")
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(GD.web_login_url)
    LoginPage(driver).login(LD['username'], LD['password'])
    sleep(2)
    driver.get(GD.web_user_url)
    ug = UserPage(driver)
    yield (driver, ug)
    logger.info("==========结束执行测试用例集===========")
    driver.quit()

@pytest.fixture()
def refresh_page():
    yield
    sleep(3)
