import datetime

from config import PG_DSN

from sqlalchemy import Integer, DateTime, String, Boolean, func, Text
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine

engine = create_async_engine(
    PG_DSN,
)

Session = async_sessionmaker(bind=engine, expire_on_commit=False)

class Base(AsyncAttrs, DeclarativeBase):
    pass


class Todo(Base):
    __tablename__ = 'todo'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(200), nullable=False)
    important: Mapped[bool] = mapped_column(Boolean, default=False)
    done: Mapped[bool] = mapped_column(Boolean, default=False)
    start_time: Mapped[datetime.datetime] = mapped_column(
        DateTime,
        server_default=func.now()
    )
    finish_time: Mapped[datetime.datetime] = mapped_column(DateTime, nullable=True)


    @property
    def dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'important': self.important,
            'done': self.done,
            'start_time': self.start_time.isoformat(),
            'finish_time': self.finish_time.isoformat() if self.finish_time else None
        }


class Advertisement(Base):
    __tablename__ = "adv"

    id = mapped_column(Integer, primary_key=True)
    heading = mapped_column(String(20), nullable=False)
    description = mapped_column(Text)
    date_of_creation = mapped_column(
        DateTime,
        server_default=func.now()
    )
    user_id = mapped_column(Integer)



    @property
    def dict(self):

        return {
            "id": self.id,
            "heading": self.heading,
            "description": self.description,
            "date_of_creation": self.date_of_creation.isoformat(),
            "user_id": self.user_id,
        }
