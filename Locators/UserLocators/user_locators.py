from selenium.webdriver.common.by import By


class UserLocator:
    user_add_btn = (By.XPATH, '//span[text()="添加按钮"]')

    user_add_dialog_username = (
    By.XPATH, '//div[@aria-label="添加用户"]/div[@class="el-dialog__body"]/form/div[1]//input')
    # By.XPATH, '//*[@id="app"]/section/section/main/div/div/div[5]/div/div[2]/form/div[1]/div/div/input')

    user_add_dialog_password = (
    By.XPATH, '//*[@id="app"]/section/section/main/div/div/div[5]/div/div[2]/form/div[2]/div/div/input')

    user_add_dialog_email = (
    By.XPATH, '//*[@id="app"]/section/section/main/div/div/div[5]/div/div[2]/form/div[3]/div/div/input')

    user_add_dialog_phone = (
    By.XPATH, '//*[@id="app"]/section/section/main/div/div/div[5]/div/div[2]/form/div[4]/div/div/input')

    user_add_dialog_confirm_btn = (By.XPATH, '//*[@id="app"]/section/section/main/div/div/div[5]/div/div[3]/div/button[2]')

    user_add_dialog_cancel_btn = (By.XPATH, '//*[@id="app"]/section/section/main/div/div/div[5]/div/div[3]/div/button[1]')

    user_add_dialog_msg = (By.XPATH, '//div[@role="alert"]/p[@class="el-message__content"]')
