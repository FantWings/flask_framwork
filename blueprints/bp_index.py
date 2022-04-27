from uuid import uuid1
from flask import request, Blueprint
from time import time

from utils.response import json_response
from utils.generator import gen_md5_password, gen_token
from utils.database import session

from tables.t_user import Users
from tables.t_email import Email

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
    return json_response(data=body)


@blueprint.route('/add', methods=["POST"])
def demo_sql_add():
    body = request.get_json()
    if body is None:
        return json_response(msg="参数错误", status=1)

    # 增加一个邮箱
    EMAIL_ADD = Email(addr=body['email'])
    session.add(EMAIL_ADD)
    session.flush()

    # 增加一个用户，并与其将邮箱进行关联
    USER_ADD = Users(password=gen_md5_password(body['password']),
                     nickname=body['nickname'],
                     uuid=uuid1().hex,
                     email_id=EMAIL_ADD.id)
    session.add(USER_ADD)

    # 提交数据库修改
    session.commit()

    return json_response(msg="用户创建成功")


@blueprint.route('/query', methods=["GET"])
def demo_sql_query():
    nickname = request.args.get('nickname')
    email = request.args.get('email')
    if nickname:
        QUERY_RESULT = Users.query.filter_by(nickname=nickname).first()
        if QUERY_RESULT is None:
            return json_response(msg="数据不存在", status=1)
        return json_response({
            'data': {
                'nickname': QUERY_RESULT.nickname,
                'password': QUERY_RESULT.password,
                'email': QUERY_RESULT.bind_email.addr,
                'token': gen_token(32),
                "expTime": int(round(time() * 1000)) + 172800000
            }
        })
    if email:
        QUERY_RESULT = Email.query.filter_by(addr=email).first()
        if QUERY_RESULT is None:
            return json_response(msg="数据不存在", status=1)

        data = list()
        for users in QUERY_RESULT.owner:
            data.append({
                'nickname': users.nickname,
                'password': users.password,
                'email': QUERY_RESULT.addr,
                'token': gen_token(32),
                "expTime": int(round(time() * 1000)) + 172800000
            })
        return json_response(data)
    else:
        return json_response(msg="数据不存在", status=1)
