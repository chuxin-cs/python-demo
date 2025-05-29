"""
离线语音引擎
    1.运行前需要安装第三方库 faker，可使用以下命令进行安装：
        pip install faker
    2.若安装过程中出现超时问题，可使用国内镜像源进行安装，命令如下：
        pip install -i https://mirrors.aliyun.com/pypi/simple/ faker
"""

from faker import Faker
fake = Faker('zh_CN')  # 支持中文！

print(fake.name())
print(fake.address())
print(fake.ssn())
print(fake.company())
