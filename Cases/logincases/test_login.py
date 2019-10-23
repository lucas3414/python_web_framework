import pytest
import sys
import os
from PageObjects.IndexPage.index_page import IndexPage
from TestDatas.LoginDatas import login_datas as LD
from Common.plugs.get_log import Log
from Common.plugs.get_config import r_config

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
if sys.platform == "win32":
    conf_dir = os.path.join(BASE_DIR, 'Common/config/config.ini').replace('/', '\\')
else:
    conf_dir = os.path.join(BASE_DIR, 'Common/config/config.ini')
log_dir = r_config(conf_dir, "log", "log_path")
logger = Log(log_dir)


@pytest.mark.usefixtures('start_session')
@pytest.mark.usefixtures('refresh_page')
class TestLogin:

    # 异常测试用例
    @pytest.mark.parametrize('data', LD.error_usernameFormat_data)
    def test_login_usernameFormat_error(self, data, start_session):
        logger.info(" 执行 {0} 测试用例 ".format(sys._getframe().f_code.co_name))
        logger.info(" 异常测试用例：{0} ".format(data['name']))
        # 前置  访问登录页面
        # 步骤  输入用户名为空  密码 点击登录
        # 断言  登录中  提示：用户名或密码错误
        start_session[1].login(data['username'], data['password'])
        logger.info("期望值：{0}".format(data['errorMsg']))
        logger.info("实际值：{0}".format(start_session[1].get_login_errMsg()))
        try:
            assert start_session[1].get_login_errMsg() == data['errorMsg']
            logger.info(" 结束执行 {0} 测试用例， 测试结果 --- PASS ".format(sys._getframe().f_code.co_name))
            start_session[1].save_pictuer("{0}-正常截图".format(data['name']))
        except:
            logger.info(" 结束执行 {0} 测试用例， 测试结果 --- False ".format(sys._getframe().f_code.co_name))
            start_session[1].save_pictuer("{0}-异常截图".format(data['name']))
            raise

    # 异常测试用例
    @pytest.mark.parametrize('data', LD.error_passwordFormat_data)
    def test_login_passwordFormat_error(self, data, start_session):
        logger.info(" 执行 {0} 测试用例 ".format(sys._getframe().f_code.co_name))
        logger.info(" 异常测试用例：{0} ".format(data['name']))
        # 前置  访问登录页面
        # 步骤  输入用户名为空  密码 点击登录
        # 断言  登录中  提示：用户名或密码错误

        start_session[1].login(data['username'], data['password'])
        logger.info("期望值：{0}".format(data['errorMsg']))
        logger.info("实际值：{0}".format(start_session[1].get_login_errMsg()))
        try:
            assert start_session[1].get_login_errMsg() == data['errorMsg']
            logger.info(" 结束执行 {0} 测试用例， 测试结果 --- PASS ".format(sys._getframe().f_code.co_name))
            start_session[1].save_pictuer("{0}-正常截图".format(data['name']))
        except:
            logger.info(" 结束执行 {0} 测试用例， 测试结果 --- False ".format(sys._getframe().f_code.co_name))
            start_session[1].save_pictuer("{0}-异常截图".format(data['name']))
            raise

    # 正常用例
    @pytest.mark.lucas
    @pytest.mark.smoke
    def test_login_success(self, start_session):
        logger.info(" 执行 {0} 测试用例 ".format(sys._getframe().f_code.co_name))
        logger.info(" 正常登录测试用例 ")
        # 前置  访问登录页面
        # 步骤  输入用户名 密码 点击登录
        # 断言  首页中 能否找到退出 这个元素
        start_session[1].login(LD.success_data['username'], LD.success_data['password'])
        logger.info("期望值：{0}".format(True))
        logger.info("实际值：{0}".format(IndexPage(start_session[0]).isExist_logout_ele()))
        try:
            assert IndexPage(start_session[0]).isExist_logout_ele()
            logger.info(" 结束执行 {0} 测试用例， 测试结果 --- PASS ".format(sys._getframe().f_code.co_name))
            start_session[1].save_pictuer("{0}-正常截图".format(LD.success_data['name']))
        except:
            logger.info(" 结束执行 {0} 测试用例， 测试结果 --- False ".format(sys._getframe().f_code.co_name))
            start_session[1].save_pictuer("{0}-异常截图".format(LD.success_data['name']))
            raise
