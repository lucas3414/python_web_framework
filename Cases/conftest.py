import pytest
import os
from selenium import webdriver
from Common.plugs.get_log import Log
from Common.plugs.get_config import r_config

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
conf_dir = os.path.join(BASE_DIR, 'Common/config/config.ini').replace('/', '\\')
log_dir = r_config(conf_dir, "log", "log_path")
logger = Log(log_dir)

driver = None


@pytest.fixture(scope='session')
def project_session_start():
    logger.info("==========开始 XX项目 执行测试===========")
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
    logger.info("==========结束 XX项目 测试===========")


@pytest.fixture(scope='module')
def project_module_start():
    logger.info("==========开始 XX模块 执行测试===========")
    global driver
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
    logger.info("==========结束 XX模块 测试===========")


@pytest.fixture()
def project_func():
    print("project_func")



def pytest_configure(config):
    # 标签名集合
    marker_list = ['smoke', 'lucas']
    for markers in marker_list:
        config.addinivalue_line('markers', markers)
