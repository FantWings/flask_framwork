from flask_sqlalchemy import SQLAlchemy

# 实例化SQL Alchemy
db = SQLAlchemy()
session = db.session
model = db.Model
