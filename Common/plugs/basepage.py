import time, datetime, os, sys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Common.plugs.get_log import Log
from Common.plugs.get_config import r_config

BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))

if sys.platform == "win32":
    conf_dir = os.path.join(BASE_DIR, 'Common/config/config.ini').replace('/', '\\')
else:
    conf_dir = os.path.join(BASE_DIR, 'Common/config/config.ini')
log_dir = r_config(conf_dir, "log", "log_path")
images_dir = r_config(conf_dir, "image", "img_path")

logger = Log(log_dir)


# 封装基本函数 - 执行日志、 异常处理、 截图
class BasePage:

    def __init__(self, driver):
        self.driver = driver

    # 截图
    def save_pictuer(self, doc):
        filePath = images_dir + '{0}_{1}.png'.format(doc, time.strftime('%Y-%m-%d_%H_%M_%S', time.localtime()))
        try:
            self.driver.save_screenshot(filePath)
            logger.info('截图成功，图片路径为: {0}'.format(filePath))
        except:
            logger.info('截图失败')

    # 等待元素可见
    def wait_eleVisible(self, locator, doc=''):
        try:
            start = datetime.datetime.now()
            WebDriverWait(self.driver, timeout=20, poll_frequency=0.5).until(EC.visibility_of_element_located(locator))
            end = datetime.datetime.now()
            wait_time = (end - start).seconds
            logger.info('等待元素 {0} 可见，共耗时{1}s '.format(locator, wait_time))
        except:
            logger.info('等待元素 {0} 失败！！！'.format(locator))
            self.save_pictuer(doc)

    # 等待元素存在
    def wait_elePresence(self):
        pass

    # 查找元素
    def get_element(self, locator, doc=''):
        print(locator)
        logger.info('查找元素 {0}'.format(locator))
        try:
            self.wait_eleVisible(locator, doc)
            return self.driver.find_element(*locator)
        except:
            logger.info('查找元素 {0} 失败！！！'.format(locator))
            raise

    # 点击元素
    def click_element(self, locator, doc=''):
        self.get_element(locator, doc)
        logger.info('{0} 点击元素 {1}'.format(doc, locator))
        try:
            self.wait_eleVisible(locator, doc)
            self.get_element(locator, doc).click()
        except:
            logger.info('点击元素 {0} 失败！！！'.format(locator))
            raise

    # 输入操作
    def input_element(self, locator, key, doc=''):
        self.get_element(locator, doc)
        logger.info('{0} 输入元素 {1}'.format(doc, locator))
        try:
            self.wait_eleVisible(locator, doc)
            self.get_element(locator, doc).send_keys(key)
        except:
            logger.info('元素输入失败！！！')
            raise

    # 获取文本
    def get_element_text(self, locator, doc=''):
        self.get_element(locator, doc)
        logger.info('{0} 获取元素 {1}'.format(doc, locator))
        try:
            self.wait_eleVisible(locator, doc)
            return self.get_element(locator, doc).text
        except:
            logger.info('元素的文本获取失败！！！')
            raise

    # 获取元素属性
    def get_element_attribute(self, attr, locator, doc=''):
        self.get_element(locator, doc)
        logger.info('{0} 获取元素属性 {1}'.format(doc, locator))
        try:
            self.wait_eleVisible(locator, doc)
            return self.get_element(locator, doc).get_attribute(attr)
        except:
            logger.info('元素的属性获取失败！！！')
            raise

    # alter 处理
    def alter_action(self):
        pass

    # iframe 切换
    def switch_iframe(self):
        pass

    # windows 切换
    def switch_window(self):
        pass

    # 上传操作
    def upload_file(self):
        pass

    # 滚动条处理
