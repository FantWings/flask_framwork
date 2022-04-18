from flask import make_response


def json_response(data=None, msg=None, status=0, code=200):
    """
    接口统一函数
    data:           回调数据（Json）
    msg:            附加消息（字符串）
    status:           返回码（数值）
    """
    response = {"status": status, "msg": msg, "data": data}
    return make_response(response, code)