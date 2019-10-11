# python_web_framework
这是一个关于python的WebUI自动化测试的项目，之前用的是unittest测试框架，现在改成pytest测试框架，Python+PageObject+Pytest

实现页面元素、页面对象及业务、测试数据分离

项目结构：说明

            .
            |-- assets
            |   `-- style.css
            |-- cases                       --------------------- 测试用例模块
            |   |-- conftest.py
            |   |-- __init__.py
            |   |-- logincases              --------------------- 测试模块1
            |   |   |-- conftest.py
            |   |   |-- __init__.py
            |   |   `-- test_login.py
            |   `-- usercases               --------------------- 测试模块2
            |       |-- conftest.py
            |       |-- __init__.py
            |       `-- test_user_add.py
            |-- Common                      --------------------- 配置和功能函数
            |   |-- config     
            |   |   `-- config.ini          --------------------- 配置文件， 日志、报告、截图的目录等
            |   |-- __init__.py
            |   |-- plugs                   --------------------- 功能函数
            |   |   |-- basepage.py         --------------------- 封装的 webdriver Api (后续可以自己添加，目前只是封装的少许) 
            |   |   |-- get_config.py       --------------------- 获取配置文件方法
            |   |   |-- get_log.py          --------------------- 日志的配置方法
            |   |   |-- __init__.py
            |-- Locators                    --------------------- 测试页面定位
            |   |-- __init__.py
            |   |-- LoginLocators           --------------------- 登录模块的页面对象定位
            |   |   |-- __init__.py
            |   |   |-- login_locators.py
            |   `-- UserLocators            --------------------- 用户模块的页面对象定位
            |       |-- __init__.py
            |       `-- user_locators.py
            |-- OutPuts                     --------------------- 输出
            |   |-- image                   --------------------- 截图
            |   |-- log                     --------------------- 日志
            |   `-- reports                 --------------------- 报告
            |       `-- report.html
            |-- PageObjects                 ---------------------- 业务流程
            |   |-- IndexPage               ---------------------- 主页模块的页面对象
            |   |   |-- index_page.py
            |   |   |-- __init__.py
            |   |-- __init__.py
            |   |-- LoginPage               ---------------------- 登录模块的页面对象
            |   |   |-- __init__.py
            |   |   |-- login_page.py
            |   `-- UserPage                ---------------------- 用户模块的页面对象
            |       |-- __init__.py
            |       `-- user_page.py
            |-- README.md
            `-- TestDatas                   ---------------------- 测试数据
                |-- GobalDatas              ---------------------- 全局的测试数据
                |   |-- gobal_datas.py
                |   |-- __init__.py
                |-- __init__.py
                |-- LoginDatas              ---------------------- 登录模块的正常、异常测试数据
                |   |-- __init__.py
                |   |-- login_datas.py
                `-- UserDatas               ---------------------- 用户模块的正常、异常测试数据
                    |-- __init__.py
                    `-- user_add_datas.py
        
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------       

以下是简单说明：

    case: pytest的参数化  fixture的使用  conftest全局和本地的配置
            Cases/conftest：测试类的前置和后置，单个测试用例的前置和后置

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



-------------------------------------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------------------------------------

测试用例:参数的正常和异常用例


            pytest.mark.usefixtures('start_session')
            @pytest.mark.usefixtures('refresh_page')
            class TestUserAdd:

                @pytest.mark.smoke
                def test_add_user(self, start_session):
                    logger.info(" 执行 {0} 测试用例 ".format(sys._getframe().f_code.co_name))
                    logger.info('正常新增用户测试用例')
                    start_session[1].add_user(UAD.success_data['username'], UAD.success_data['password'],
                                               UAD.success_data['email'],
                                               UAD.success_data['phone'])
                    logger.info("期望值：{0}".format(UAD.success_data['Msg']))
                    logger.info("实际值：{0}".format(start_session[1].get_add_result_msg()))
                    try:
                        assert start_session[1].get_add_result_msg() == UAD.success_data['Msg']
                        logger.info(" 结束执行 {0} 测试用例， 测试结果 --- PASS ".format(sys._getframe().f_code.co_name))
                        start_session[1].save_pictuer("{0}-正常截图".format(UAD.success_data['name']))
                    except:
                        logger.info(" 结束执行 {0} 测试用例， 测试结果 --- False ".format(sys._getframe().f_code.co_name))
                        start_session[1].save_pictuer("{0}-异常截图".format(UAD.success_data['name']))
                        raise

                @pytest.mark.parametrize('data', UAD.error_usernameFormat_data)
                def test_add_usernameFormat_error(self, data, start_session):
                    print(" 执行 {0} 测试用例 ".format(sys._getframe().f_code.co_name))
                    logger.info(" 异常测试用例：{0} ".format(data['name']))
                    start_session[1].add_user(data['username'], data['password'], data['email'], data['phone'])
                    logger.info("期望值：{0}".format(data['Msg']))
                    logger.info("实际值：{0}".format(start_session[1].get_add_result_msg()))
                    try:
                        assert start_session[1].get_add_result_msg() == data['Msg']
                        logger.info(" 结束执行 {0} 测试用例， 测试结果 --- PASS ".format(sys._getframe().f_code.co_name))
                        start_session[1].save_pictuer("{0}-正常截图".format(data['name']))
                    except:
                        logger.info(" 结束执行 {0} 测试用例， 测试结果 --- False ".format(sys._getframe().f_code.co_name))
                        start_session[1].save_pictuer("{0}-异常截图".format(data['name']))
                        raise

                @pytest.mark.parametrize('data', UAD.error_usernameFormat_data)
                def test_add_passwordFormat_error(self, data, start_session):
                    logger.info(" 执行 {0} 测试用例 ".format(sys._getframe().f_code.co_name))
                    logger.info(" 异常测试用例：{0} ".format(data['name']))
                    start_session[1].add_user(data['username'], data['password'], data['email'], data['phone'])
                    logger.info("期望值：{0}".format(data['Msg']))
                    logger.info("实际值：{0}".format(start_session[1].get_add_result_msg()))
                    try:
                        assert start_session[1].get_add_result_msg() == data['Msg']
                        logger.info(" 结束执行 {0} 测试用例， 测试结果 --- PASS ".format(sys._getframe().f_code.co_name))
                        start_session[1].save_pictuer("{0}-正常截图".format(data['name']))
                    except:
                        logger.info(" 结束执行 {0} 测试用例， 测试结果 --- False ".format(sys._getframe().f_code.co_name))
                        start_session[1].save_pictuer("{0}-异常截图".format(data['name']))
                        raise
-------------------------------------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------------------------------------
 Locators：
        #页面的元素
        
        
        class LoginLocator:
            username_loc = (By.XPATH, '//*[@id="app"]/div/form/div[1]/div/div/input')
            password_loc = (By.XPATH, '//*[@id="app"]/div/form/div[2]/div/div/input')
            login_btn_loc = (By.XPATH, '//*[@type="button"]')
            error_msg_loc = (By.CLASS_NAME, 'el-message__content')
            
 -------------------------------------------------------------------------------------------------------------------------------------
 -------------------------------------------------------------------------------------------------------------------------------------
 PageObjects：
      # 业务功能流程
      
      
     class LoginPage(BasePage):

        # 登录
        def login(self, username, password):
            doc = '登录页面_登录功能_查找元素失败'
            self.input_element(loc.username_loc, username, doc)
            self.input_element(loc.password_loc, password, doc)
            self.click_element(loc.login_btn_loc, doc)

        # 获取错误提示
        def get_login_errMsg(self):
            doc = '登录页面_登录功能错误信息_查找元素失败'
            # self.wait_eleVisible(loc.error_msg_loc)
            return self.get_element_text(loc.error_msg_loc, doc)
-------------------------------------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------------------------------------
TestDatas
     # 测试数据
     
     
      # 正常场景测试数据
      success_data = {'name': '登录功能-正常测试', 'username': 'admin', 'password': '123456'}

      # 异常场景测试 - username
      error_usernameFormat_data = [
          {'name': '登录功能-异常测试-用户名为空', 'username': '', 'password': '123456', 'errorMsg': '参数错误'},
          {'name': '登录功能-异常测试-用户名不存在', 'username': 'xxoo', 'password': '123456', 'errorMsg': '用户名不存在'},
      ]

      # 异常场景测试 - password
      error_passwordFormat_data = [
          {'name': '登录功能-异常测试-密码为空', 'username': 'admin', 'password': '', 'errorMsg': '参数错误'},
          {'name': '登录功能-异常测试-密码错误', 'username': 'admin', 'password': '1234567', 'errorMsg': '密码错误'},
      ] 
-------------------------------------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------------------------------------
