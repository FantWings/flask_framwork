from utils.database import model
from sqlalchemy import Integer, String, Column, DateTime, ForeignKey

from sqlalchemy.sql import functions


class Users(model):
    """用户表"""
    __tablename__ = "t_users"
    id = Column(Integer, primary_key=True, nullable=False, comment="索引")
    nickname = Column(String(16), nullable=False, comment="用户名")
    uuid = Column(String(64), nullable=False, comment="用户UUID")
    avatar = Column(String(256), comment="头像")
    password = Column(String(32), comment="密码")
    phone = Column(
        String(11),
        nullable=True,
        comment="手机号",
        unique=True,
    )
    qq = Column(String(13), comment="QQ号")
    create_time = Column(DateTime,
                         nullable=False,
                         server_default=functions.now(),
                         comment="创建时间")
    update_time = Column(
        DateTime,
        nullable=False,
        server_default=functions.now(),
        comment="修改时间",
        onupdate=functions.now(),
    )
    # 外键
    email_id = Column(Integer,
                      ForeignKey("t_email.id"),
                      nullable=False,
                      comment="邮箱ID")
