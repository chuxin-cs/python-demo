from .role import role_blue


# 注册路由
def register_blueprint(app):
    # 角色模块
    app.register_blueprint(role_blue)
    print("注册路由")
    return
