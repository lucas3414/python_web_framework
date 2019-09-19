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
