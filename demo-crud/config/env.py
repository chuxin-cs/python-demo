import os

# 应用运行地址
FLASK_HOST = os.getenv('FLASK_HOST', '127.0.0.1')
# 应用运行端口
FLASK_PORT = os.getenv('FLASK_PORT', 8021)
# 是否调试模式：是-True,否-False
FLASK_DEBUG = (os.getenv('FLASK_DEBUG', 'True') == 'True')
# 是否演示模式：是-True,否-False
FLASK_DEMO = (os.getenv('FLASK_DEMO', 'True') == 'True')


# =============================================== 数据库配置 =================================================

# 数据库驱动
DB_DRIVER = os.getenv('DB_DRIVER', 'mysql')
# 数据库地址
DB_HOST = os.getenv('DB_HOST', '127.0.0.1')
# 数据库端口
DB_PORT = os.getenv('DB_PORT', 3306)
# 数据库名称
DB_DATABASE = os.getenv('DB_DATABASE', 'py_crud')
# 数据库账号
DB_USERNAME = os.getenv('DB_USERNAME', 'root')
# 数据库密码
DB_PASSWORD = os.getenv('DB_PASSWORD', '')
# 数据表前缀
DB_PREFIX = os.getenv('DB_PREFIX', 'flask_')
# 是否开启调试模式：是-True,否-False
DB_DEBUG = (os.getenv('DB_DEBUG', 'True') == 'True')