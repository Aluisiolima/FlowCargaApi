from typing import TYPE_CHECKING

from sqlalchemy import Boolean, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.base_model import Base

if TYPE_CHECKING:
    from src.core.repository import Transporte


class Motorista(Base):
    __tablename__ = "motoristas"

    nome: Mapped[str] = mapped_column(String(150), nullable=False)
    cpf: Mapped[str] = mapped_column(String(11), unique=True, nullable=False)
    cnh: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    categoria_cnh: Mapped[str | None] = mapped_column(String(5))
    telefone: Mapped[str | None] = mapped_column(String(20))
    email: Mapped[str | None] = mapped_column(String(150), unique=True, nullable=True)
    senha_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    ativo: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    transportes: Mapped[list["Transporte"]] = relationship(back_populates="motorista")
