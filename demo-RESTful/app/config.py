import os
# 用户名
USERNAME = os.getenv('MYSQL_USER_NAME')
# 密码
PASSWORD = os.getenv('MYSQL_USER_PASSWORD')
# 地址
HOSTNAME = os.getenv('MYSQL_HOSTNAME')
# 端口
PORT = os.getenv('MYSQL_PORT')
# 数据库名称
DATABASE = os.getenv('MYSQL_DATABASE_NAME')
DIALECT = 'mysql'
DRIVER = 'pymysql'
class Config(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_ECHO = True
    SECRET_KEY = os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = "{}+{}://{}:{}@{}:{}/{}?charset=utf8".format(DIALECT, DRIVER, USERNAME, PASSWORD,
                                                                           HOSTNAME, PORT, DATABASE)

# 生成环境
class ProductionConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = ''
# 开发环境
class DevelopmentConfig(Config):
    DEBUG = True
# 测试环境
class TestingConfig(Config):
    TESTING = True
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'testing': TestingConfig,
    'default': DevelopmentConfig,
}
