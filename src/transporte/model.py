from datetime import datetime

from sqlalchemy import (
    DateTime,
    Enum as SAEnum,
    ForeignKey,
    String,
    Text,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.base_model import Base
from src.core.types import StatusTransporte

from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from src.core.repository import Motorista, Caminhao, Carga, Agendamento


class Transporte(Base):
    __tablename__ = "transportes"

    motorista_id: Mapped[int] = mapped_column(
        ForeignKey("motoristas.id"), nullable=False
    )
    caminhao_id: Mapped[int] = mapped_column(
        ForeignKey("caminhoes.id"), nullable=False
    )
    carga_id: Mapped[int] = mapped_column(
        ForeignKey("cargas.id"), nullable=False
    )

    codigo_transporte: Mapped[str | None] = mapped_column(
        String(50), unique=True
    )

    data_saida: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True)
    )
    previsao_chegada: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True)
    )
    chegada_real: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True)
    )

    status: Mapped[StatusTransporte] = mapped_column(
        SAEnum(
            StatusTransporte,
            name="status_transporte",
            values_callable=lambda enum: [item.value for item in enum],
        ),
        default=StatusTransporte.SOLICITADO,
        nullable=False,
    )

    observacoes: Mapped[str | None] = mapped_column(Text)

    
    motorista: Mapped["Motorista"] = relationship(
        back_populates="transportes"
    )
    caminhao: Mapped["Caminhao"] = relationship(
        back_populates="transportes"
    )
    carga: Mapped["Carga"] = relationship(back_populates="transportes")

    agendamentos: Mapped[list["Agendamento"]] = relationship(
        back_populates="transporte"
    )