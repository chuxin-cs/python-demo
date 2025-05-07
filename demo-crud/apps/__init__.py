from flask import Flask
from flask_cors import CORS

from apps.controller import register_blueprint
from extends import register_extends


# 创建应用app
def create_app():
    # 创建Flask对象
    app = Flask(__name__)
    # 跨域处理
    CORS(app, resources={r"/*": {"origins": "*"}}, supports_credentials=True)
    # 注册蓝图
    register_blueprint(app)
    # 初始化扩展
    register_extends(app)
    # 返回APP
    return app