from decimal import Decimal
from typing import TYPE_CHECKING

from sqlalchemy import (
    Boolean,
    Numeric,
    String,
)
from sqlalchemy import (
    Enum as SAEnum,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.base_model import Base
from src.core.types import StatusDoca

if TYPE_CHECKING:
    from src.core.repository import Agendamento


class Doca(Base):
    __tablename__ = "docas"

    numero: Mapped[str] = mapped_column(String(20), unique=True, nullable=False)
    descricao: Mapped[str | None] = mapped_column(String(255))
    localizacao: Mapped[str | None] = mapped_column(String(150))

    capacidade_maxima_kg: Mapped[Decimal | None] = mapped_column(Numeric(12, 2))

    status: Mapped[StatusDoca] = mapped_column(
        SAEnum(
            StatusDoca,
            name="status_doca",
            values_callable=lambda enum: [item.value for item in enum],
        ),
        default=StatusDoca.DISPONIVEL,
        nullable=False,
    )

    ativo: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)

    agendamentos: Mapped[list["Agendamento"]] = relationship(back_populates="doca")
