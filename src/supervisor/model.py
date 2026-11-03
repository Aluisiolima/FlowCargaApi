from datetime import datetime

from sqlalchemy import Boolean, DateTime, Enum as SAEnum, String, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.base_model import Base
from src.core.types import TipoUsuario

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.core.repository import Agendamento, Relatorio


class Supervisor(Base):
    __tablename__ = "supervisores"

    nome: Mapped[str] = mapped_column(String(150), nullable=False)
    email: Mapped[str] = mapped_column(
        String(150), unique=True, nullable=False
    )
    senha_hash: Mapped[str] = mapped_column(String(255), nullable=False)
    telefone: Mapped[str | None] = mapped_column(String(20))

    tipo: Mapped[TipoUsuario] = mapped_column(
        SAEnum(
            TipoUsuario,
            name="tipo_usuario",
            values_callable=lambda enum: [item.value for item in enum],
        ),
        default=TipoUsuario.SUPERVISOR,
        nullable=False,
    )

    ativo: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)


    agendamentos: Mapped[list["Agendamento"]] = relationship(
        back_populates="supervisor"
    )

    relatorios: Mapped[list["Relatorio"]] = relationship(
        back_populates="supervisor"
    )