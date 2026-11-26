from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy import Integer, String, ForeignKey
from database import Base
from datetime import datetime, UTC


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    product: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    quantity: Mapped[int] = mapped_column(Integer, nullable=False)
    status: Mapped[str] = mapped_column(String(20), nullable=False)
    created_at: Mapped[datetime] = mapped_column(
        datetime(timezone=True),
        nullable=False, 
        default=lambda: datetime.now(UTC),
    )
