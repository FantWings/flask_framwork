# from flask_cors import CORS
from flask import Flask
from config import FlaskConfig
from utils.database import db
from blueprints.bp_index import blueprint as index

app = Flask(__name__)
app.config.from_object(FlaskConfig)
# CORS(app, supports_credentials=True)

with app.app_context():
    # 运行时初始化数据库
    db.init_app(app)
    # 创建数据库表
    db.create_all()

# 蓝图
app.register_blueprint(blueprint=index)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=9090)
