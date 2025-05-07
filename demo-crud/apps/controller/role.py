from flask import Blueprint
# 角色蓝图
role_blue = Blueprint('role', __name__, url_prefix='/role')

# 查询分页数据
@role_blue.route('/list', methods=["GET"])
def list():
    return "222"

