from Locators.LoginLocators.login_locators import LoginLocator as loc
from Common.plugs.basepage import BasePage


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
