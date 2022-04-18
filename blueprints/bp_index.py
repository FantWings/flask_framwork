from flask import request, Blueprint
from utils.response import json_response

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