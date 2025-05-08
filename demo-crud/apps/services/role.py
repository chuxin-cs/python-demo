from flask import request

from apps.constants.message import PAGE_LIMIT


# 查询角色分页数据
def RoleList():
    # 页码
    page = int(request.args.get('page', 1))
    # 每页数
    limit = int(request.args.get('limit', PAGE_LIMIT))
    # 分页查询
    # query =



    return


# 根据角色ID查询详情
def RoleDetail():
    return


# 添加角色
def RoleAdd():
    return


# 更新角色
def RoleUpdate():
    return


# 删除角色
def RoleDelete():
    return


# 设置状态
def RoleStatus():
    return


# 获取角色列表
def getRoleList():
    return
