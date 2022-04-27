from utils.database import model
from sqlalchemy import Integer, String, Column, DateTime
from sqlalchemy.orm import relationship, backref
from sqlalchemy.sql import functions
from .t_user import Users


class Email(model):
    """邮箱表"""
    __tablename__ = "t_email"
    id = Column(Integer, primary_key=True, nullable=False, comment="索引")
    addr = Column(String(32), nullable=False, comment="邮箱")
    active = Column(Integer, nullable=False, default=0, comment="邮箱已验证")
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

    # 反向引用
    owner = relationship(
        Users,
        backref=backref("bind_email"),
    )
