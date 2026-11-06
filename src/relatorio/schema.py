from datetime import date
from decimal import Decimal
from typing import TYPE_CHECKING

from pydantic import Field

from src.core.base_schema import Base

if TYPE_CHECKING:
    from src.core.schemas import SupervisorResponse


class RelatorioResponse(Base):
    supervisor_id: int

    titulo: str
    tipo_relatorio: str | None = None

    data_inicio: date
    data_fim: date

    total_agendamentos: int
    total_concluidos: int
    total_cancelados: int

    tempo_medio_descarga_min: Decimal | None = None

    observacoes: str | None = None

    supervisor: SupervisorResponse | None = None


class RelatorioCreate(Base):
    supervisor_id: int = Field(..., gt=0)

    titulo: str = Field(..., min_length=1, max_length=200)
    tipo_relatorio: str | None = Field(None, max_length=100)

    data_inicio: date
    data_fim: date

    observacoes: str | None = None


class RelatorioUpdate(Base):
    supervisor_id: int | None = Field(None, gt=0)

    titulo: str | None = Field(None, min_length=1, max_length=200)
    tipo_relatorio: str | None = Field(None, max_length=100)

    data_inicio: date | None = None
    data_fim: date | None = None

    observacoes: str | None = None
