from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class UserPreference(Base):
    __tablename__='user_preferences'
    id:Mapped[int] = mapped_column(primary_key=True)
    user_id:Mapped[str]
    preferred_airline:Mapped[str]
    seat_type:Mapped[str]
    budget:Mapped[int]
