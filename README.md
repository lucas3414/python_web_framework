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
conftest：测试类的前置和后置，单个测试用例的前置和后置





    @pytest.fixture(scope='class')
    def setUpDownClass():
        logger.info("==========开始执行测试用例集===========")
        global driver
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(GD.web_login_url)
        lg = LoginPage(driver)
        yield (driver, lg)
        logger.info("==========结束执行测试用例集===========")
        driver.quit()


    @pytest.fixture()
    def refresh_page():
        yield
        driver.refresh()
        sleep(3)
-------------------------------------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------------------------------------

测试用例:参数的正常和异常用例


        @pytest.mark.usefixtures('setUpDownClass')
        @pytest.mark.usefixtures('refresh_page')
        class TestLogin:

            # 异常测试用例
            @pytest.mark.parametrize('data', LD.error_usernameFormat_data)
            def test_login_usernameFormat_error(self, data, setUpDownClass):
                logger.info(" 执行 {0} 测试用例 ".format(sys._getframe().f_code.co_name))
                logger.info(" 异常测试用例：{0} ".format(data['name']))
                # 前置  访问登录页面
                # 步骤  输入用户名为空  密码 点击登录
                # 断言  登录中  提示：用户名或密码错误
                setUpDownClass[1].login(data['username'], data['password'])
                logger.info("期望值：{0}".format(data['errorMsg']))
                logger.info("实际值：{0}".format(setUpDownClass[1].get_login_errMsg()))
                try:
                    assert setUpDownClass[1].get_login_errMsg() == data['errorMsg']
                    logger.info(" 结束执行 {0} 测试用例， 测试结果 --- PASS ".format(sys._getframe().f_code.co_name))
                    setUpDownClass[1].save_pictuer("{0}-正常截图".format(data['name']))
                except:
                    logger.info(" 结束执行 {0} 测试用例， 测试结果 --- False ".format(sys._getframe().f_code.co_name))
                    setUpDownClass[1].save_pictuer("{0}-异常截图".format(data['name']))
                    raise

            # 异常测试用例
            @pytest.mark.parametrize('data', LD.error_passwordFormat_data)
            def test_login_passwordFormat_error(self, data, setUpDownClass):
                logger.info(" 执行 {0} 测试用例 ".format(sys._getframe().f_code.co_name))
                logger.info(" 异常测试用例：{0} ".format(data['name']))
                # 前置  访问登录页面
                # 步骤  输入用户名为空  密码 点击登录
                # 断言  登录中  提示：用户名或密码错误

                setUpDownClass[1].login(data['username'], data['password'])
                logger.info("期望值：{0}".format(data['errorMsg']))
                logger.info("实际值：{0}".format(setUpDownClass[1].get_login_errMsg()))
                try:
                    assert setUpDownClass[1].get_login_errMsg() == data['errorMsg']
                    logger.info(" 结束执行 {0} 测试用例， 测试结果 --- PASS ".format(sys._getframe().f_code.co_name))
                    setUpDownClass[1].save_pictuer("{0}-正常截图".format(data['name']))
                except:
                    logger.info(" 结束执行 {0} 测试用例， 测试结果 --- False ".format(sys._getframe().f_code.co_name))
                    setUpDownClass[1].save_pictuer("{0}-异常截图".format(data['name']))
                    raise

             # 正常用例
                @pytest.mark.lucas
                @pytest.mark.smoke
                def test_login_success(self, setUpDownClass):
                    logger.info(" 执行 {0} 测试用例 ".format(sys._getframe().f_code.co_name))
                    logger.info(" 正常登录测试用例 ")
                    # 前置  访问登录页面
                    # 步骤  输入用户名 密码 点击登录
                    # 断言  首页中 能否找到退出 这个元素
                    setUpDownClass[1].login(LD.success_data['username'], LD.success_data['password'])
                    logger.info("期望值：{0}".format(True))
                    logger.info("实际值：{0}".format(IndexPage(setUpDownClass[0]).isExist_logout_ele()))
                    try:
                        assert IndexPage(setUpDownClass[0]).isExist_logout_ele()
                        logger.info(" 结束执行 {0} 测试用例， 测试结果 --- PASS ".format(sys._getframe().f_code.co_name))
                        setUpDownClass[1].save_pictuer("{0}-正常截图".format(LD.success_data['name']))
                    except:
                        logger.info(" 结束执行 {0} 测试用例， 测试结果 --- False ".format(sys._getframe().f_code.co_name))
                        setUpDownClass[1].save_pictuer("{0}-异常截图".format(LD.success_data['name']))
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
