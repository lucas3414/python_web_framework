from selenium.webdriver.common.by import By


class LoginLocator:
    username_loc = (By.XPATH, '//*[@id="app"]/div/form/div[1]/div/div/input')
    password_loc = (By.XPATH, '//*[@id="app"]/div/form/div[2]/div/div/input')
    login_btn_loc = (By.XPATH, '//*[@type="button"]')
    error_msg_loc = (By.CLASS_NAME, 'el-message__content')
