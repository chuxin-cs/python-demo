from config.env import DB_PREFIX
from extends import db


# 角色模型
class Role(base_model, base_db):
    # 设置表名
    __tablename__ = DB_PREFIX + "role"
    # 角色名称
    name = db.Column(db.String(150), nullable=False, comment="角色名称")
    # 角色编码
    code = db.Column(db.String(30), nullable=False, comment="角色编码")
    # 角色状态：1-正常 2-停用
    status = db.Column(db.Integer, default=1, comment="角色状态：1-正常 2-停用")
    # 角色排序
    sort = db.Column(db.Integer, default=0, comment="角色排序")
    # 角色备注
    note = db.Column(db.String(255), nullable=True, comment="角色备注")
