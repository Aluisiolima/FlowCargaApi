from datetime import date, datetime, time

from sqlalchemy import (
    Date,
    DateTime,
    Enum as SAEnum,
    ForeignKey,
    Index,
    Text,
    Time,
    func,
)
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.base_model import Base
from src.core.types import StatusAgendamento

from typing import TYPE_CHECKING
if TYPE_CHECKING:   
    from src.core.repository import Supervisor, Doca, Transporte

class Agendamento(Base):
    __tablename__ = "agendamentos"

    __table_args__ = (
        Index("ix_agendamentos_doca_data", "doca_id", "data_agendamento"),
        Index("ix_agendamentos_data_status", "data_agendamento", "status"),
    )

    supervisor_id: Mapped[int | None] = mapped_column(
        ForeignKey("supervisores.id")
    )
    doca_id: Mapped[int] = mapped_column(
        ForeignKey("docas.id"), nullable=False
    )
    transporte_id: Mapped[int] = mapped_column(
        ForeignKey("transportes.id"), nullable=False
    )

    data_agendamento: Mapped[date] = mapped_column(Date, nullable=False)
    horario_inicio: Mapped[time] = mapped_column(Time, nullable=False)
    horario_fim: Mapped[time] = mapped_column(Time, nullable=False)

    status: Mapped[StatusAgendamento] = mapped_column(
        SAEnum(
            StatusAgendamento,
            name="status_agendamento",
            values_callable=lambda enum: [item.value for item in enum],
        ),
        default=StatusAgendamento.PENDENTE,
        nullable=False,
    )

    checkin_em: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True)
    )
    inicio_descarga: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True)
    )
    fim_descarga: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True)
    )
    checkout_em: Mapped[datetime | None] = mapped_column(
        DateTime(timezone=True)
    )

    observacoes: Mapped[str | None] = mapped_column(Text)
    motivo_cancelamento: Mapped[str | None] = mapped_column(Text)


    supervisor: Mapped["Supervisor | None"] = relationship(
        back_populates="agendamentos"
    )
    doca: Mapped["Doca"] = relationship(back_populates="agendamentos")
    transporte: Mapped["Transporte"] = relationship(
        back_populates="agendamentos"
    )