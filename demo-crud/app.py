from apps import create_app
from config.env import FLASK_HOST, FLASK_PORT, FLASK_DEBUG

# 创建应用实例
app = create_app()

if __name__ == '__main__':
    # 启动应用
    app.run(host=FLASK_HOST, port=FLASK_PORT, debug=FLASK_DEBUG)