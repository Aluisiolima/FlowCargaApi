from datetime import date
from decimal import Decimal
from typing import TYPE_CHECKING

from sqlalchemy import Date, ForeignKey, Integer, Numeric, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.core.base_model import Base

if TYPE_CHECKING:
    from src.supervisor.model import Supervisor


class Relatorio(Base):
    __tablename__ = "relatorios"

    supervisor_id: Mapped[int] = mapped_column(
        ForeignKey("supervisores.id"), nullable=False
    )

    titulo: Mapped[str] = mapped_column(String(200), nullable=False)
    tipo_relatorio: Mapped[str | None] = mapped_column(String(100))

    data_inicio: Mapped[date] = mapped_column(Date, nullable=False)
    data_fim: Mapped[date] = mapped_column(Date, nullable=False)

    total_agendamentos: Mapped[int] = mapped_column(
        Integer, default=0, server_default="0", nullable=False
    )
    total_concluidos: Mapped[int] = mapped_column(
        Integer, default=0, server_default="0", nullable=False
    )
    total_cancelados: Mapped[int] = mapped_column(
        Integer, default=0, server_default="0", nullable=False
    )

    tempo_medio_descarga_min: Mapped[Decimal | None] = mapped_column(Numeric(10, 2))

    observacoes: Mapped[str | None] = mapped_column(Text)
    supervisor: Mapped["Supervisor"] = relationship(back_populates="relatorios")
