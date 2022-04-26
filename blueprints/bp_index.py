from flask import request, Blueprint
from time import time

from utils.response import json_response
from utils.generator import gen_md5_password, gen_token

from tables.t_example import Users

blueprint = Blueprint("index", __name__, url_prefix="/")


# 示例页面，打开获得{"key": "value"}返回值
@blueprint.route("/", methods=["GET"])
def index():
    """首页示例"""
    return json_response({"key": "value"}, "hello_world", 0)


# 示例页面，打开获得提交的Json作为返回
@blueprint.route("/json", methods=["POST"])
def json():
    """json返回示例"""
    body = request.get_json()
    return json_response(**body)


@blueprint.route('/login_api_demo', methods=['POST'])
def login_demo():
    body = request.json()
    result = userLogin(**body)
    return json_response(**result)


def userLogin(username, password):
    if not username or not password:
        # 因为没有入参，访问demo一定会返回“用户名和密码不可为空”的示例
        return {"status": 1, "msg": "用户名和密码不可为空"}
    query = (Users.query.with_entities(
        Users.id, Users.password).filter_by(email_addr=username).first())
    if query is None:
        return {"status": 1, "msg": "用户名或密码错误"}
    if gen_md5_password(password) != query.password:
        return {"status": 1, "msg": "用户名或密码错误"}

    token = gen_token(32)
    # 为了能让demo跑起来，免得还要开个Redis，禁用这一行代码
    # Redis.write("session/{}".format(token), query.id)
    return {
        "data": {
            "token": token,
            "expTime": int(round(time() * 1000)) + 172800000
        }
    }
