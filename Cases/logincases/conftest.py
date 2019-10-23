import pytest
import os
import sys
from time import sleep
from selenium import webdriver
from TestDatas.GobalDatas import gobal_datas as GD
from PageObjects.LoginPage.login_page import LoginPage
from Common.plugs.basepage import BasePage
from Common.plugs.get_log import Log
from Common.plugs.get_config import r_config

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
if sys.platform == "win32":
    conf_dir = os.path.join(BASE_DIR, 'Common/config/config.ini').replace('/', '\\')
else:
    conf_dir = os.path.join(BASE_DIR, 'Common/config/config.ini')
log_dir = r_config(conf_dir, "log", "log_path")
logger = Log(log_dir)

driver = None


@pytest.fixture(scope='class')
def start_module(project_module_start):
    '''
    每个模块单独打开一次浏览器，此时 driver.quit() 需要单独加上
    :param project_module_start:  每个模块单独打开一次浏览器
    :return: driver lg
    '''
    logger.info("==========开始执行测试用例集===========")
    global driver
    driver = project_module_start
    driver.get(GD.web_login_url)
    lg = LoginPage(driver)
    yield (driver, lg)
    logger.info("==========结束执行测试用例集===========")
    driver.quit()


@pytest.fixture(scope='class')
def start_session(project_session_start):
    '''
    所有模块只打开一次浏览器
    :param project_session_start: 所有模块只打开一次浏览器
    :return: driver lg
    '''
    logger.info("==========开始执行测试用例集===========")
    global driver
    driver = project_session_start
    logger.info("----------------------------------------------------------------------------------" + str(driver))
    driver.get(GD.web_login_url)
    lg = LoginPage(driver)
    yield (driver, lg)
    logger.info("==========结束执行测试用例集===========")


@pytest.fixture()
def refresh_page():
    yield
    driver.refresh()
    sleep(3)
