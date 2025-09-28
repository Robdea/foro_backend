from ..db.mysql_bd import Base
import uuid
from sqlalchemy import Column, String, Text, DateTime, ForeignKey
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.mysql import CHAR  


class Posts(Base):
    __tablename__="posts"
    id = Column(CHAR(36, collation="utf8mb4_general_ci"), primary_key=True, default=lambda: str(uuid.uuid4()))
    title = Column(String(100), nullable=False)
    content = Column(Text, nullable=False)
    author_id = Column(CHAR(36, collation="utf8mb4_general_ci"), ForeignKey("users.id"))
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    
    user = relationship("User", back_populates="posts")    