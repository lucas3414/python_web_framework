# 正常场景测试数据
success_data = {'name': '新增用户功能-正常测试', 'username': 'haha', 'password': '123456', 'email': '123@qq.com',
                'phone': '13776787676', 'Msg': '创建成功'}

# 异常场景测试 - username
error_usernameFormat_data = [
    {'name': '新增用户功能-异常测试-用户已存在', 'username': 'haha', 'password': '123456', 'email': '123@qq.com',
     'phone': '13776787676', 'Msg': '用户名已存在'},
    {'name': '新增用户功能-异常测试-用户名为空', 'username': '', 'password': '123456', 'email': '123@qq.com', 'phone': '13776787676',
     'Msg': '用户名不能为空'},
]

# 异常场景测试 - password
error_passwordFormat_data = [
    {'name': '新增用户功能-异常测试-用户已存在', 'username': 'haha', 'password': '123456', 'email': '123@qq.com',
     'phone': '13776787676', 'Msg': '用户名已存在'},
    {'name': '新增用户功能-异常测试-密码为空', 'username': 'wang', 'password': '', 'email': '123@qq.com', 'phone': '13776787676',
     'Msg': '密码不能为空'},
]
