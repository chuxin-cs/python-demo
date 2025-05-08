from extends.extends_sqlalchemy import db

# 注册扩展(扩展初始化)
def register_extends(app):
    db.init_app(app)
    return