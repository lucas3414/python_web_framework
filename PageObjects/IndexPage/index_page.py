from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Locators.IndexLocators.index_locators import IndexLocator as loc


class IndexPage:

    def __init__(self, driver):
        self.driver = driver

    # 判断当前元素是否存在 存在返回True 否则返回false
    def isExist_logout_ele(self):
        try:
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(loc.logout_loc))
            return True
        except:
            return False


