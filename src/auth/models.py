from sqlalchemy import ForeignKey, text, Text
from sqlalchemy.orm import relationship, Mapped, mapped_column
from src.database import Base, str_uniq, int_pk, str_null_true , str_nullable


# создаем модель таблицы студентов
class Applicant(Base):
    id: Mapped[int_pk]
    phone_number: Mapped[str_uniq]
    first_name: Mapped[str]
    last_name: Mapped[str]
    first_name_fa : Mapped[str]
    email: Mapped[str_uniq]
    snils : Mapped[str_uniq]
    role_id: Mapped[int] = mapped_column(ForeignKey("roles.id"), nullable=False)
    
    role: Mapped["Role"] = relationship("Role", back_populates="applicants")

    def __str__(self):
        return (f"{self.__class__.__name__}(id={self.id}, "
                f"first_name={self.first_name!r},"
                f"last_name={self.last_name!r})")

    def __repr__(self):
        return str(self)


# создаем модель таблицы факультетов (majors)
class Role(Base):
    id: Mapped[int_pk]
    permission : Mapped[str_nullable]
    count_applicants: Mapped[int] = mapped_column(server_default=text('0'))

    def __str__(self):
        return f"{self.__class__.__name__}(id={self.id}, major_name={self.major_name!r})"

    def __repr__(self):
        return str(self)