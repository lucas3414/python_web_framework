import pytest, sys, os
from TestDatas.UserDatas import user_add_datas as UAD
from Common.plugs.get_log import Log
from Common.plugs.get_config import r_config

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
conf_dir = os.path.join(BASE_DIR, 'Common/config/config.ini').replace('/', '\\')
log_dir = r_config(conf_dir, "log", "log_path")
logger = Log(log_dir)


@pytest.mark.usefixtures('setUpDownClass')
@pytest.mark.usefixtures('refresh_page')
class TestUserAdd:

    @pytest.mark.smoke
    def test_add_user(self, setUpDownClass):
        logger.info(" 执行 {0} 测试用例 ".format(sys._getframe().f_code.co_name))
        logger.info('正常新增用户测试用例')
        setUpDownClass[1].add_user(UAD.success_data['username'], UAD.success_data['password'],
                                   UAD.success_data['email'],
                                   UAD.success_data['phone'])
        logger.info("期望值：{0}".format(UAD.success_data['Msg']))
        logger.info("实际值：{0}".format(setUpDownClass[1].get_add_result_msg()))
        try:
            assert setUpDownClass[1].get_add_result_msg() == UAD.success_data['Msg']
            logger.info(" 结束执行 {0} 测试用例， 测试结果 --- PASS ".format(sys._getframe().f_code.co_name))
            setUpDownClass[1].save_pictuer("{0}-正常截图".format(UAD.success_data['name']))
        except:
            logger.info(" 结束执行 {0} 测试用例， 测试结果 --- False ".format(sys._getframe().f_code.co_name))
            setUpDownClass[1].save_pictuer("{0}-异常截图".format(UAD.success_data['name']))
            raise

    @pytest.mark.parametrize('data', UAD.error_usernameFormat_data)
    def test_add_usernameFormat_error(self, data, setUpDownClass):
        print(" 执行 {0} 测试用例 ".format(sys._getframe().f_code.co_name))
        logger.info(" 异常测试用例：{0} ".format(data['name']))
        setUpDownClass[1].add_user(data['username'], data['password'], data['email'], data['phone'])
        logger.info("期望值：{0}".format(data['Msg']))
        logger.info("实际值：{0}".format(setUpDownClass[1].get_add_result_msg()))
        try:
            assert setUpDownClass[1].get_add_result_msg() == data['Msg']
            logger.info(" 结束执行 {0} 测试用例， 测试结果 --- PASS ".format(sys._getframe().f_code.co_name))
            setUpDownClass[1].save_pictuer("{0}-正常截图".format(data['name']))
        except:
            logger.info(" 结束执行 {0} 测试用例， 测试结果 --- False ".format(sys._getframe().f_code.co_name))
            setUpDownClass[1].save_pictuer("{0}-异常截图".format(data['name']))
            raise

    @pytest.mark.parametrize('data', UAD.error_usernameFormat_data)
    def test_add_passwordFormat_error(self, data, setUpDownClass):
        logger.info(" 执行 {0} 测试用例 ".format(sys._getframe().f_code.co_name))
        logger.info(" 异常测试用例：{0} ".format(data['name']))
        setUpDownClass[1].add_user(data['username'], data['password'], data['email'], data['phone'])
        logger.info("期望值：{0}".format(data['Msg']))
        logger.info("实际值：{0}".format(setUpDownClass[1].get_add_result_msg()))
        try:
            assert setUpDownClass[1].get_add_result_msg() == data['Msg']
            logger.info(" 结束执行 {0} 测试用例， 测试结果 --- PASS ".format(sys._getframe().f_code.co_name))
            setUpDownClass[1].save_pictuer("{0}-正常截图".format(data['name']))
        except:
            logger.info(" 结束执行 {0} 测试用例， 测试结果 --- False ".format(sys._getframe().f_code.co_name))
            setUpDownClass[1].save_pictuer("{0}-异常截图".format(data['name']))
            raise
