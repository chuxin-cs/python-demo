import os

# 应用运行地址
FLASK_HOST = os.getenv('FLASK_HOST', '127.0.0.1')
# 应用运行端口
FLASK_PORT = os.getenv('FLASK_PORT', 8021)
# 是否调试模式：是-True,否-False
FLASK_DEBUG = (os.getenv('FLASK_DEBUG', 'True') == 'True')
# 是否演示模式：是-True,否-False
FLASK_DEMO = (os.getenv('FLASK_DEMO', 'True') == 'True')