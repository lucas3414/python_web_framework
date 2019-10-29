from Locators.UserLocators.user_locators import UserLocator as loc
from Common.plugs.basepage import BasePage


class UserPage(BasePage):

    def add_user(self, username, password, email, phone):
        doc = '用户列表页面_新增用户功能'
        self.click_element(loc.user_add_btn, doc)
        self.input_element(loc.user_add_dialog_username, username, doc)
        self.input_element(loc.user_add_dialog_password, password, doc)
        self.input_element(loc.user_add_dialog_email, email, doc)
        self.input_element(loc.user_add_dialog_phone, phone, doc)
        self.click_element(loc.user_add_dialog_confirm_btn, doc)

    def get_add_result_msg(self):
        doc = '用户列表页面_新增用户功能_获取新增结果信息'
        # self.wait_eleVisible(loc.user_add_dialog_msg, doc)
        return self.get_element_text(loc.user_add_dialog_msg, doc)
